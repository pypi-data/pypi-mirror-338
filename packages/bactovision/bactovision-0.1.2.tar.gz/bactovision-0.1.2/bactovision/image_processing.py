"""Image processing functions for BactoVision."""

import warnings
from typing import Dict, Tuple

import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw
from scipy.spatial import ConvexHull
from skimage.filters import gaussian, threshold_otsu
from skimage.measure import label
from skimage.morphology import remove_small_objects
from skimage.segmentation import clear_border

__all__ = [
    "segment_by_thresholding",
    "get_summary_metrics",
    "clahe",
    "add_convex_hulls",
    "preprocess_image",
    "normalize_image",
    "default_preprocessing",
]


def segment_by_thresholding(
    image,
    t: float = 1.0,
    s: float = 1,
    convexhull: bool = True,
    small_obj_percent: float = 0.00005,
) -> Tuple[np.ndarray, np.ndarray]:
    """Identifies suitable morphological components from image by thresholding.

    Args:
        image: numpy array of the image.
        t: threshold for thresholding.
        s: size of the morphological component.
        convexhull: whether to add convex hulls to the mask.
        small_obj_percent: percentage of the image area to filter small components.

    Returns:
        Tuple of the original image and the mask.
    """
    # Apply Otsu thresholding
    thresh = t * threshold_otsu(image)

    mask = image > thresh

    # Filter small components. The default threshold is 0.005 % of the image area
    size_thresh = s * np.prod(image.shape) * small_obj_percent

    mask = remove_small_objects(mask, min_size=size_thresh)

    # Clear border
    mask = clear_border(mask)

    # Label connected components
    mask = label(mask)

    if convexhull:
        mask = add_convex_hulls(mask)

    return image, mask


def add_convex_hulls(mask: np.ndarray) -> np.ndarray:
    """Create convex hulls around each connected component in mask.

    Args:
        mask: numpy array of the mask.

    Returns:
        Processed mask.
    """
    labels = np.unique(mask)[1:]

    if not labels.size:
        return mask

    new_mask = np.zeros_like(mask)

    for mask_label in labels:
        region = np.argwhere(mask == mask_label)
        hull = ConvexHull(region)
        verts = [(region[v, 0], region[v, 1]) for v in hull.vertices]
        img = Image.new("L", mask.shape, 0)
        ImageDraw.Draw(img).polygon(verts, outline=1, fill=1)
        new_mask += np.array(img).T * mask_label

    return new_mask


def default_preprocessing(
    img,
    subtract_background: bool = True,
    use_clahe: bool = True,
    clahe_limit: float = 200,
) -> np.ndarray:
    """Preprocess image for thresholding and analysis.

    Args:
        img: numpy array of the image.
        subtract_background: whether to subtract the background.
        use_clahe: whether to use CLAHE.
        clahe_limit: limit for CLAHE.

    Returns:
        Preprocessed image.
    """
    img = normalize_image(np.array(img)) * 255

    if use_clahe:
        img = cv.cvtColor(img.astype(np.uint16), cv.COLOR_BGR2GRAY)
        img = (
            normalize_image(
                cv.createCLAHE(clipLimit=clahe_limit, tileGridSize=(1, 1)).apply(
                    img.astype("uint16")
                )
            )
            * 255
        )
        img = cv.applyColorMap(img.astype(np.uint8), cv.COLORMAP_CIVIDIS)

    img = img.astype(np.float32)

    img = 0.5 * img[:, :, 1] + 1 * img[:, :, 2]

    if subtract_background:
        # Estimate background by gaussian.
        # Scale sigma with image area to compensate for different resolutions
        background = gaussian(img, sigma=np.prod(img.shape) / 10000, truncate=4)
        img -= background  # This may contain some negative values

    # Scale image to [0,1] in invert
    img = 1 - normalize_image(img)

    return img


def preprocess_image(
    img: np.ndarray,
    subtract_background: bool = False,
    use_clahe: bool = False,
    clahe_limit: float = 200,
    channel_weights: tuple = (0, 0.5, 1),
    clahe_first: bool = True,
    **kwargs,
) -> np.ndarray:
    """Prepare image for thresholding and analysis.

    Channels are weighted by (0, 0.5, 1) and summed.
    The background is estimated by gaussian blur and subtracted.
    The image is scaled to [0, 1] and inverted.

    Args:
        img: numpy array of the image.
        subtract_background: whether to subtract the background.
        use_clahe: whether to use CLAHE.
        clahe_limit: limit for CLAHE.
        channel_weights: weights for the channels.
        clahe_first: whether to apply CLAHE first.
        **kwargs: additional arguments for CLAHE.

    Returns:
        Preprocessed image.
    """
    if clahe_first and use_clahe:
        img = normalize_image(img) * 255
        img = cv.cvtColor(img.astype(np.uint16), cv.COLOR_BGR2GRAY)
        img = clahe(img, limit=clahe_limit, **kwargs)
        img = cv.applyColorMap(img.astype(np.uint8), cv.COLORMAP_CIVIDIS).astype(np.float32)

    # Sum weighted channels
    img = np.sum([img[:, :, i] * w for i, w in enumerate(channel_weights)], axis=0)

    # Convert to float and rescale to range [0,1]

    if subtract_background:
        # Estimate background by gaussian.
        # Scale sigma with image area to compensate for different resolutions
        background = gaussian(img, sigma=np.prod(img.shape) / 10000, truncate=4)
        img -= background  # This may contain some negative values

    if use_clahe and not clahe_first:
        img = clahe(normalize_image(img) * 255, limit=clahe_limit, **kwargs).astype(np.float32)

    # Scale image to [0,1] and invert
    img = 1 - normalize_image(img)

    return img


def normalize_image(image: np.ndarray) -> np.ndarray:
    """Normalize image to [0, 1].

    Args:
        image: numpy array of the image.

    Returns:
        Normalized image.
    """
    image = image.astype(np.float32)
    delta = np.max(image) - np.min(image)

    if delta:
        image = (image - np.min(image)) / delta
    else:
        image = np.zeros_like(image)

    return image


def get_summary_metrics(
    image,
    mask,
    grid_x,
    grid_y,
    mode: str = "luminance-inverse",
) -> Dict[str, np.ndarray]:
    """Construct summary metrics.

    Metrics include label, area, mean intensity,
    integral opacity and average opacity for each tile.

    Args:
        image: numpy array of the image.
        mask: numpy array of the mask.
        grid_x: number of tiles in the x direction.
        grid_y: number of tiles in the y direction.
        mode: mode to calculate the brightness, one of
            'luminance', 'luminance-inverse', 'red', 'green', 'blue'.
            Default is 'luminance-inverse' used in the paper.

    Returns:
        A dictionary containing the following keys:
        - 'integral_opacity': numpy array of the integral opacity.
        - 'average_opacity': numpy array of the average opacity.
        - 'relative_area': numpy array of the relative area.
    """
    brightness = img2brightness(image, mode=mode)

    brightness_patches = get_patches(brightness, grid_y, grid_x)
    mask_patches = get_patches(mask, grid_y, grid_x)

    num_pixels = mask_patches.sum(axis=(-1, -2))
    tile_pixes = np.prod(mask_patches.shape[-2:])

    relative_area = num_pixels / tile_pixes

    num_background_pixels = tile_pixes - num_pixels

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        c1 = 1 / num_pixels
        c1[num_pixels == 0] = 1
        c2 = 1 / num_background_pixels
        c2[num_background_pixels == 0] = 1

    average_background_brightness = (brightness_patches * (1 - mask_patches)).sum(
        axis=(-2, -1)
    ) * c2
    integral_opacity = (brightness_patches * mask_patches).sum(
        axis=(-2, -1)
    ) - average_background_brightness * num_pixels
    average_opacity = integral_opacity * c1

    return dict(
        integral_opacity=integral_opacity,
        average_opacity=average_opacity,
        relative_area=relative_area,
        num_pixels=num_pixels,
    )


def img2brightness(img: np.ndarray, mode: str = "luminance") -> np.ndarray:
    if mode == "luminance":
        return img[..., 0] * 0.2989 + img[..., 1] * 0.5870 + img[..., 2] * 0.1140
    elif mode == "sum":
        return img.sum(-1)
    elif mode == "luminance-inverse":
        img = 255 - img
        return img[..., 0] * 0.2989 + img[..., 1] * 0.5870 + img[..., 2] * 0.1140
    else:
        raise ValueError(f"Unknown mode {mode}")


def get_patches(img: np.ndarray, y_grid: int, x_grid: int) -> np.ndarray:
    if img.ndim == 2:
        reduce_channels = True
        img = img[..., None]
    else:
        reduce_channels = False

    ysize, xsize, channels = img.shape
    y_delta = ysize // y_grid
    x_delta = xsize // x_grid

    patches = img[: y_delta * y_grid, : x_delta * x_grid].reshape(
        y_grid, y_delta, x_grid, x_delta, channels
    )
    patches = patches.transpose(0, 2, 1, 3, 4)
    if reduce_channels:
        patches = patches[..., 0]
    return patches


def clahe(img: np.ndarray, limit: float = 200, grid_size: tuple = (1, 1)) -> np.ndarray:
    """Apply Contrast Limited Adaptive Histogram Equalization (CLAHE) to img.

    Args:
        img: numpy array of the image.
        limit: limit for CLAHE.
        grid_size: size of the grid for CLAHE.

    Returns:
        CLAHE-processed image.
    """
    return cv.createCLAHE(clipLimit=limit, tileGridSize=grid_size).apply(img.astype("uint16"))
