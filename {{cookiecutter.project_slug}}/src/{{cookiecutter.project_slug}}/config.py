import yaml
import os
from box import Box
import logging.config
from pathlib import Path
from dotenv import load_dotenv

try:
    env = os.environ["ENVIRONMENT"]  # dev/prod
except KeyError:
    env = 'dev'


env_path = Path('.') / '.env'
load_dotenv(env_path)

config_path = Path(__file__).parent.parent.parent.joinpath('configs', 'config.yaml')

with open(config_path, "r") as config_file:
    full_cfg = yaml.safe_load(config_file)

cfg = Box({**full_cfg["base"], **full_cfg[env]}, default_box=True, default_box_attr=None)
cfg.environment = env

# create logs paths if not exist
os.makedirs(cfg.path.logs, exist_ok=True)

if os.path.exists(cfg.path.log_config):
    with open(cfg.path.log_config, "r") as ymlfile:
        log_config = yaml.safe_load(ymlfile)

    # Set up the logger configuration
    logging.config.dictConfig(log_config)
else:
    raise FileNotFoundError(f"Log yaml configuration file not found in {cfg.path.log_config}")
