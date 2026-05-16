import json
import os
import shutil
import sys

# Determine base paths
if getattr(sys, 'frozen', False):
    # Running in a bundle (PyInstaller)
    bundle_dir = sys._MEIPASS
    exe_dir = os.path.dirname(sys.executable)
else:
    # Running in normal Python environment
    bundle_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    exe_dir = bundle_dir

config_path = os.path.join(exe_dir, "config.json")
default_config_path = os.path.join(bundle_dir, "default.config.json")

# If config.json does not exist, copy from default.config.json
if not os.path.exists(config_path) and os.path.exists(default_config_path):
    shutil.copy(default_config_path, config_path)

if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file 'config.json' not found at {config_path}. Please create it or copy from 'default.config.json' and make sure the name is correct.")

# Load configuration from config.json
with open(config_path, "r", encoding="utf-8") as config_file:
    config = json.load(config_file)