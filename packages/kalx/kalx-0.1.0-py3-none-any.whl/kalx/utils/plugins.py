"""
Plugin system for kalX.
"""
import os
import json
from pathlib import Path
from typing import Dict, List
from rich.console import Console
from rich.table import Table
from kalx.utils.logger import get_logger

logger = get_logger(__name__)
console = Console()

class PluginManager:
    """Manages kalX plugins."""
    
    def __init__(self):
        """Initialize the plugin manager."""
        self.plugin_dir = os.path.join(Path.home(), ".kalx", "plugins")
        self.config_file = os.path.join(self.plugin_dir, "plugins.json")
        os.makedirs(self.plugin_dir, exist_ok=True)
        
        # Initialize or load plugin config
        if not os.path.exists(self.config_file):
            self._save_config({"installed": {}, "enabled": []})
    
    def _load_config(self) -> Dict:
        """Load plugin configuration."""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load plugin config: {e}")
            return {"installed": {}, "enabled": []}
    
    def _save_config(self, config: Dict) -> bool:
        """Save plugin configuration."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Failed to save plugin config: {e}")
            return False
    
    def list_plugins(self) -> None:
        """Display installed plugins."""
        config = self._load_config()
        
        table = Table(title="kalX Plugins")
        table.add_column("Name", style="cyan")
        table.add_column("Version", style="magenta")
        table.add_column("Status", style="green")
        table.add_column("Description", style="blue")
        
        for name, info in config["installed"].items():
            status = "Enabled" if name in config["enabled"] else "Disabled"
            table.add_row(
                name,
                info.get("version", "unknown"),
                status,
                info.get("description", "No description")
            )
        
        if not config["installed"]:
            console.print("[yellow]No plugins installed[/yellow]")
            console.print("\nTo install a plugin:")
            console.print("[cyan]kalx --plugin-install <url>[/cyan]")
        else:
            console.print(table)

    def install_plugin(self, url: str) -> bool:
        """Install a new plugin from URL."""
        console.print(f"[yellow]Plugin installation not yet implemented[/yellow]")
        console.print(f"Would install from: {url}")
        return False

    def enable_plugin(self, name: str) -> bool:
        """Enable an installed plugin."""
        config = self._load_config()
        
        if name not in config["installed"]:
            console.print(f"[red]Plugin '{name}' not installed[/red]")
            return False
            
        if name not in config["enabled"]:
            config["enabled"].append(name)
            if self._save_config(config):
                console.print(f"[green]Plugin '{name}' enabled[/green]")
                return True
        else:
            console.print(f"[yellow]Plugin '{name}' already enabled[/yellow]")
            
        return False

    def disable_plugin(self, name: str) -> bool:
        """Disable an installed plugin."""
        config = self._load_config()
        
        if name not in config["installed"]:
            console.print(f"[red]Plugin '{name}' not installed[/red]")
            return False
            
        if name in config["enabled"]:
            config["enabled"].remove(name)
            if self._save_config(config):
                console.print(f"[green]Plugin '{name}' disabled[/green]")
                return True
        else:
            console.print(f"[yellow]Plugin '{name}' already disabled[/yellow]")
            
        return False

    def remove_plugin(self, name: str) -> bool:
        """Remove an installed plugin."""
        config = self._load_config()
        
        if name not in config["installed"]:
            console.print(f"[red]Plugin '{name}' not installed[/red]")
            return False
            
        if name in config["enabled"]:
            config["enabled"].remove(name)
            
        del config["installed"][name]
        if self._save_config(config):
            console.print(f"[green]Plugin '{name}' removed[/green]")
            return True
            
        return False
