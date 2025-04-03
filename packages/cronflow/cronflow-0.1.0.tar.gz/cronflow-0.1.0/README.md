# Cronflow

[![PyPI version](https://img.shields.io/pypi/v/cronflow.svg)](https://pypi.org/project/cronflow/)
[![Python Versions](https://img.shields.io/pypi/pyversions/cronflow.svg)](https://pypi.org/project/cronflow/)
[![License](https://img.shields.io/pypi/l/cronflow.svg)](https://github.com/jinwenliu/cronflow/blob/main/LICENSE)

A lightweight Python package for controlling cron job execution with a simple decorator.

## Overview

Cronflow allows you to easily enable or disable Python scripts that run via cron without modifying your crontab entries. By using a simple decorator, you can control which scripts run based on a centralized configuration file.

**Key Features:**

- Simple decorator syntax for enabling/disabling cron jobs
- No need to modify crontab entries to enable/disable scripts
- Centralized configuration for managing multiple scripts
- Automatic logging of script execution
- Customizable configuration and log paths

## Installation

```bash
pip install cronflow
```

## Basic Usage

1. **Import the decorator:**

```python
from cronflow import cron_switch
```

2. **Apply it to your main function:**

```python
@cron_switch
def main():
    # Your code here...
    print("Processing data...")

if __name__ == "__main__":
    main()
```

3. **Create a configuration file:**

Create a `cron_control.json` file in the same directory as your script:

```json
{
  "your_script.py": true,
  "another_script.py": false
}
```

4. **Run your script from cron with the CRON environment variable:**

```crontab
CRON=true
0 8 * * * cd /path/to/scripts && python your_script.py
```

Now `your_script.py` will only run if it's set to `true` in the configuration file. You can disable it without modifying your crontab by simply changing the configuration.

## Advanced Usage

### Custom Configuration Path

You can specify a custom path for the configuration file:

```python
@cron_switch(config_path="/etc/cronflow", config_name="cron_config.json")
def main():
    # Your code here...
```

### Custom Log Directory

Customize where logs are stored:

```python
@cron_switch(log_dir="/var/log/cronflow")
def main():
    # Your code here...
```

### Custom Environment Variable

Use a different environment variable instead of "CRON":

```python
@cron_switch(env_var="SCHEDULED_RUN")
def main():
    # Your code here...
```

## Configuration Management

You can create/edit the `cron_control.json` file manually or use a script:

```python
import json

def enable_script(script_name, config_path="cron_control.json"):
    with open(config_path, "r") as f:
        config = json.load(f)
    
    config[script_name] = True
    
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Enabled {script_name}")

def disable_script(script_name, config_path="cron_control.json"):
    with open(config_path, "r") as f:
        config = json.load(f)
    
    config[script_name] = False
    
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Disabled {script_name}")
```

## How It Works

1. When a Python script with the `@cron_switch` decorator runs, it checks if the `CRON` environment variable is set
2. If running from cron, it checks the configuration file to see if the script is enabled
3. If disabled, it exits immediately without executing the main logic
4. If enabled or not running from cron, it continues with normal execution

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
