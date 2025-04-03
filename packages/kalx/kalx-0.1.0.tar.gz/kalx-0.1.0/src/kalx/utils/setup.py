"""
Setup utilities for kalX.
"""

import os
import json
import shutil
import sys
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from kalx.utils.config import USER_CONFIG_DIR, get_config_dir

console = Console()

def setup_firebase():
    """Check Firebase setup."""
    from kalx.utils.config import CREDENTIALS_PATH
    
    if not CREDENTIALS_PATH.exists():
        raise FileNotFoundError(
            "Firebase credentials not found in package. "
            "This is a developer-only issue. End users should not see this error."
        )
    return True
