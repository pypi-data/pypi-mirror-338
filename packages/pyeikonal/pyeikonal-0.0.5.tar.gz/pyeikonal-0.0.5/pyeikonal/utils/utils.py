import numpy as np
from scipy.ndimage import gaussian_filter


def smooth2d(data, span_x, span_z):
    """Smooths values 2D rectangular grid"""

    return gaussian_filter(data, sigma=(span_x, span_z))


def generate_checkerboard2d(nx, nz, dx, dz, scale_x, scale_z, amplitude):
    """
    Generate a checkerboard pattern for full-waveform inversion.

    Parameters:
    nx (int): Number of grid points in the x-direction.
    nz (int): Number of grid points in the z-direction.
    dx (float): Grid spacing in the x-direction.
    dz (float): Grid spacing in the z-direction.
    scale_x (float): Scale (period) of the checkerboard in the x-direction.
    scale_z (float): Scale (period) of the checkerboard in the z-direction.
    amplitude (float): Amplitude of the anomaly.

    Returns:
    checkerboard (2D array): Generated checkerboard anomaly model.
    """

    x = np.arange(0, nx * dx, dx)
    z = np.arange(0, nz * dz, dz)
    X, Z = np.meshgrid(x, z)

    checkerboard = (
        amplitude * np.sin(2 * np.pi * X / scale_x) * np.sin(2 * np.pi * Z / scale_z)
    )

    return checkerboard


def generate_ellipse_anomaly2d(
    nx,
    nz,
    dx,
    dz,
    center_x,
    center_z,
    sigma_x,
    sigma_z,
    amplitude,
    theta=0.0,
    half=True,
):
    """
    Generate a rotated elliptical Gaussian velocity anomaly (supports dx, dz; v shape = (nx, nz))

    Parameters:
        v        : Background velocity model (2D numpy array), shape = (nx, nz)
        dx, dz    : Spatial sampling intervals in x and z directions (in meters)
        center_x  : Center x-coordinate of the anomaly (in meters)
        center_z  : Center z-coordinate of the anomaly (in meters)
        sigma_x   : Standard deviation along the x-axis (in meters)
        sigma_z   : Standard deviation along the z-axis (in meters)
        amplitude : Amplitude of the anomaly (same unit as v, e.g., m/s)
        theta     : Rotation angle of the ellipse (in degrees, counterclockwise)
        half      : If True, only keep the anomaly below the center_z
    """

    anomaly_v = np.zeros((nx, nz), dtype=np.float64)

    # compute center indices and standard deviations in grid units
    cx = center_x / dx
    cz = center_z / dz
    sx = sigma_x / dx
    sz = sigma_z / dz
    theta_rad = np.deg2rad(theta)

    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)

    for ix in range(nx):
        for iz in range(nz):
            x = ix - cx
            z = iz - cz

            # rotate coordinates
            x_rot = x * cos_t + z * sin_t
            z_rot = -x * sin_t + z * cos_t

            distance = (x_rot / sx) ** 2 + (z_rot / sz) ** 2
            anomaly_v[ix, iz] = amplitude * np.exp(-distance)

    if half:
        cz_idx = int(cz)
        anomaly_v[:, :cz_idx] = 0.0

    return anomaly_v
