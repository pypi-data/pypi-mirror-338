import numpy as np
from allmetrics.utils import ImageTranslationDataValidator
from typing import Union, Optional
import torch
import warnings
from scipy.signal import fftconvolve

validator = ImageTranslationDataValidator()

list_of_metrics = ['psnr', 'ssim']


def psnr(
    image_true: Union[np.ndarray, torch.Tensor],
    image_test: Union[np.ndarray, torch.Tensor],
    data_range: Optional[float] = None,
    validator: Optional[ImageTranslationDataValidator] = None,
    **validator_kwargs
) -> float:
    """
    Compute the Peak Signal to Noise Ratio (PSNR) - Compatible with skimage.metrics.peak_signal_noise_ratio

    Parameters
    ----------
    image_true : ndarray or Tensor
        Ground-truth image
    image_test : ndarray or Tensor
        Test image
    data_range : float, optional
        The data range of the input image (max possible value)
    validator : ImageTranslationValidator, optional
        Validator instance
    **validator_kwargs : dict
        Additional validator arguments

    Returns
    -------
    psnr : float
        The PSNR metric in dB
    """
    # 1. Initialize validator if not provided
    if validator is None:
        validator = ImageTranslationDataValidator(raise_warning=False)

    # 2. Convert to numpy arrays
    image_true = validator._ensure_numpy(image_true)
    image_test = validator._ensure_numpy(image_test)

    # 3. Validate shapes
    if image_true.shape != image_test.shape:
        raise ValueError(f"Input images must have the same dimensions. Got {image_true.shape} and {image_test.shape}")

    # 4. Determine data range
    if data_range is None:
        if image_true.dtype != image_test.dtype:
            warnings.warn("Inputs have mismatched dtype. Setting data_range based on image_true.")

        if image_true.dtype == np.uint8:
            data_range = 255
        elif image_true.dtype == np.uint16:
            data_range = 65535
        elif image_true.dtype in (np.float32, np.float64):
            data_range = 1.0
        else:
            raise ValueError(f"Unsupported dtype: {image_true.dtype}")

    # 5. Validate data range
    true_min, true_max = np.min(image_true), np.max(image_true)
    if true_max > data_range or true_min < 0:
        raise ValueError(
            f"Image values must be in range [0, {data_range}]. Got range [{true_min}, {true_max}]"
        )

    # 6. Compute MSE
    mse = np.mean((image_true - image_test) ** 2)

    # 7. Handle special case
    if mse == 0:
        return float('inf')

    # 8. Compute PSNR
    return 10 * np.log10((data_range ** 2) / mse)


def _create_gaussian_window(size: int, sigma: float) -> np.ndarray:
    """Create a Gaussian window with proper normalization"""
    ax = np.arange(-size // 2 + 1, size // 2 + 1)
    xx, yy = np.meshgrid(ax, ax)
    window = np.exp(-(xx**2 + yy**2) / (2.0 * sigma**2))
    return window / window.sum()

def _compute_ssim(img1: np.ndarray, img2: np.ndarray, window: np.ndarray, dynamic_range: float) -> float:
    """Compute SSIM for single-channel images"""
    C1 = (0.01 * dynamic_range)**2
    C2 = (0.03 * dynamic_range)**2

    # Compute local means
    mu1 = fftconvolve(img1, window, mode='same')
    mu2 = fftconvolve(img2, window, mode='same')

    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2

    # Compute variance and covariance
    sigma1_sq = fftconvolve(img1**2, window, mode='same') - mu1_sq
    sigma2_sq = fftconvolve(img2**2, window, mode='same') - mu2_sq
    sigma12 = fftconvolve(img1 * img2, window, mode='same') - mu1_mu2

    # Prevent negative values
    sigma1_sq = np.maximum(0, sigma1_sq)
    sigma2_sq = np.maximum(0, sigma2_sq)

    # Final SSIM computation
    numerator = (2 * mu1_mu2 + C1) * (2 * sigma12 + C2)
    denominator = (mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2)
    ssim_map = numerator / denominator

    return np.mean(ssim_map)

def ssim(
    img1: np.ndarray,
    img2: np.ndarray,
    window_size: int = 11,
    dynamic_range: float = 255.0,
    multichannel: bool = False
) -> float:
    # Convert to float32
    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)

    # Create Gaussian window
    window = _create_gaussian_window(window_size, 1.5)

    # Compute for color or grayscale images
    if not multichannel or img1.ndim == 2:
        return _compute_ssim(img1, img2, window, dynamic_range)
    else:
        channel_scores = []
        for c in range(img1.shape[-1]):
            channel_scores.append(_compute_ssim(img1[..., c], img2[..., c], window, dynamic_range))
        return np.mean(channel_scores)