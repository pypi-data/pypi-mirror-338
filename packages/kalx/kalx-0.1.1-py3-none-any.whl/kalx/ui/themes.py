# kalx/ui/themes.py
"""
Themes for the kalX console interface.
"""

from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Theme:
    """
    Theme configuration for the console UI.
    """
    background: str
    foreground: str
    accent: str
    text: str
    error: str
    warning: str
    success: str
    info: str
    dim: str
    
    @classmethod
    def to_dict(cls, theme):
        """Convert a Theme to a dictionary."""
        return {
            "background": theme.background,
            "foreground": theme.foreground,
            "accent": theme.accent,
            "text": theme.text,
            "error": theme.error,
            "warning": theme.warning,
            "success": theme.success,
            "info": theme.info,
            "dim": theme.dim
        }

# Predefined themes
THEMES = {
    "dark": Theme(
        background="black",
        foreground="white",
        accent="green",
        text="white",
        error="red",
        warning="yellow",
        success="green",
        info="cyan",
        dim="gray"
    ),
    "matrix": Theme(
        background="black",
        foreground="green",
        accent="bright_green",
        text="green",
        error="red",
        warning="yellow",
        success="bright_green",
        info="cyan",
        dim="dark_green"
    ),
    "blue": Theme(
        background="navy",
        foreground="white",
        accent="cyan",
        text="white",
        error="red",
        warning="yellow",
        success="green",
        info="cyan",
        dim="gray"
    ),
    "amber": Theme(
        background="black",
        foreground="yellow",
        accent="orange",
        text="yellow",
        error="red",
        warning="orange",
        success="green",
        info="cyan",
        dim="dark_orange"
    ),
    "light": Theme(
        background="white",
        foreground="black",
        accent="blue",
        text="black",
        error="red",
        warning="orange",
        success="green",
        info="blue",
        dim="gray"
    )
}

def get_theme(name: str) -> Theme:
    """
    Get a theme by name.
    
    Args:
        name: Name of the theme
        
    Returns:
        Theme: The requested theme or default dark theme
    """
    return THEMES.get(name, THEMES["dark"])

def create_custom_theme(config: Dict[str, Any]) -> Theme:
    """
    Create a custom theme from configuration.
    
    Args:
        config: Theme configuration
        
    Returns:
        Theme: The custom theme
    """
    return Theme(
        background=config.get("background", "black"),
        foreground=config.get("foreground", "white"),
        accent=config.get("accent", "green"),
        text=config.get("white", "white"),
        error=config.get("error", "red"),
        warning=config.get("warning", "yellow"),
        success=config.get("green", "green"),
        info=config.get("info", "cyan"),
        dim=config.get("dim", "gray")
    )
