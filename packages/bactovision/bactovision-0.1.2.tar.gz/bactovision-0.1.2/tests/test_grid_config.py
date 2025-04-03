"""Tests for GridConfig functionality."""

import os
import tempfile
from pathlib import Path

import numpy as np

from bactovision.canvas_widget import CanvasWidget
from bactovision.grid_config import GridConfig, load_grid_config
from bactovision.widget import BactoWidget


def test_grid_config_init():
    """Test initialization of GridConfig with default and custom values."""
    # Test with default values
    config = GridConfig()
    assert config.num_x == 12
    assert config.num_y == 8
    assert config.pad_top == 50.0
    assert config.pad_bottom == 60.0
    assert config.pad_left == 90.0
    assert config.pad_right == 50.0

    # Test with custom values
    custom_config = GridConfig(
        num_x=5,
        num_y=10,
        pad_top=30.0,
        pad_bottom=40.0,
        pad_left=50.0,
        pad_right=60.0,
    )
    assert custom_config.num_x == 5
    assert custom_config.num_y == 10
    assert custom_config.pad_top == 30.0
    assert custom_config.pad_bottom == 40.0
    assert custom_config.pad_left == 50.0
    assert custom_config.pad_right == 60.0


def test_grid_config_to_from_dict():
    """Test converting GridConfig to and from dictionary."""
    config = GridConfig(
        num_x=15,
        num_y=20,
        pad_top=25.0,
        pad_bottom=35.0,
        pad_left=45.0,
        pad_right=55.0,
    )

    # Convert to dict
    config_dict = config.to_dict()
    assert config_dict["num_x"] == 15
    assert config_dict["num_y"] == 20
    assert config_dict["pad_top"] == 25.0
    assert config_dict["pad_bottom"] == 35.0
    assert config_dict["pad_left"] == 45.0
    assert config_dict["pad_right"] == 55.0

    # Create from dict
    new_config = GridConfig.from_dict(config_dict)
    assert new_config.num_x == 15
    assert new_config.num_y == 20
    assert new_config.pad_top == 25.0
    assert new_config.pad_bottom == 35.0
    assert new_config.pad_left == 45.0
    assert new_config.pad_right == 55.0


def test_grid_config_save_load():
    """Test saving and loading GridConfig to/from file."""
    config = GridConfig(
        num_x=3,
        num_y=4,
        pad_top=5.0,
        pad_bottom=6.0,
        pad_left=7.0,
        pad_right=8.0,
    )

    # Create temporary file
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        # Save config to file
        config.save(tmp_path)

        # Load config from file
        loaded_config = GridConfig.load(tmp_path)

        # Check values
        assert loaded_config.num_x == 3
        assert loaded_config.num_y == 4
        assert loaded_config.pad_top == 5.0
        assert loaded_config.pad_bottom == 6.0
        assert loaded_config.pad_left == 7.0
        assert loaded_config.pad_right == 8.0

        # Test with string path
        string_loaded = GridConfig.load(str(tmp_path))
        assert string_loaded.num_x == 3

        # Test with load_grid_config utility
        util_loaded = load_grid_config(tmp_path)
        assert util_loaded.num_x == 3

        # Test default with load_grid_config
        default_config = load_grid_config()
        assert default_config.num_x == 12
    finally:
        # Clean up
        if tmp_path.exists():
            os.unlink(tmp_path)


def test_canvas_widget_integration():
    """Test integration with CanvasWidget."""
    # Create a custom config
    config = GridConfig(
        num_x=5,
        num_y=6,
        pad_top=10.0,
        pad_bottom=20.0,
        pad_left=30.0,
        pad_right=40.0,
    )

    # Create widget
    widget = CanvasWidget()

    # Set grid config
    widget.set_grid_config(config)

    # Check values were applied
    assert widget.grid_num_x == 5
    assert widget.grid_num_y == 6
    assert widget.pad_top == 10.0
    assert widget.pad_bottom == 20.0
    assert widget.pad_left == 30.0
    assert widget.pad_right == 40.0

    # Get config back
    retrieved_config = widget.get_grid_config()

    # Check retrieved values
    assert retrieved_config.num_x == 5
    assert retrieved_config.num_y == 6
    assert retrieved_config.pad_top == 10.0
    assert retrieved_config.pad_bottom == 20.0
    assert retrieved_config.pad_left == 30.0
    assert retrieved_config.pad_right == 40.0


def test_bacto_widget_integration():
    """Test integration with BactoWidget."""
    # Create a dummy image for testing
    dummy_img = np.zeros((200, 300, 3), dtype=np.uint8)

    # Create a custom config
    config = GridConfig(
        num_x=7,
        num_y=9,
        pad_top=15.0,
        pad_bottom=25.0,
        pad_left=35.0,
        pad_right=45.0,
    )

    # Create widget with config
    widget = BactoWidget(img=dummy_img, grid_config=config)

    # Check config was applied to canvas widget
    assert widget.canvas_widget.grid_num_x == 7
    assert widget.canvas_widget.grid_num_y == 9
    assert widget.canvas_widget.pad_top == 15.0
    assert widget.canvas_widget.pad_bottom == 25.0
    assert widget.canvas_widget.pad_left == 35.0
    assert widget.canvas_widget.pad_right == 45.0

    # Test getting config
    retrieved_config = widget.get_grid_config()
    assert retrieved_config.num_x == 7
    assert retrieved_config.num_y == 9

    # Test setting new config
    new_config = GridConfig(
        num_x=3,
        num_y=4,
        pad_top=5.0,
        pad_bottom=6.0,
        pad_left=7.0,
        pad_right=8.0,
    )
    widget.set_grid_config(new_config)

    # Check new config was applied
    assert widget.canvas_widget.grid_num_x == 3
    assert widget.canvas_widget.grid_num_y == 4
    assert widget.canvas_widget.pad_top == 5.0
    assert widget.canvas_widget.pad_bottom == 6.0
    assert widget.canvas_widget.pad_left == 7.0
    assert widget.canvas_widget.pad_right == 8.0

    # Check UI components were updated
    assert widget.x_grid_size_text.value == 3
    assert widget.y_grid_size_text.value == 4
    assert widget.top_pad_slider.value == 5.0
    assert widget.bottom_pad_slider.value == 6.0
    assert widget.left_pad_slider.value == 7.0
    assert widget.right_pad_slider.value == 8.0


def test_file_path_integration():
    """Test using file paths instead of direct GridConfig instances."""
    # Create a dummy image for testing
    dummy_img = np.zeros((200, 300, 3), dtype=np.uint8)

    # Create and save a config
    config = GridConfig(
        num_x=3,
        num_y=4,
        pad_top=5.0,
        pad_bottom=6.0,
        pad_left=7.0,
        pad_right=8.0,
    )

    # Create temporary file
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        # Save config to file
        config.save(tmp_path)

        # Create widget with config path
        widget = BactoWidget(img=dummy_img, grid_config=tmp_path)

        # Check config was loaded and applied
        assert widget.canvas_widget.grid_num_x == 3
        assert widget.canvas_widget.grid_num_y == 4
        assert widget.canvas_widget.pad_top == 5.0
        assert widget.canvas_widget.pad_bottom == 6.0
        assert widget.canvas_widget.pad_left == 7.0
        assert widget.canvas_widget.pad_right == 8.0

        # Create a new config
        new_config = GridConfig(
            num_x=9,
            num_y=10,
            pad_top=11.0,
            pad_bottom=12.0,
            pad_left=13.0,
            pad_right=14.0,
        )

        # Save to a new file
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as new_tmp:
            new_tmp_path = Path(new_tmp.name)

        try:
            new_config.save(new_tmp_path)

            # Update widget with new config path
            widget.set_grid_config(new_tmp_path)

            # Check new config was loaded and applied
            assert widget.canvas_widget.grid_num_x == 9
            assert widget.canvas_widget.grid_num_y == 10
            assert widget.canvas_widget.pad_top == 11.0
            assert widget.canvas_widget.pad_bottom == 12.0
            assert widget.canvas_widget.pad_left == 13.0
            assert widget.canvas_widget.pad_right == 14.0
        finally:
            if new_tmp_path.exists():
                os.unlink(new_tmp_path)
    finally:
        if tmp_path.exists():
            os.unlink(tmp_path)
