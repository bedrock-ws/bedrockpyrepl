# bedrockpyrepl

> Execute Python inside Minecraft

`bedrockpyrepl` is a Python REPL that can be used inside a Minecraft chat.
At the moment, not all features are supported yet:

* Variables are dropped immediately.
  
  ```text
  <PlayerName> a = 5
  <PlayerName> a + 1
    File "chat", line 1, in <module>
  NameError: name 'a' is not defined
  ```
* `print` cannot be used correctly
* use `__run__` function sync

Following features are intended to be unsupported:

* Multiline code such as:
  
  ```python
  >>> for i in range(5):
  ...     print(i)
  ...
  0
  1
  2
  3
  4
  5
  ```


## Features

* Use `_` to access the value returned by the last expression.
* `SystemExit` stops the program, other errors are displayed in the chat.

## Quickstart

1. Install bedrockpyrepl and its dependencies
  
   ```console
   pip install -U git+https://github.com/bedrock-ws/bedrockpyrepl.git
   ```
2. Set up
  [bedrockpy](https://bedrockpy.readthedocs.io/en/latest/setup.html).
3. Run the server.
  
   ```console
   python -m bedrockpyrepl
   ```
