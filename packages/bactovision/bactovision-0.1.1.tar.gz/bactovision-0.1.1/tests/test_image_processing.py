"""Tests for the bactovision.image_processing module."""

import numpy as np
import pytest

from bactovision.image_processing import (
    add_convex_hulls,
    clahe,
    get_summary_metrics,
    normalize_image,
    preprocess_image,
    segment_by_thresholding,
)

from .utils import (
    create_test_binary_mask,
    create_test_color_image,
    create_test_grayscale_image,
    create_test_labeled_mask,
)


def test_normalize_image():
    """Test the normalize_image function."""
    # Create a simple test array
    test_array = np.array([[0, 50, 100], [150, 200, 255]], dtype=np.uint8)

    # Normalize the array
    normalized = normalize_image(test_array)

    # Check that the values are between 0 and 1
    assert np.min(normalized) == 0
    assert np.max(normalized) == 1

    # Check that the original values are proportionally maintained
    assert normalized[0, 0] == 0
    assert normalized[1, 2] == 1
    assert normalized[0, 1] == pytest.approx(50 / 255)


def test_normalize_image_constant():
    """Test normalize_image with a constant image."""
    # Create a constant array
    test_array = np.ones((5, 5)) * 100

    # Normalize the array
    normalized = normalize_image(test_array)

    # Check that the result is all zeros (as per the function definition)
    assert np.all(normalized == 0)


def test_segment_by_thresholding():
    """Test the segment_by_thresholding function."""
    # Create a test image
    img = create_test_grayscale_image()

    # Apply thresholding
    _, mask = segment_by_thresholding(img, t=0.8, s=0.5)

    # Check that the mask has some non-zero values
    assert np.max(mask) > 0

    # Check that the mask has the same shape as the input
    assert mask.shape == img.shape


def test_add_convex_hulls():
    """Test the add_convex_hulls function."""
    # Create a simple labeled mask
    mask = create_test_labeled_mask()

    # Apply convex hull
    result = add_convex_hulls(mask)

    # Check the result has the same shape
    assert result.shape == mask.shape

    # Check that the result has values 1 and 2
    assert set(np.unique(result)) == {0, 1, 2}

    # Check that the convex hull filled in some additional pixels
    assert np.sum(result > 0) >= np.sum(mask > 0)


def test_clahe():
    """Test the CLAHE function."""
    # Create a simple test image
    img = np.array([[0, 50], [150, 255]], dtype=np.uint16)

    # Apply CLAHE
    result = clahe(img, limit=100)

    # Check the result has the same shape
    assert result.shape == img.shape

    # Check that the result is a numpy array
    assert isinstance(result, np.ndarray)


def test_preprocess_image():
    """Test the preprocess_image function."""
    # Create a test image
    img = create_test_color_image()

    # Preprocess the image
    processed = preprocess_image(img)

    # Check that the result is a 2D array
    assert processed.ndim == 2

    # Check that the values are between 0 and 1
    assert np.min(processed) >= 0
    assert np.max(processed) <= 1

    # Test with CLAHE
    processed_clahe = preprocess_image(img, use_clahe=True)
    assert processed_clahe.ndim == 2
    assert np.min(processed_clahe) >= 0
    assert np.max(processed_clahe) <= 1


def test_get_summary_metrics():
    """Test the get_summary_metrics function."""
    # Create a test image and mask
    img = create_test_color_image()
    mask = create_test_binary_mask(size=img.shape[:2])

    # Get metrics
    metrics = get_summary_metrics(img, mask, grid_x=2, grid_y=2, mode="luminance")

    # Check that the metrics contain the expected keys
    assert "intergal_opacity" in metrics
    assert "average_opacity" in metrics
    assert "relative_area" in metrics
    assert "num_pixels" in metrics

    # Check the shape of the metrics
    assert metrics["relative_area"].shape == (2, 2)
