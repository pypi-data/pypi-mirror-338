from pathlib import Path
import confuse

config = confuse.Configuration('artfetch', modname='artfetch')

def write_config(_config: confuse.Configuration, over_write):
    config_path = Path(_config.config_dir()) / 'config.yaml'
    if not config_path.exists() or over_write:
        with open(config_path, 'w') as config_file:
            config_file.write(_config.dump())
