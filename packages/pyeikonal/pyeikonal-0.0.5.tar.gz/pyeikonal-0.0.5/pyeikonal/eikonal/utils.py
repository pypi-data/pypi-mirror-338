import pickle
import numpy as np
from numba import njit


def load_eikonal(filename):
    with open(filename, "rb") as f:
        eikonal = pickle.load(f)
    return eikonal


# **********************************************************
#                           2D
# **********************************************************
@njit
def parse_ray2d(ray, shape, delta):
    num_ray = len(ray)

    max_segment = 0
    for i in range(num_ray):
        max_segment = max(max_segment, len(ray[i]))

    row_indices = np.zeros(num_ray * max_segment, dtype=np.int32)
    col_indices = np.zeros(num_ray * max_segment, dtype=np.int32)
    data = np.zeros(num_ray * max_segment, dtype=np.float64)

    idx = 0
    for i in range(num_ray):
        for j in range(len(ray[i]) - 1):
            x0, z0 = ray[i][j]
            x1, z1 = ray[i][j + 1]

            ix = int((x0 + x1) / delta[0] / 2)
            iz = int((z0 + z1) / delta[1] / 2)

            segment_length = np.sqrt((x1 - x0) ** 2 + (z1 - z0) ** 2)

            cell_index = ix * shape[1] + iz
            row_indices[idx] = i
            col_indices[idx] = cell_index
            data[idx] = segment_length
            idx += 1

    return row_indices[:idx], col_indices[:idx], data[:idx]


@njit
def get_id2d(i, j, nz):
    return i * nz + j


@njit
def bilinear_interp2d(jac, x0, z0, dx, dz, nx, nz):
    """
    Perform bilinear interpolation for a given point (x0, z0) based on grid data `jac`.

    Parameters:
    - jac: 2D numpy array, representing the gradient values at the grid points.
    - x0, z0: The coordinates of the point where interpolation is needed.
    - dx, dz: Grid spacing in the x and z directions.

    Returns:
    - jac_interp: The interpolated value at (x0, z0).
    """

    # Determine the indices of the lower-left grid point (i0, j0)
    i0 = int(x0 // dx)
    j0 = int(z0 // dz)

    # Ensure the indices do not exceed the grid boundaries
    i0 = max(0, min(i0, nx - 2))
    j0 = max(0, min(j0, nz - 2))

    # Compute the normalized position within the grid cell (range: 0 to 1)
    tx = (x0 - i0 * dx) / dx  # weight in the x direction
    tz = (z0 - j0 * dz) / dz  # weight in the z direction

    # Retrieve the gradient values at the four surrounding grid points
    J00 = jac[i0, j0]
    J10 = jac[i0 + 1, j0]
    J01 = jac[i0, j0 + 1]
    J11 = jac[i0 + 1, j0 + 1]

    # Compute the bilinear interpolation
    # bilinear_value = (
    #     J00 * (1 - tx) * (1 - tz)
    #     + J10 * tx * (1 - tz)
    #     + J01 * (1 - tx) * tz
    #     + J11 * tx * tz
    # )
    mean_value = (J00 + J10 + J01 + J11) / 4
    jac[i0, j0] = mean_value
    jac[i0 + 1, j0] = mean_value
    jac[i0, j0 + 1] = mean_value
    jac[i0 + 1, j0 + 1] = mean_value


@njit
def jac_interp2d(jac, source, receiver, dx, dz):
    jac = jac.copy()
    nx, nz = jac.shape

    # source
    x0, z0 = source
    bilinear_interp2d(jac, x0, z0, dx, dz, nx, nz)

    # # receiver
    # for i in range(len(receiver)):
    #     x, z = receiver[i]
    #     bilinear_interp2d(jac, x, z, dx, dz, nx, nz)

    return jac


@njit
def build_sparse_matrix2d(tt, s, source, receiver, weight, tt_residual, dx, dz, nx, nz):
    # build T_residual vector
    T_residual = np.zeros(nx * nz, dtype=np.float64)
    for i in range(len(receiver)):
        x, z = receiver[i]
        ix = int(x / dx)
        iz = int(z / dz)
        cell_index = ix * nz + iz
        T_residual[cell_index] = tt_residual[i] * weight[i]

    # source index
    ix0 = max(0, min(int(source[0] / dx), nx - 1))
    jx0 = max(0, min(int(source[1] / dz), nz - 1))
    ix1 = min(nx - 1, ix0 + 1)
    jx1 = min(nz - 1, jx0 + 1)

    # build A matrix
    max_elements = nx * nz * 4
    rows = np.zeros(max_elements, dtype=np.int32)
    cols = np.zeros(max_elements, dtype=np.int32)
    data = np.zeros(max_elements, dtype=np.float64)
    count = 0
    dx2 = dx * dx
    dz2 = dz * dz

    for i in range(nx):
        for j in range(nz):
            this_id = get_id2d(i, j, nz)
            this_id_is_not_zero = False

            if (
                i == ix0
                and j == jx0
                or (i == ix0 and j == jx1)
                or (i == ix1 and j == jx0)
                or (i == ix1 and j == jx1)
            ):
                rows[count] = this_id
                cols[count] = this_id
                data[count] = 1.0
                # s[i, j] = 0.0
                count += 1
                continue

            if i == 0:
                idx = get_id2d(i + 1, j, nz)
                tt_xmin = tt[i + 1, j]
            elif i == nx - 1:
                idx = get_id2d(i - 1, j, nz)
                tt_xmin = tt[i - 1, j]
            else:
                if tt[i + 1, j] > tt[i - 1, j]:
                    idx = get_id2d(i - 1, j, nz)
                    tt_xmin = tt[i - 1, j]
                else:
                    idx = get_id2d(i + 1, j, nz)
                    tt_xmin = tt[i + 1, j]

            if j == 0:
                idz = get_id2d(i, j + 1, nz)
                tt_zmin = tt[i, j + 1]
            elif j == nz - 1:
                idz = get_id2d(i, j - 1, nz)
                tt_zmin = tt[i, j - 1]
            else:
                if tt[i, j + 1] > tt[i, j - 1]:
                    idz = get_id2d(i, j - 1, nz)
                    tt_zmin = tt[i, j - 1]
                else:
                    idz = get_id2d(i, j + 1, nz)
                    tt_zmin = tt[i, j + 1]

            if tt[i, j] > tt_xmin:
                this_id_is_not_zero = True
                value = (tt[i, j] - tt_xmin) / dx2
                rows[count] = this_id
                cols[count] = this_id
                data[count] = value
                count += 1

                rows[count] = this_id
                cols[count] = idx
                data[count] = -value
                count += 1

            if tt[i, j] > tt_zmin:
                this_id_is_not_zero = True
                value = (tt[i, j] - tt_zmin) / dz2
                rows[count] = this_id
                cols[count] = this_id
                data[count] = value
                count += 1

                rows[count] = this_id
                cols[count] = idz
                data[count] = -value
                count += 1

            if not this_id_is_not_zero:
                rows[count] = this_id
                cols[count] = this_id
                data[count] = 1.0
                s[i, j] = 0.0
                count += 1

    return rows[:count], cols[:count], data[:count], T_residual


# **********************************************************
#                           3D
# **********************************************************
@njit
def parse_ray3d(ray, shape, delta):
    num_ray = len(ray)

    max_segment = 0
    for i in range(num_ray):
        max_segment = max(max_segment, len(ray[i]))

    row_indices = np.zeros(num_ray * max_segment, dtype=np.int32)
    col_indices = np.zeros(num_ray * max_segment, dtype=np.int32)
    data = np.zeros(num_ray * max_segment, dtype=np.float64)

    idx = 0
    for i in range(num_ray):
        for j in range(len(ray[i]) - 1):
            x0, y0, z0 = ray[i][j]
            x1, y1, z1 = ray[i][j + 1]

            ix = int((x0 + x1) / delta[0] / 2)
            iy = int((y0 + y1) / delta[1] / 2)
            iz = int((z0 + z1) / delta[2] / 2)

            segment_length = np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2)

            cell_index = ix * shape[1] * shape[2] + iy * shape[2] + iz
            row_indices[idx] = i
            col_indices[idx] = cell_index
            data[idx] = segment_length
            idx += 1

    return row_indices[:idx], col_indices[:idx], data[:idx]


@njit
def get_id3d(i, j, k, ny, nz):
    return i * ny * nz + j * nz + k


@njit
def trilinear_interp3d(jac, x0, y0, z0, dx, dy, dz, nx, ny, nz):
    """
    Perform trilinear interpolation for a given point (x0, y0, z0) based on grid data `jac`.

    Parameters:
    - jac: 3D numpy array, representing the gradient values at the grid points.
    - x0, y0, z0: The coordinates of the point where interpolation is needed.
    - dx, dy, dz: Grid spacing in the x, y, and z directions.
    - nx, ny, nz: Dimensions of the 3D grid.

    Returns:
    - jac_interp: The interpolated value at (x0, y0, z0).
    """

    # Determine the indices of the nearest lower-left-front grid point (i0, j0, k0)
    i0 = int(x0 // dx)
    j0 = int(y0 // dy)
    k0 = int(z0 // dz)

    # Ensure indices are within valid bounds (avoiding out-of-bounds errors)
    i0 = max(0, min(i0, nx - 2))
    j0 = max(0, min(j0, ny - 2))
    k0 = max(0, min(k0, nz - 2))

    # Compute the normalized position within the grid cell (range: 0 to 1)
    tx = (x0 - i0 * dx) / dx  # weight in x direction
    ty = (y0 - j0 * dy) / dy  # weight in y direction
    tz = (z0 - k0 * dz) / dz  # weight in z direction

    # Retrieve the values at the eight surrounding grid points
    J000 = jac[i0, j0, k0]  # (i0, j0, k0) - lower-left-front
    J100 = jac[i0 + 1, j0, k0]  # (i0+1, j0, k0) - lower-right-front
    J010 = jac[i0, j0 + 1, k0]  # (i0, j0+1, k0) - upper-left-front
    J110 = jac[i0 + 1, j0 + 1, k0]  # (i0+1, j0+1, k0) - upper-right-front
    J001 = jac[i0, j0, k0 + 1]  # (i0, j0, k0+1) - lower-left-back
    J101 = jac[i0 + 1, j0, k0 + 1]  # (i0+1, j0, k0+1) - lower-right-back
    J011 = jac[i0, j0 + 1, k0 + 1]  # (i0, j0+1, k0+1) - upper-left-back
    J111 = jac[i0 + 1, j0 + 1, k0 + 1]  # (i0+1, j0+1, k0+1) - upper-right-back

    # Compute trilinear interpolation
    # trilinear_value = (
    #     J000 * (1 - tx) * (1 - ty) * (1 - tz)
    #     + J100 * tx * (1 - ty) * (1 - tz)
    #     + J010 * (1 - tx) * ty * (1 - tz)
    #     + J110 * tx * ty * (1 - tz)
    #     + J001 * (1 - tx) * (1 - ty) * tz
    #     + J101 * tx * (1 - ty) * tz
    #     + J011 * (1 - tx) * ty * tz
    #     + J111 * tx * ty * tz
    # )
    mean_value = (J000 + J100 + J010 + J110 + J001 + J101 + J011 + J111) / 8
    jac[i0, j0, k0] = mean_value
    jac[i0 + 1, j0, k0] = mean_value
    jac[i0, j0 + 1, k0] = mean_value
    jac[i0 + 1, j0 + 1, k0] = mean_value
    jac[i0, j0, k0 + 1] = mean_value
    jac[i0 + 1, j0, k0 + 1] = mean_value
    jac[i0, j0 + 1, k0 + 1] = mean_value
    jac[i0 + 1, j0 + 1, k0 + 1] = mean_value


@njit
def jac_interp3d(jac, source, receiver, dx, dy, dz):
    jac = jac.copy()
    nx, ny, nz = jac.shape

    # source
    x0, y0, z0 = source
    trilinear_interp3d(jac, x0, y0, z0, dx, dy, dz, nx, ny, nz)

    # # receiver
    # for i in range(len(receiver)):
    #     x, y, z = receiver[i]
    #     trilinear_interp3d(jac, x, y, z, dx, dy, dz, nx, ny, nz)

    return jac


@njit
def build_sparse_matrix3d(
    tt, s, source, receiver, weight, tt_residual, dx, dy, dz, nx, ny, nz
):
    # build T_residual vector
    T_residual = np.zeros(nx * ny * nz, dtype=np.float64)
    for i in range(len(receiver)):
        x, y, z = receiver[i]
        ix = int(x / dx)
        iy = int(y / dy)
        iz = int(z / dz)
        cell_index = ix * ny * nz + iy * nz + iz
        T_residual[cell_index] = tt_residual[i] * weight[i]

    # source index
    ix0 = max(0, min(int(source[0] / dx), nx - 1))
    jx0 = max(0, min(int(source[1] / dy), ny - 1))
    kx0 = max(0, min(int(source[2] / dz), nz - 1))
    ix1 = min(nx - 1, ix0 + 1)
    jx1 = min(ny - 1, jx0 + 1)
    kx1 = min(nz - 1, kx0 + 1)

    # build A matrix
    max_elements = nx * nz * nz * 6
    rows = np.zeros(max_elements, dtype=np.int32)
    cols = np.zeros(max_elements, dtype=np.int32)
    data = np.zeros(max_elements, dtype=np.float64)
    count = 0
    dx2 = dx * dx
    dy2 = dy * dy
    dz2 = dz * dz

    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                this_id = get_id3d(i, j, k, ny, nz)
                this_id_is_not_zero = False

                if (
                    i == ix0
                    and j == jx0
                    and k == kx0
                    or (i == ix0 and j == jx0 and k == kx1)
                    or (i == ix0 and j == jx1 and k == kx0)
                    or (i == ix0 and j == jx1 and k == kx1)
                    or (i == ix1 and j == jx0 and k == kx0)
                    or (i == ix1 and j == jx0 and k == kx1)
                    or (i == ix1 and j == jx1 and k == kx0)
                    or (i == ix1 and j == jx1 and k == kx1)
                ):
                    rows[count] = this_id
                    cols[count] = this_id
                    data[count] = 1.0
                    # s[i, j, k] = 0.0
                    count += 1
                    continue

                if i == 0:
                    idx = get_id3d(i + 1, j, k, ny, nz)
                    tt_xmin = tt[i + 1, j, k]
                elif i == nx - 1:
                    idx = get_id3d(i - 1, j, k, ny, nz)
                    tt_xmin = tt[i - 1, j, k]
                else:
                    if tt[i + 1, j, k] > tt[i - 1, j, k]:
                        idx = get_id3d(i - 1, j, k, ny, nz)
                        tt_xmin = tt[i - 1, j, k]
                    else:
                        idx = get_id3d(i + 1, j, k, ny, nz)
                        tt_xmin = tt[i + 1, j, k]

                if j == 0:
                    idy = get_id3d(i, j + 1, k, ny, nz)
                    tt_ymin = tt[i, j + 1, k]
                elif j == ny - 1:
                    idy = get_id3d(i, j - 1, k, ny, nz)
                    tt_ymin = tt[i, j - 1, k]
                else:
                    if tt[i, j + 1, k] > tt[i, j - 1, k]:
                        idy = get_id3d(i, j - 1, k, ny, nz)
                        tt_ymin = tt[i, j - 1, k]
                    else:
                        idy = get_id3d(i, j + 1, k, ny, nz)
                        tt_ymin = tt[i, j + 1, k]

                if k == 0:
                    idz = get_id3d(i, j, k + 1, ny, nz)
                    tt_zmin = tt[i, j, k + 1]
                elif k == nz - 1:
                    idz = get_id3d(i, j, k - 1, ny, nz)
                    tt_zmin = tt[i, j, k - 1]
                else:
                    if tt[i, j, k + 1] > tt[i, j, k - 1]:
                        idz = get_id3d(i, j, k - 1, ny, nz)
                        tt_zmin = tt[i, j, k - 1]
                    else:
                        idz = get_id3d(i, j, k + 1, ny, nz)
                        tt_zmin = tt[i, j, k + 1]

                if tt[i, j, k] > tt_xmin:
                    this_id_is_not_zero = True
                    value = (tt[i, j, k] - tt_xmin) / dx2
                    rows[count] = this_id
                    cols[count] = this_id
                    data[count] = value
                    count += 1

                    rows[count] = this_id
                    cols[count] = idx
                    data[count] = -value
                    count += 1

                if tt[i, j, k] > tt_ymin:
                    this_id_is_not_zero = True
                    value = (tt[i, j, k] - tt_ymin) / dy2
                    rows[count] = this_id
                    cols[count] = this_id
                    data[count] = value
                    count += 1

                    rows[count] = this_id
                    cols[count] = idy
                    data[count] = -value
                    count += 1

                if tt[i, j, k] > tt_zmin:
                    this_id_is_not_zero = True
                    value = (tt[i, j, k] - tt_zmin) / dz2
                    rows[count] = this_id
                    cols[count] = this_id
                    data[count] = value
                    count += 1

                    rows[count] = this_id
                    cols[count] = idz
                    data[count] = -value
                    count += 1

                if not this_id_is_not_zero:
                    rows[count] = this_id
                    cols[count] = this_id
                    data[count] = 1.0
                    s[i, j, k] = 0.0
                    count += 1

    return rows[:count], cols[:count], data[:count], T_residual
