import os
from . import app

# TODO: cli options to change host and port

app.start(os.getenv("IP") or "localhost", 6464)
