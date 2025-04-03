#!/usr/bin/env python3
"""
Cronflow - Cron Switch Decorator

This module provides a decorator that can be applied to any Python function
to enable/disable its execution based on cron control configuration.

Basic Usage:
    from cronflow import cron_switch
    
    @cron_switch
    def main():
        # Your script's main logic here
        pass
        
    if __name__ == "__main__":
        main()

Advanced Usage:
    # Configure custom paths
    @cron_switch(config_path="/path/to/config.json", log_dir="/path/to/logs")
    def main():
        pass
"""
import os
import sys
import json
import functools
import inspect
from datetime import datetime
from pathlib import Path
import logging
from typing import Optional, Union, Callable, Any

# Set up package logging
logger = logging.getLogger("cronflow")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def cron_switch(func=None, *, config_path=None, config_name="cron_control.json", 
                log_dir=None, log_name=None, env_var="CRON"):
    """
    Decorator that controls whether a function should run based on cron configuration.
    
    When applied to a function, this decorator will:
    1. Check if the script is running from cron (specified env variable is set)
    2. If running from cron, check if the script is enabled in the configuration
    3. If disabled, exit early without executing the function
    4. If enabled or not running from cron, execute the function normally
    
    Args:
        func (callable, optional): The function to decorate. 
        config_path (str, Path, optional): Path to configuration file. If None, uses script dir.
        config_name (str, optional): Name of the configuration file. Default: "cron_control.json"
        log_dir (str, Path, optional): Path to log directory. If None, uses script dir/logs.
        log_name (str, optional): Base name for log file. If None, uses script name.
        env_var (str, optional): Environment variable to check. Default: "CRON"
    
    Returns:
        callable: The decorated function
        
    Usage:
        # Basic usage
        @cron_switch
        def main():
            # Your code here
            pass
            
        # With custom config and log paths
        @cron_switch(config_path="/etc/cronflow", log_dir="/var/log/cronflow")
        def main():
            pass
    """
    # Handle both @cron_switch and @cron_switch() syntax
    if func is None:
        return lambda f: cron_switch(f, config_path=config_path, 
                                    config_name=config_name, 
                                    log_dir=log_dir,
                                    log_name=log_name,
                                    env_var=env_var)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get frame information for the script calling this decorator
        calling_frame = inspect.stack()[1]
        calling_script_path = calling_frame.filename
        calling_script = os.path.basename(calling_script_path)
        script_dir = Path(os.path.dirname(os.path.abspath(calling_script_path)))
        
        # Determine path to configuration file
        if config_path is None:
            cfg_path = script_dir / config_name
        else:
            cfg_path = Path(config_path) / config_name
        
        # Determine log directory and file
        if log_dir is None:
            logs_dir = script_dir / "logs"
        else:
            logs_dir = Path(log_dir)
        
        # Create logs directory if it doesn't exist
        logs_dir.mkdir(exist_ok=True, parents=True)
        
        # Set up log file name
        if log_name is None:
            log_file = logs_dir / f"{Path(calling_script).stem}_execution.log"
        else:
            log_file = logs_dir / f"{log_name}"
        
        # Check if running from cron or equivalent
        if env_var in os.environ:
            logger.debug(f"Running in {env_var} mode, checking configuration")
            
            # If config doesn't exist, assume disabled
            if not cfg_path.exists():
                message = f"{datetime.now()}: Cron job is disabled for {calling_script} (no config). Exiting."
                logger.warning(message)
                with open(log_file, "a") as f:
                    f.write(message + "\n")
                return None
            
            try:
                # Load the configuration
                with open(cfg_path, 'r') as f:
                    config = json.load(f)
                
                # Check if the script is in the config and enabled
                if not config.get(calling_script, False):
                    message = f"{datetime.now()}: Cron job is disabled for {calling_script}. Exiting."
                    logger.info(message)
                    with open(log_file, "a") as f:
                        f.write(message + "\n")
                    return None
                
                logger.debug(f"Cron job is enabled for {calling_script}, proceeding")
                
            except Exception as e:
                # If any error occurs, log it and assume disabled
                message = f"{datetime.now()}: Error checking cron status for {calling_script}: {e}. Exiting."
                logger.error(message)
                with open(log_file, "a") as f:
                    f.write(message + "\n")
                return None
        
        # Log execution
        try:
            with open(log_file, "a") as f:
                f.write(f"{datetime.now()}: Script started execution\n")
        except Exception as e:
            logger.error(f"Error writing to log file {log_file}: {e}")
        
        # Execute the function
        try:
            result = func(*args, **kwargs)
            
            # Log successful completion
            try:
                with open(log_file, "a") as f:
                    f.write(f"{datetime.now()}: Script completed successfully\n")
            except Exception as e:
                logger.error(f"Error writing to log file {log_file}: {e}")
                
            return result
            
        except Exception as e:
            # Log the exception
            error_message = f"{datetime.now()}: Script failed with error: {str(e)}\n"
            logger.error(error_message)
            try:
                with open(log_file, "a") as f:
                    f.write(error_message)
            except Exception as log_error:
                logger.error(f"Error writing to log file {log_file}: {log_error}")
            
            # Re-raise the exception
            raise
    
    return wrapper

# Example of usage
if __name__ == "__main__":
    @cron_switch
    def test_function():
        """Test function to demonstrate the decorator"""
        print("This is a test function")
        return "Success"
    
    # Configure logging for the test
    logging.basicConfig(level=logging.DEBUG)
    
    result = test_function()
    print(f"Result: {result}")