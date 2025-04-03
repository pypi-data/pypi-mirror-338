"""
Configuration management for kalX.
"""

import os
from configparser import ConfigParser
from pathlib import Path
from kalx.utils.logger import get_logger
from kalx.utils.encryption import decrypt_credentials

logger = get_logger(__name__)

# Package directories
PACKAGE_DIR = Path(__file__).parent.parent
DATA_DIR = PACKAGE_DIR / "data"
CREDENTIALS_PATH = DATA_DIR / "firebase_credentials.json"

# User config directory (for user settings only)
USER_CONFIG_DIR = Path.home() / ".kalx"
USER_CONFIG_PATH = USER_CONFIG_DIR / "config.ini"

# Default configuration values
DEFAULT_CONFIG = {
    'firebase': {
        'credentials_path': str(CREDENTIALS_PATH)  # package credentials
    },
    'ui': {
        'theme': 'dark'
    },
    'logging': {
        'level': 'INFO'
    },
    'network': {
        'server_host': 'api.kalx.io',
        'server_port': '443',
        'timeout': '30'
    }
}

def ensure_default_config():
    """Create default config file if it doesn't exist."""
    if not CREDENTIALS_PATH.exists():
        logger.error(f"Firebase credentials not found in package: {CREDENTIALS_PATH}")
        raise FileNotFoundError("Firebase credentials missing from package")

    USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    if not USER_CONFIG_PATH.exists():
        config = ConfigParser()
        # Only save UI and logging settings to user config
        config['ui'] = DEFAULT_CONFIG['ui']
        config['logging'] = DEFAULT_CONFIG['logging']
            
        with open(USER_CONFIG_PATH, 'w') as f:
            config.write(f)
        logger.info(f"Created default config at {USER_CONFIG_PATH}")

def get_config(config_path=None):
    """Get configuration."""
    # First verify package credentials exist
    if not CREDENTIALS_PATH.exists():
        logger.error(f"Firebase credentials not found in package: {CREDENTIALS_PATH}")
        raise FileNotFoundError("Firebase credentials missing from package")

    config = ConfigParser()
    
    # Start with all defaults including credential path
    for section, values in DEFAULT_CONFIG.items():
        config[section] = values

    # Load user settings (only UI and logging)
    if USER_CONFIG_PATH.exists():
        user_config = ConfigParser()
        user_config.read(USER_CONFIG_PATH)
        if 'ui' in user_config:
            config['ui'].update(user_config['ui'])
        if 'logging' in user_config:
            config['logging'].update(user_config['logging'])
    
    # Override credentials path with environment variable if set
    env_creds = os.environ.get('KALX_FIREBASE_CREDENTIALS')
    if env_creds:
        try:
            # Decrypt credentials if encrypted
            decrypted_creds = decrypt_credentials(env_creds)
            config['firebase']['credentials_json'] = decrypted_creds
            config['firebase']['use_env'] = 'true'
        except Exception as e:
            logger.warning(f"Failed to use environment credentials: {e}")
    
    return config

def update_config(section: str, key: str, value: str) -> bool:
    """Update a specific config value."""
    try:
        config = get_config()
        
        if section not in config:
            config[section] = {}
            
        config[section][key] = value
        
        config_path = os.path.join(Path.home(), ".kalx", "config.ini")
        with open(config_path, 'w') as f:
            config.write(f)
            
        return True
    except Exception as e:
        logger.error(f"Failed to update config: {e}")
        return False
