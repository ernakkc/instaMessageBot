# Account configuration file
# This file contains the configuration for the account
# It includes the account username, password, and other settings
# The configuration is stored in a JSON file; file name is accounts.json

import json
import os
from typing import Dict, Any

def load_account_config(file_path: str) -> Dict[str, Any]:
    """
    Load the account configuration from a JSON file.

    :param file_path: Path to the JSON file containing account configuration.
    :return: A dictionary containing account configurations. {id: {username, password, proxy}}
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the file is empty or contains no valid accounts.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Accounts file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        config = json.load(file).get('accounts', {})
    
    for _ in range(4):
        for account_id in config:
            if 'username' not in account_id or 'password' not in account_id:
                config.remove(account_id)

    account_count = len(config)
    if account_count == 0:
        raise ValueError(f"No accounts found in {file_path}.")
    
    return config
    
def save_account_config(file_path: str, config: Dict[str, Any]) -> None:
    """
    Save the account configuration to a JSON file.

    :param file_path: Path to the JSON file where account configuration will be saved.
    :param config: A dictionary containing account configurations. {id: {username, password}}
    """
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=4)
        
        
def isHaveProxy(account: Dict[str, Any]) -> bool:
    """
    Check if the account has a proxy.

    :param account: A dictionary containing account configuration.
    :return: True if the account has a proxy, False otherwise.
    """
    return 'proxy' in account and bool(account['proxy'])

