import warnings
import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as scipy_sparse
import scipy.sparse.linalg as scipy_linalg
from fteikpy._interp import vinterp2d
from fteikpy._fteik._ray2d import ray2d
from fteikpy._fteik._fteik2d import fteik2d
from pyeikonal.viz import plot_model2d
from pyeikonal.eikonal.utils import parse_ray2d, jac_interp2d, build_sparse_matrix2d

try:
    import cupy as cp
    import cupyx.scipy.sparse as cupy_sparse
    import cupyx.scipy.sparse.linalg as cupy_linalg

    GPU_AVAILABLE = True
except ImportError:
    warnings.warn("CuPy is not installed. GPU acceleration will be disabled.")
    GPU_AVAILABLE = False


class Eikonal2D:
    def __init__(
        self,
        model,
        dx=1,
        dz=1,
    ):
        if not np.issubdtype(model.dtype, np.floating):
            model = model.astype(np.float64)
        self.model = model
        self.nx = model.shape[0]
        self.nz = model.shape[1]
        self.dx = dx
        self.dz = dz
        self.source = None
        self.tt = None
        self.ttgrad_x = None
        self.ttgrad_z = None
        self.receiver = None
        self.vzero = None
        self.tt_min = None
        self.tt_max = None

    def __str__(self):

        if self.receiver is None:
            receiver_num = None
        else:
            receiver_num = len(self.receiver)

        info = (
            f"* Eikonal2D:\n"
            f"         receiver_num: {receiver_num}\n"
            f"               source: {self.source}\n"
            f"               tt_min: {self.tt_min}\n"
            f"               tt_max: {self.tt_max}\n"
            f"                   dx: {self.dx}\n"
            f"                   dz: {self.dz}\n"
            f"                   nx: {self.nx}\n"
            f"                   nz: {self.nz}\n"
        )

        return info

    def __repr__(self):
        return str(self)

    @property
    def receiver_num(self):
        if self.receiver is None:
            return None
        else:
            return len(self.receiver)

    def set_source(self, source=[0, 0]):
        if type(source) == tuple:
            ss = np.array(source)
        elif type(source) == list:
            ss = np.array(source)
        elif type(source) == np.ndarray:
            ss = source
        else:
            raise ValueError("source should be tuple, list or numpy array")

        self.source = np.asarray(ss, dtype=np.float64)

    def set_receiver(self, receiver):
        if receiver.ndim == 1:
            receiver = receiver.reshape(1, 2)

        self.receiver = np.asarray(receiver, dtype=np.float64)

    def forward(self, nsweep=2, tt_gradient=False):
        if self.source is None:
            raise ValueError("Source not set")

        xsrc = self.source[0]
        zsrc = self.source[1]
        dx = self.dx
        dz = self.dz
        slow = 1.0 / self.model.T

        tt, ttgrad, vzero = fteik2d(
            slow=slow,
            dz=dz,
            dx=dx,
            zsrc=zsrc,
            xsrc=xsrc,
            nsweep=nsweep,
            grad=tt_gradient,
        )

        self.tt = tt.T
        self.vzero = vzero
        if tt_gradient:
            self.ttgrad_x = ttgrad[:, :, 1].T
            self.ttgrad_z = ttgrad[:, :, 0].T

        self.tt_min = np.nanmin(self.tt)
        self.tt_max = np.nanmax(self.tt)

    def raytrace(self, stepsize=None, max_step=None, honor_grid=True):
        if self.receiver is None:
            raise ValueError("Receiver not set")

        if self.ttgrad_x is None or self.ttgrad_z is None:
            raise ValueError("tt gradient not computed")

        if honor_grid or not stepsize:
            stepsize = np.min([self.dx, self.dz])

        if not max_step:
            nz, nx = self.nz, self.nx
            dz, dx = self.dz, self.dx
            max_dist = 2.0 * ((nz * dz) ** 2 + (nx * dx) ** 2) ** 0.5
            max_step = int(max_dist / stepsize)

        xaxis = np.asarray(np.arange(self.nx + 1) * self.dx, dtype=np.float64)
        zaxis = np.asarray(np.arange(self.nz + 1) * self.dz, dtype=np.float64)
        xgrad = self.ttgrad_x.T
        zgrad = self.ttgrad_z.T
        p = self.receiver[:, [1, 0]].copy()
        src = [self.source[1], self.source[0]]

        ray_raw = ray2d(
            z=zaxis,
            x=xaxis,
            zgrad=zgrad,
            xgrad=xgrad,
            p=p,
            src=src,
            stepsize=stepsize,
            max_step=max_step,
            honor_grid=honor_grid,
        )

        ray = [arr[:, [1, 0]] for arr in ray_raw]

        return ray

    def calculate_tt(self):
        if self.receiver is None:
            raise ValueError("receiver not set")

        if self.tt is None:
            raise ValueError("tt not computed")

        xaxis = np.asarray(np.arange(self.nx + 1) * self.dx, dtype=np.float64)
        zaxis = np.asarray(np.arange(self.nz + 1) * self.dz, dtype=np.float64)

        # from scipy.interpolate import RegularGridInterpolator
        # interpolator = RegularGridInterpolator(
        #     (xaxis, zaxis),
        #     self.tt,
        #     method="linear",
        # )
        # t = interpolator(self.receiver)

        t = vinterp2d(
            x=xaxis,
            y=zaxis,
            v=self.tt,
            q=self.receiver,
            src=self.source,
            vzero=self.vzero,
            fval=np.nan,
        )

        return t

    def calculate_G(self, ray):
        shape = [self.nx, self.nz]
        delta = [self.dx, self.dz]
        row_indices, col_indices, data = parse_ray2d(ray, shape, delta)

        num_cell = self.nx * self.nz
        num_ray = len(ray)
        G = scipy_sparse.csr_matrix(
            (data, (row_indices, col_indices)), shape=(num_ray, num_cell)
        )

        return G

    def adjoint(
        self,
        tt_residual,
        weight=None,
        method="lu",
        device="cpu",
        **kwargs,
    ):
        """objective function J = 1/2 * ∑(Gm - d_obs)^2, m = 1/v, m is the slowness, v is the velocity
        ∂J/∂m = λ * (1/v), where λ is the Lagrange multiplier
        ∂J/∂v = -λ * (1/v^3)

        Args:
            tt_residual (_type_): d_syn - d_obs
            weight (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if weight is None:
            weight = np.ones(len(tt_residual), dtype=np.float64)

        dx = self.dx
        dz = self.dz
        nx = self.nx
        nz = self.nz
        s = 1 / self.model.copy()
        tt = self.tt
        source = self.source
        receiver = self.receiver

        # build A matrix and T_residual vector
        rows, cols, data, T = build_sparse_matrix2d(
            tt,
            s,
            source,
            receiver,
            weight,
            tt_residual,
            dx,
            dz,
            nx,
            nz,
        )

        # solve A * λ = T ---> λ = A^{-1} * T
        if device == "cpu":
            A = scipy_sparse.csr_matrix(
                (data, (rows, cols)), shape=(nx * nz, nx * nz)
            ).T
            if method == "lu":
                Lambda = scipy_linalg.spsolve(A, T, **kwargs)
            elif method == "gmres":
                Lambda, info = scipy_linalg.gmres(A, T, **kwargs)
                if info != 0:
                    warnings.warn(f"GMRES did not converge, info: {info}", UserWarning)
            elif method == "gmres_ilu":
                ilu = scipy_linalg.spilu(A)
                M = scipy_linalg.LinearOperator(A.shape, ilu.solve)
                Lambda, info = scipy_linalg.gmres(A, T, M=M, **kwargs)
                if info != 0:
                    warnings.warn(f"GMRES did not converge, info: {info}", UserWarning)
            else:
                raise ValueError("method should be 'lu' or 'gmres' or 'gmres_ilu'")

        elif device == "cuda":
            data = cp.array(data)
            rows = cp.array(rows)
            cols = cp.array(cols)
            T = cp.asarray(T)
            A = cupy_sparse.csr_matrix((data, (rows, cols)), shape=(nx * nz, nx * nz)).T
            if method == "lu":
                Lambda = cupy_linalg.spsolve(A, T, **kwargs)
            elif method == "gmres":
                Lambda, info = cupy_linalg.gmres(A, T, **kwargs)
                if info != 0:
                    warnings.warn(f"GMRES did not converge, info: {info}", UserWarning)
            elif method == "gmres_ilu":
                ilu = cupy_linalg.spilu(A)
                M = cupy_linalg.LinearOperator(A.shape, ilu.solve)
                Lambda, info = cupy_linalg.gmres(A, T, M=M, **kwargs)
                if info != 0:
                    warnings.warn(f"GMRES did not converge, info: {info}", UserWarning)
            else:
                raise ValueError("method should be 'lu' or 'gmres' or 'gmres_ilu'")

            Lambda = cp.asnumpy(Lambda)
        else:
            raise ValueError("device should be 'cpu' or 'cuda'")

        # compute gradient ∂J/∂m = λ * (1/v), ∂J/∂v = -λ * (1/v^3), where m = 1/v and v is the velocity
        # Jac = Lambda.reshape(nx, nz) * s.reshape(nx, nz)
        Jac = -Lambda.reshape(nx, nz) * s.reshape(nx, nz) ** 3

        # interpolate gradient on source and receiver grid
        Jac = jac_interp2d(Jac, source, receiver, dx, dz)

        return Jac

    def plot(
        self,
        show_model=True,
        mask=None,
        colorbar=True,
        cmap="jet_r",
        alpha=1,
        show_contour=False,
        contour_levels=None,
        contour_colors="black",
        contour_alpha=0.5,
        contour_linewidths=0.2,
        contour_linestyles="-",
        show_source=True,
        source_marker="*",
        source_color="red",
        source_alpha=1,
        source_size=50,
        show_receiver=True,
        receiver_marker="^",
        receiver_color="deepskyblue",
        receiver_alpha=1,
        receiver_size=30,
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
        if show_model:
            model = self.model
        else:
            model = None

        if show_contour:
            tt = self.tt
        else:
            tt = None

        if show_source:
            source = self.source.reshape(-1, 2)
        else:
            source = None

        if show_receiver:
            receiver = self.receiver.reshape(-1, 2)
        else:
            receiver = None

        ax = plot_model2d(
            nx=self.nx,
            nz=self.nz,
            dx=self.dx,
            dz=self.dz,
            model=model,
            mask=mask,
            colorbar=colorbar,
            cmap=cmap,
            alpha=alpha,
            tt=tt,
            contour_levels=contour_levels,
            contour_colors=contour_colors,
            contour_alpha=contour_alpha,
            contour_linewidths=contour_linewidths,
            contour_linestyles=contour_linestyles,
            source=source,
            source_marker=source_marker,
            source_color=source_color,
            source_alpha=source_alpha,
            source_size=source_size,
            receiver=receiver,
            receiver_marker=receiver_marker,
            receiver_color=receiver_color,
            receiver_alpha=receiver_alpha,
            receiver_size=receiver_size,
            invert_x=invert_x,
            invert_y=invert_y,
            xlim=xlim,
            ylim=ylim,
            clip=clip,
            ax=ax,
            figsize=figsize,
            show=False,
        )

        if show:
            plt.show()

        fig = ax.figure
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
        else:
            return ax
