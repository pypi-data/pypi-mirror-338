"""Grid configuration utilities for BactoVision."""

import json
from pathlib import Path
from typing import Dict, Optional, Union


class GridConfig:
    """Grid configuration for BactoVision widgets.

    Manages grid parameters like rows, columns, and padding, with save/load functionality.
    """

    def __init__(
        self,
        num_x: int = 12,
        num_y: int = 8,
        pad_top: float = 50.0,
        pad_bottom: float = 60.0,
        pad_left: float = 90.0,
        pad_right: float = 50.0,
    ):
        """Initialize a GridConfig with grid dimensions and padding values.

        Args:
            num_x: Number of grid rows
            num_y: Number of grid columns
            pad_top: Top padding in pixels
            pad_bottom: Bottom padding in pixels
            pad_left: Left padding in pixels
            pad_right: Right padding in pixels
        """
        self.num_x = num_x
        self.num_y = num_y
        self.pad_top = pad_top
        self.pad_bottom = pad_bottom
        self.pad_left = pad_left
        self.pad_right = pad_right

    @classmethod
    def from_dict(cls, config_dict: Dict) -> "GridConfig":
        """Create a GridConfig instance from a dictionary.

        Args:
            config_dict: Dictionary with grid configuration parameters

        Returns:
            A new GridConfig instance
        """
        return cls(
            num_x=config_dict.get("num_x", 12),
            num_y=config_dict.get("num_y", 8),
            pad_top=config_dict.get("pad_top", 50.0),
            pad_bottom=config_dict.get("pad_bottom", 60.0),
            pad_left=config_dict.get("pad_left", 90.0),
            pad_right=config_dict.get("pad_right", 50.0),
        )

    def to_dict(self) -> Dict:
        """Convert the GridConfig to a dictionary.

        Returns:
            Dictionary with grid configuration parameters
        """
        return {
            "num_x": self.num_x,
            "num_y": self.num_y,
            "pad_top": self.pad_top,
            "pad_bottom": self.pad_bottom,
            "pad_left": self.pad_left,
            "pad_right": self.pad_right,
        }

    def save(self, path: Union[str, Path]) -> None:
        """Save the grid configuration to a JSON file.

        Args:
            path: Path to save the configuration file
        """
        path = Path(path)
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, path: Union[str, Path]) -> "GridConfig":
        """Load a grid configuration from a JSON file.

        Args:
            path: Path to the configuration file

        Returns:
            A new GridConfig instance

        Raises:
            FileNotFoundError: If the specified file doesn't exist
        """
        path = Path(path)
        with open(path, "r") as f:
            config_dict = json.load(f)
        return cls.from_dict(config_dict)

    def __repr__(self) -> str:
        """Return a string representation of the GridConfig."""
        args = ", ".join([f"{k}={v}" for k, v in self.to_dict().items()])
        return f"GridConfig({args})"


def load_grid_config(config_path: Optional[Union[str, Path]] = None) -> GridConfig:
    """Load grid configuration from a file, or return default config if path is None.

    Args:
        config_path: Path to the configuration file, or None for defaults

    Returns:
        GridConfig instance
    """
    if config_path is None:
        return GridConfig()
    return GridConfig.load(config_path)
