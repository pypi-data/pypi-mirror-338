import warnings
import numpy as np
import scipy.sparse as scipy_sparse
import scipy.sparse.linalg as scipy_linalg
from fteikpy._interp import vinterp3d
from fteikpy._fteik._ray3d import ray3d
from fteikpy._fteik._fteik3d import fteik3d
from pyeikonal.viz import plot_model3d
from pyeikonal.eikonal.utils import parse_ray3d, jac_interp3d, build_sparse_matrix3d

try:
    import cupy as cp
    import cupyx.scipy.sparse as cupy_sparse
    import cupyx.scipy.sparse.linalg as cupy_linalg

    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False


class Eikonal3D:
    def __init__(
        self,
        model,
        dx=1,
        dy=1,
        dz=1,
    ):
        if not np.issubdtype(model.dtype, np.floating):
            model = model.astype(np.float64)
        self.model = model
        self.nx = model.shape[0]
        self.ny = model.shape[1]
        self.nz = model.shape[2]
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.x_min = 0
        self.y_min = 0
        self.z_min = 0
        self.x_max = self.nx * dx
        self.y_max = self.ny * dy
        self.z_max = self.nz * dz
        self.source = None
        self.tt = None
        self.ttgrad_x = None
        self.ttgrad_y = None
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
            f"* Eikonal3D:\n"
            f"         receiver_num: {receiver_num}\n"
            f"               source: {self.source}\n"
            f"               tt_min: {self.tt_min}\n"
            f"               tt_max: {self.tt_max}\n"
            f"                   dx: {self.dx}\n"
            f"                   dy: {self.dy}\n"
            f"                   dz: {self.dz}\n"
            f"                   nx: {self.nx}\n"
            f"                   ny: {self.ny}\n"
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

    def set_source(self, source=[0, 0, 0]):
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
            receiver = receiver.reshape(1, 3)

        self.receiver = np.asarray(receiver, dtype=np.float64)

    def forward(self, nsweep=2, tt_gradient=False):
        if self.source is None:
            raise ValueError("Source not set")

        xsrc = self.source[0]
        ysrc = self.source[1]
        zsrc = self.source[2]
        dx = self.dx
        dy = self.dy
        dz = self.dz
        slow = 1.0 / np.transpose(self.model, (2, 0, 1))  # from (x, y, z) to (z, x, y)

        tt, ttgrad, vzero = fteik3d(
            slow=slow,
            dz=dz,
            dx=dx,
            dy=dy,
            zsrc=zsrc,
            xsrc=xsrc,
            ysrc=ysrc,
            nsweep=nsweep,
            grad=tt_gradient,
        )

        self.tt = np.transpose(tt, (1, 2, 0))  # from (z, x, y) to (x, y, z)
        self.vzero = vzero
        if tt_gradient:
            self.ttgrad_x = np.transpose(ttgrad[:, :, :, 1], (1, 2, 0))
            self.ttgrad_y = np.transpose(ttgrad[:, :, :, 2], (1, 2, 0))
            self.ttgrad_z = np.transpose(ttgrad[:, :, :, 0], (1, 2, 0))

        self.tt_min = np.nanmin(self.tt)
        self.tt_max = np.nanmax(self.tt)

    def raytrace(self, stepsize=None, max_step=None, honor_grid=True):
        if self.receiver is None:
            raise ValueError("Receiver not set")

        if self.ttgrad_x is None or self.ttgrad_y is None or self.ttgrad_z is None:
            raise ValueError("tt gradient not computed")

        if honor_grid or not stepsize:
            stepsize = np.min([self.dx, self.dy, self.dz])

        if not max_step:
            nx, ny, nz = self.nx, self.ny, self.nz
            dx, dy, dz = self.dx, self.dy, self.dz
            max_dist = 2.0 * ((nx * dx) ** 2 + (ny * dy) ** 2 + (nz * dz) ** 2) ** 0.5
            max_step = int(max_dist / stepsize)

        xaxis = np.asarray(np.arange(self.nx + 1) * self.dx, dtype=np.float64)
        yaxis = np.asarray(np.arange(self.ny + 1) * self.dy, dtype=np.float64)
        zaxis = np.asarray(np.arange(self.nz + 1) * self.dz, dtype=np.float64)
        xgrad = np.transpose(self.ttgrad_x, (2, 0, 1))  #  from (x, y, z) to (z, x, y)
        ygrad = np.transpose(self.ttgrad_y, (2, 0, 1))
        zgrad = np.transpose(self.ttgrad_z, (2, 0, 1))
        p = self.receiver[:, [2, 0, 1]].copy()
        src = [self.source[2], self.source[0], self.source[1]]

        ray_raw = ray3d(
            z=zaxis,
            x=xaxis,
            y=yaxis,
            zgrad=zgrad,
            xgrad=xgrad,
            ygrad=ygrad,
            p=p,
            src=src,
            stepsize=stepsize,
            max_step=max_step,
            honor_grid=honor_grid,
        )

        ray = [arr[:, [1, 2, 0]] for arr in ray_raw]  # from (z, x, y) to (x, y, z)

        return ray

    def calculate_tt(self):
        if self.receiver is None:
            raise ValueError("Receiver not set")

        if self.tt is None:
            raise ValueError("tt not computed")

        xaxis = np.asarray(np.arange(self.nx + 1) * self.dx, dtype=np.float64)
        yaxis = np.asarray(np.arange(self.ny + 1) * self.dy, dtype=np.float64)
        zaxis = np.asarray(np.arange(self.nz + 1) * self.dz, dtype=np.float64)

        # from scipy.interpolate import RegularGridInterpolator
        # interpolator = RegularGridInterpolator(
        #     (xaxis, yaxis, zaxis),
        #     self.tt,
        #     method="linear",
        # )
        # t = interpolator(self.receiver)

        t = vinterp3d(
            x=xaxis,
            y=yaxis,
            z=zaxis,
            v=self.tt,
            q=self.receiver,
            src=self.source,
            vzero=self.vzero,
            fval=np.nan,
        )

        return t

    def calculate_G(self, ray):
        shape = [self.nx, self.ny, self.nz]
        delta = [self.dx, self.dy, self.dz]
        row_indices, col_indices, data = parse_ray3d(ray, shape, delta)

        num_cell = self.nx * self.ny * self.nz
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
        if weight is None:
            weight = np.ones(len(tt_residual), dtype=np.float64)

        dx = self.dx
        dy = self.dy
        dz = self.dz
        nx = self.nx
        ny = self.ny
        nz = self.nz
        s = 1 / self.model.copy()
        tt = self.tt
        source = self.source
        receiver = self.receiver

        # build A matrix and T vector
        rows, cols, data, T = build_sparse_matrix3d(
            tt,
            s,
            source,
            receiver,
            weight,
            tt_residual,
            dx,
            dy,
            dz,
            nx,
            ny,
            nz,
        )

        # solve A * λ = T ---> λ = A^{-1} * T
        if device == "cpu":
            A = scipy_sparse.csr_matrix(
                (data, (rows, cols)), shape=(nx * ny * nz, nx * ny * nz)
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
            A = cupy_sparse.csr_matrix(
                (data, (rows, cols)), shape=(nx * ny * nz, nx * ny * nz)
            ).T
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
        # Jac = Lambda.reshape(nx, ny, nz) * s.reshape(nx, ny, nz)
        Jac = -Lambda.reshape(nx, ny, nz) * s.reshape(nx, ny, nz) ** 3

        # interpolate gradient on source and receiver grid
        Jac = jac_interp3d(Jac, source, receiver, dx, dy, dz)

        return Jac

    def plot(
        self,
        show_source=True,
        show_receiver=True,
        xlim=[None, None],
        ylim=[None, None],
        zlim=[None, None],
        grid=True,
        box_aspect=[1, 1, 0.9],
        fig=None,
        legend=False,
        template="ggplot2",  # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"
        pane_color=None,  # "white",
        width=900,
        height=700,
        show=True,
        save_path=None,
    ):
        if show_source:
            source = self.source.reshape(-1, 3)
        else:
            source = None

        if show_receiver:
            receiver = self.receiver.reshape(-1, 3)
        else:
            receiver = None

        fig = plot_model3d(
            nx=self.nx,
            ny=self.ny,
            nz=self.nz,
            dx=self.dx,
            dy=self.dy,
            dz=self.dz,
            source=source,
            receiver=receiver,
            xlim=xlim,
            ylim=ylim,
            zlim=zlim,
            grid=grid,
            box_aspect=box_aspect,
            fig=fig,
            legend=legend,
            template=template,
            pane_color=pane_color,
            width=width,
            height=height,
            show=False,
        )

        # show
        if show:
            fig.show()

        # save
        if save_path:
            fig.write_html(save_path)
        else:
            return fig
