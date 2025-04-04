import copy
import json
import os.path
import typing
from pathlib import Path

from attr import dataclass
from tqdm import tqdm
from typing import Type, Optional, Callable

import inspect

from .communication import aiml_example, protolang_specs, generate_aiml_syntax, encode_aiml

from .communication import parse_aiml
from .tool import ToolDesc, parseFuncDesc, parseFuncParameters
from .config import Config, get_default_config

default_system_prompt = Path(os.path.dirname(__file__), "default_system_prompt.txt").read_text(encoding='utf-8')

chat_templates = {
  "qwq": Path(os.path.dirname(__file__), "chat_templates", "qwq.jinja").read_text(encoding='utf-8'),
}

# apply formatting
default_system_prompt = default_system_prompt.replace("%%PROTOCOL_DEFINITIONS%%", f"""
{aiml_example}
----
{protolang_specs}
""")

@dataclass
class Identity:
  name: str = 'Helper'                                  # The name of this agent.
  peer: str = 'User'                                    # Who is this agent talking to?
  purpose: str = 'Assist User. '                        # What does this agent trying to achieve?
  respond_gbnf: str = 'respond-format ::= (text-line)*' # GBNF respond format specification, must contain 'respond-format`.

class Agent:
    def __init__(self, identity: Identity = None, config: Config = None):
        if config is None:
          config = get_default_config()
        if identity is None:
          identity = Identity()
        self.identity: Identity = identity
        self.config: Config = config
        self.tool_desc: typing.Dict[str, ToolDesc] = {}
        self.tools: typing.Dict[str, Type[Callable[..., str]]] = {}
        self.system_msg = default_system_prompt
        self.msg_history = [
          {'role': 'system', 'content': self.system_msg},
        ]
    def register_tool(self, tool: any, name_prefix: str = None, exclude: typing.Optional[typing.List[str]] = None):
      """
      # Register a tool instance to this agent.
      tool: "The tool class instance. "
      name_prefix: "Prefix all tool methods in this instance with name_prefix, or None to use class name. "
      exclude: "A list of method names to exclude from adding as tools. "
      """
      if name_prefix is None:
        name_prefix = type(tool).__name__
      mem = inspect.getmembers(tool, predicate=inspect.ismethod)
      for v in mem:
        if not v[0].startswith('_') and (exclude is None or v[0] not in exclude):
          self.register_tool_func(v[1], name_prefix + '.' + v[0])
    def register_tool_func(self, f: Callable[..., str], name: Optional[str] = None):
      """
      # Register a tool function to this agent.
      f: "A function that returns a string, or a dict of string, each param should be annotated by types. "
      name: "Specify a name for this tool, or None to use function name as tool name. "
      """
      if name is None:
        name = f.__name__
      if name in self.tools:
        raise Exception(f'tool {name} already registered')
      self.tools[name] = f
      param_desc, param_list = parseFuncParameters(f)
      self.tool_desc[name] = ToolDesc(name=name, desc=parseFuncDesc(f), parameters=param_desc, param_names = param_list)

    # ---- core chatting functions ----
    def chat(self, message: Optional[str] = None, add = True, return_delta: bool = False):
      """
      # Send a message to this agent, and get RESPOND from it.
      message: "Text to send to the agent. "
      """
      history = copy.copy(self.msg_history)
      history[0]['content'] = (self.system_msg
                               .replace("%%NAME%%", self.identity.name)
                               .replace("%%PEER%%", self.identity.peer)
                               .replace("%%PURPOSE%%", self.identity.purpose)
                               .replace("%%TOOLS%%", "----\n".join([self.tool_desc[x].__str__() for x in self.tool_desc])))
      delta_history = [{'role': 'user', 'content': encode_aiml({'sender': 'peer ['+self.identity.peer+']', 'text': message})}]
      delta_history = self._run(history, delta_history)
      if add:
        for d in delta_history:
          self.msg_history.append(d)
      if return_delta:
        return delta_history
      # return latest generated AIML.
      parsed_last = parse_aiml(delta_history[-1]['content'])
      if 'respond' not in parsed_last:
        print(json.dumps(delta_history))
        print(parsed_last)
      return parsed_last['respond']
    # ---- internal calls ----
    def _run(self, history, delta_histories) -> typing.List[dict]:
      """
      # Run with delta_histories recursively, returns updated delta_histories.
      history: Existing history data.
      delta_histories: Only used for recursive calls, please pass in empty list [].
      """
      cloned_history = [*history, *delta_histories]
      # print(cloned_history[0]['content'])
      resp: str = self._call_llm(cloned_history)
      if '</think>' in resp:
        resp = resp[resp.rindex('</think>')+8:]
      # print(resp)
      aiml: dict = parse_aiml(resp)
      if aiml == {}:
        aiml = {'action': 'RESPOND', 'respond': ''} # default to respond nothing
      action = aiml['action']
      if action == 'RESPOND':
        delta_histories.append({'role': 'assistant', 'content': resp})
        return delta_histories
      if action == 'TOOLCALL':
        # cloned_aiml_without_params = dict([(k, v if not k.startswith('param:') and len(v) > 10 else '(...deducted from memory...)') for k, v in aiml.items()])
        # delta_histories.append({'role': 'assistant', 'content': encode_aiml(cloned_aiml_without_params)})
        delta_histories.append({'role': 'assistant', 'content': resp})
        tool_name = aiml['name']
        if tool_name in self.tools:
          tool = self.tools[tool_name]
          params = dict([(k[6:], aiml[k]) for k in aiml.keys() if k.startswith('param:')])
          print(f'{self.identity.name} call tool {tool_name}')
          # print(param)
          # import sys;sys.exit(0)
          if params == {}:
            tool_resp = tool()
          else:
            tool_resp = tool(**params)
          response_packet = {'sender': 'tool [' + tool_name + ']'}
          if isinstance(tool_resp, dict):
            for k, v in tool_resp.items():
              response_packet[f"output.{k}"] = v if isinstance(v, str) else str(v)
          elif isinstance(tool_resp, str):
            response_packet['output'] = tool_resp
          else:
            response_packet['output'] = str(tool_resp)
          print(response_packet)
          delta_histories.append({'role': 'user', 'content': encode_aiml(response_packet)})
        else:
          raise Exception(f'tool {aiml["name"]} not registered')
      else:
        delta_histories.append({'role': 'user', 'content': encode_aiml({'sender': 'n/a', 'text': "(waiting for respond)"})})
      return self._run(history, delta_histories)
    def _call_llm(self, history) -> str:
      """
      # Executes a single turn of LLM call.
      history: "Chat history [{\"role\": ..., \"content\": ...}, ...]"
      """
      extra_body: dict = {}

      if self.config.use_guided_generation:
        grammar_text = generate_aiml_syntax(self.identity.respond_gbnf, dict(
          [(x, self.tool_desc[x].param_names) for x in self.tool_desc]
        ))
        extra_body = dict(
          guided_grammar=grammar_text,
          guided_decoding_backend=self.config.guided_decoding_backend,
        )

      if self.config.chat_template_type is not None and self.config.chat_template_type in chat_templates:
        extra_body['chat_template'] = chat_templates[self.config.chat_template_type],
      if not self.config.show_generation:
        r = self.config.llm.chat.completions.create(
          model=self.config.model,
          messages=history,
          temperature=self.config.temperature,
          extra_body=extra_body,
          frequency_penalty=self.config.frequency_penalty,
          max_completion_tokens=self.config.generation_limit,
          stop="\n$$EOF$$" if self.config.use_stop_token else None
        )
        if r.choices[0].finish_reason != "stop":
          print(r.choices[0].message)
          print(f'WARNING: finish_reason={r.choices[0].finish_reason}')
          raise Exception("too long")
        if r.choices[0].message is None or len(r.choices[0].message.content) <= 0:
          print(r.choices[0])
          raise Exception("empty LLM response")
        return r.choices[0].message.content
      ##########
      r = self.config.llm.chat.completions.create(
        model=self.config.model,
        messages=history,
        temperature=self.config.temperature,
        extra_body=extra_body,
        frequency_penalty=self.config.frequency_penalty,
        max_completion_tokens=self.config.generation_limit,
        stop="\n$$EOF$$" if self.config.use_stop_token else None,
        stream=True
      )
      total = ''
      reasoning = ''
      resp = ''
      prog = tqdm(r, unit='')
      finish_reason = None

      entered_content = False
      for chunk in prog:
        # print(chunk.choices[0], flush=True)
        if hasattr(chunk.choices[0].delta, "reasoning_content"):
          total += chunk.choices[0].delta.reasoning_content
          reasoning += chunk.choices[0].delta.reasoning_content
          print(chunk.choices[0].delta.reasoning_content, end='', flush=True)
        elif hasattr(chunk.choices[0].delta, "content") and len(chunk.choices[0].delta.content) > 0:
          if not entered_content:
            entered_content=True
            # print("\n========\nOUTPUT: \n")
          total += chunk.choices[0].delta.content
          resp += chunk.choices[0].delta.content
          # print(chunk.choices[0].delta.content, end='', flush=True)
        if len(total) > self.config.progressbar_length:
          total = total[-self.config.progressbar_length:]
        prog.set_postfix_str(total.replace("\n", "").replace("\r", ""), refresh=False)
        finish_reason = chunk.choices[0].finish_reason
      if finish_reason == 'length':
        raise Exception('generation too long')
      return resp.lstrip("think>")
