# TODO: fix _ variable source
# TODO: variable bindings
# TODO: support comments (`5 # foo` works, `# foo` does not)

import io
import sys
import traceback
from typing import Any

from bedrock.consts import NAME
from bedrock.context import ConnectContext, PlayerMessageContext, ReadyContext
from bedrock.ext import ui
from bedrock.server import Server
from bedrock.utils import rawtext

def format_exception(exc: BaseException) -> str:
    return ui.red("".join(traceback.format_exception_only(exc)))  # type: ignore

app = Server()

last: Any = None
variables: dict[str, Any] = {}

@app.server_event
async def connect(ctx: ConnectContext) -> None:
    await ctx.server.run(f'tellraw @a {rawtext(ui.dark_red(ui.bold("WARNING")))}')
    await ctx.server.run(f'tellraw @a {rawtext(ui.red("Any code entered in the chat will be executed and might affect your system."))}')

@app.server_event
async def ready(ctx: ReadyContext) -> None:
    print(f"Ready @ {ctx.host}:{ctx.port}")

@app.game_event
async def player_message(ctx: PlayerMessageContext) -> None:
    global last, variables

    if ctx.sender == NAME:
        return
    
    sys.stdout = io.StringIO()

    try:
        code = compile(ctx.message, filename="chat", mode="single")
    except SyntaxError as exc:
        result = format_exception(exc)
    else:
        try:
            exec(code, {"_": last, "__run__": ctx.server.run} | variables)
        except SystemExit:
            raise
        except BaseException as exc:
            result = format_exception(exc)
        else:
            result = sys.stdout.getvalue()
            last = eval(result, variables)  # do not capture print result
    
    await ctx.server.run(f"tellraw @a {rawtext(result)}")
    sys.stdout = sys.__stdout__
