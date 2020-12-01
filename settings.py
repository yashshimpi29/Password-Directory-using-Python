import os.path
from os import path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_DIR = "config"

CONFIG_PATH = os.path.join(
    ROOT_DIR, CONFIG_DIR
)
if (path.exists(CONFIG_PATH)):
    pass
else:
    os.mkdir(CONFIG_PATH)

creds_file = os.path.join(
    ROOT_DIR, "config", "creds.txt"
)

key_file = os.path.join(
    ROOT_DIR, "config", "key.txt"
)
