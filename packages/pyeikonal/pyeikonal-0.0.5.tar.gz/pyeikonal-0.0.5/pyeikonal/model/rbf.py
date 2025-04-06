import warnings
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator
from pyeikonal.viz.plot import _get_ax


try:
    import pygmsh

    HAS_PYGMSH = True
except ImportError:
    warnings.warn(
        "pygmsh is not installed. The `gmsh_center2d` function will not be available."
    )
    HAS_PYGMSH = False


def gmsh_center2d(
    density: np.ndarray, mesh_min: float, mesh_max: float, dx: float, dz: float
):
    """Compute the center given the density distribution using gmsh in 2D

    Parameters
    ----------
    density: np.ndarray (nx, nz)
        density distribution
    mesh_min: float
        Minimum value of the mesh
    mesh_max: float
        Maximum value of the mesh
    dx: float
        Grid interval of the density distribution in x-direction
    dz: float
        Grid interval of the density distribution in z-direction

    Returns
    -------
    points: np.ndarray (npoints, 2)
        Coordinates of the mesh points
    mesh_sizes: np.ndarray (nx, nz)
        Mesh sizes of the mesh points
    """

    # get the shape of the density distribution
    if density.ndim != 2:
        raise ValueError("density must be 2D")

    nx, nz = density.shape

    # get the coordinates of the density distribution
    x = np.arange(nx) * dx
    z = np.arange(nz) * dz

    # Normalize density distribution to be in range [0, 1]
    density = (density - np.min(density)) / (np.max(density) - np.min(density))

    # Scale and shift density to be in range [mesh_min, mesh_max]
    mesh_sizes = mesh_max + (mesh_min - mesh_max) * density

    # create the interpolator
    interp = RegularGridInterpolator(
        (x, z),
        mesh_sizes,
        method="nearest",
        bounds_error=False,
        fill_value=(mesh_min + mesh_max) / 2.0,
    )

    # define the callback function for gmsh to get the mesh size
    def get_mesh_size(x, y):

        return interp((x, y)).item()

    # create the geometry and generate the mesh using gmsh
    with pygmsh.geo.Geometry() as geom:
        geom.add_polygon([[x[0], z[0]], [x[-1], z[0]], [x[-1], z[-1]], [x[0], z[-1]]])
        geom.set_mesh_size_callback(lambda dim, tag, x, y, z, lc: get_mesh_size(x, y))
        mesh = geom.generate_mesh()

    points = mesh.points[:, :2]

    return points, mesh_sizes


def set_sigma2d(points, sigma_ratio):
    """Set the sigma of the RBF."""

    # Expanding the points array to compute the pairwise differences
    diffs = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    # Computing the square distances
    dist_squared = np.sum(diffs**2, axis=2)
    # Setting the diagonal (distances to itself) to a large number to avoid zero minimum
    np.fill_diagonal(dist_squared, np.inf)
    # Finding the minimum distances
    min_distances = np.sqrt(np.min(dist_squared, axis=1))

    return min_distances * sigma_ratio


def plot_rbf2d(
    nx,
    nz,
    dx,
    dz,
    prior=None,
    centers=None,
    mask=None,
    colorbar=True,
    cmap="jet",
    alpha=1,
    color="red",
    marker=".",
    marker_size=5,
    invert_x=False,
    invert_y=False,
    xlim=[None, None],
    ylim=[None, None],
    clip=[None, None],
    ax=None,
    figsize=(10, 5),
    show=True,
    save_path=None,
    dpi=100,
):
    ax = _get_ax(ax, figsize=figsize)

    xmin = 0
    xmax = nx * dx
    zmin = 0
    zmax = nz * dz

    ax = _get_ax(ax, figsize=figsize)

    if prior is not None:
        if mask is not None:
            prior = np.ma.masked_where(mask == 0, prior)
        im = ax.imshow(
            prior.T,
            extent=[xmin, xmax, zmax, zmin],
            cmap=cmap,
        )
        if clip[0] is not None and clip[1] is not None:
            im.set_clim(clip[0], clip[1])
        if colorbar:
            plt.colorbar(im, orientation="vertical", ax=ax, label="Density")

    if mask is not None:
        for i in range(len(centers)):
            x, z = centers[i]
            if mask[int(x / dx), int(z / dz)] == 0:
                centers[i] = np.nan, np.nan

    ax.scatter(
        centers[:, 0],
        centers[:, 1],
        marker=marker,
        color=color,
        s=marker_size,
        alpha=alpha,
    )

    if xlim[0] is None and xlim[1] is None:
        xlim = [xmin, xmax]
    if ylim[0] is None and ylim[1] is None:
        ylim = [zmax, zmin]
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Z (m)")

    if invert_x:
        ax.invert_xaxis()

    if invert_y:
        ax.invert_yaxis()

    if show:
        plt.show()

    fig = ax.figure
    if save_path is not None:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    else:
        return ax
