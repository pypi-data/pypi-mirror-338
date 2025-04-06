#!/usr/bin/env python3

"""Image metrics."""

import numbers

import torch

from .utils import batched_frames
from .vmaf import vmaf


__all__ = ["psnr", "ssim", "vmaf"]


@batched_frames
def psnr(ref: torch.Tensor, dis: torch.Tensor, *args, **kwargs) -> torch.Tensor:
    """Compute the peak signal to noise ratio of 2 images.

    Parameters
    ----------
    ref, dis : arraylike
        The 2 images to be compared, of shape ([*batch], height, width, channels).
        Supported types are float32 and float64.
    weights : iterable[float], optional
        The relative weight of each channel. By default, all channels have the same weight.
    threads : int, optional
        Defines the number of threads.
        The value -1 means that the function uses as many calculation threads as there are cores.
        The default value (0) allows the same behavior as (-1) if the function
        is called in the main thread, otherwise (1) to avoid nested threads.
        Any other positive value corresponds to the number of threads used.

    Returns
    -------
    psnr : arraylike
        The global peak signal to noise ratio,
        as a ponderation of the mean square error of each channel.
        It is batched and clamped in [0, 100] db.

    Notes
    -----
    * It is optimized for C contiguous tensors.
    * If device is cpu and gradient is not required, a fast C code is used instead of torch code.

    Examples
    --------
    >>> import numpy as np
    >>> from cutcutcodec.core.analysis.video.metric import psnr
    >>> np.random.seed(0)
    >>> ref = np.random.random((720, 1080, 3))  # It could also be a torch array list...
    >>> dis = 0.8 * ref + 0.2 * np.random.random((720, 1080, 3))
    >>> psnr(ref, dis).round(1)
    np.float64(21.8)
    >>>
    """
    if (
        ref.requires_grad or dis.requires_grad
        or ref.device.type != "cpu" or dis.device.type != "cpu"
    ):
        from .psnr_torch import psnr_torch  # pylint: disable=C0415
        return psnr_torch(ref, dis, *args, **kwargs)
    from .metric import psnr as psnr_c  # pylint: disable=C0415
    return torch.asarray(
        [psnr_c(r, d, *args, **kwargs) for r, d in zip(ref.numpy(), dis.numpy())],
        dtype=ref.dtype,
    )


@batched_frames
def ssim(ref: torch.Tensor, dis: torch.Tensor, *args, stride: int = 1, **kwargs) -> torch.Tensor:
    """Compute the Structural similarity index measure of 2 images.

    Parameters
    ----------
    ref, dis : arraylike
        The 2 images to be compared, of shape ([*batch], height, width, channels).
        Supported types are float32 and float64.
    data_range : float, default=1.0
        The data range of the input image (difference between maximum and minimum possible values).
    weights : iterable[float], optional
        The relative weight of each channel. By default, all channels have the same weight.
    sigma : float, default=1.5
        The standard deviation of the gaussian. It has to be strictely positive.
    stride : int, default=1
        The stride of the convolving kernel.
    threads : int, optional
        Defines the number of threads.
        The value -1 means that the function uses as many calculation threads as there are cores.
        The default value (0) allows the same behavior as (-1) if the function
        is called in the main thread, otherwise (1) to avoid nested threads.
        Any other positive value corresponds to the number of threads used.

    Returns
    -------
    ssim : arraylike
        The ponderated structural similarity index measure of each layers.

    Notes
    -----
    * It is optimized for C contiguous tensors.
    * If device is cpu, gradient is not required and stride != 1, a fast C code is used.

    Examples
    --------
    >>> import numpy as np
    >>> from cutcutcodec.core.analysis.video.metric import ssim
    >>> np.random.seed(0)
    >>> ref = np.random.random((720, 1080, 3))  # It could also be a torch array list...
    >>> dis = 0.8 * ref + 0.2 * np.random.random((720, 1080, 3))
    >>> ssim(ref, dis).round(2)
    np.float64(0.95)
    >>>
    """
    assert isinstance(stride, numbers.Integral), stride.__class__.__name__
    if stride == 1:
        from .ssim_torch import ssim_fft_torch  # pylint: disable=C0415
        return ssim_fft_torch(ref, dis, *args, **kwargs)
    if (
        ref.requires_grad or dis.requires_grad
        or ref.device.type != "cpu" or dis.device.type != "cpu"
    ):
        from .ssim_torch import ssim_conv_torch  # pylint: disable=C0415
        return ssim_conv_torch(ref, dis, *args, stride=stride, **kwargs)
    from .metric import ssim as ssim_c  # pylint: disable=C0415
    return torch.asarray(
        [ssim_c(r, d, *args, stride=stride, **kwargs) for r, d in zip(ref.numpy(), dis.numpy())],
        dtype=ref.dtype,
    )
