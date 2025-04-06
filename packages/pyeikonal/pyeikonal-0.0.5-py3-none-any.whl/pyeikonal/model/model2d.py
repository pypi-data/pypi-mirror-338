import copy
import pickle
import numpy as np
import matplotlib.pyplot as plt
from pyeikonal.viz import plot_model2d, plot_ray2d
from pyeikonal.model.rbf import plot_rbf2d
from pyeikonal.model.utils import forward2d
from pyeikonal.utils.utils import smooth2d


class BaseModel2D:
    def __init__(
        self,
        dx,
        dz,
        nx,
        nz,
        m,
        m_ref=None,
        grad_flag=False,
        mask=None,
        smooth_size=None,
        regularization_flag=False,
        smooth_factor=1.0,
        tikhonov_order=0,
    ):
        self.type = "Model2D"
        self.dx = dx
        self.dz = dz
        self.nx = nx
        self.nz = nz
        self.x = np.arange(nx) * dx
        self.z = np.arange(nz) * dz
        self.m = m.flatten()

        # tikhonov regularization
        self.regularization_flag = regularization_flag
        self.smooth_factor = smooth_factor
        self.tikhonov_order = tikhonov_order
        if m_ref is None:
            self.m_ref = np.zeros(nx * nz)
        else:
            self.m_ref = m_ref.flatten()
        if regularization_flag:
            self.matL = np.array([])
            self.add_regularization()

        # grad processing
        self.grad_flag = grad_flag
        self.smooth_size = smooth_size
        self.mask = mask

        # misfit and gradient
        self.misfit = None
        self.grad = None

    def __str__(self):
        if self.mask is not None:
            mask = "Yes"
        else:
            mask = "No"

        info = (
            f"* Base2D\n"
            f"             grad_flag: {self.grad_flag}\n"
            f"                  mask: {mask}\n"
            f"           smooth_size: {self.smooth_size}\n"
            f"   regularization_flag: {self.regularization_flag}\n"
            f"         smooth_factor: {self.smooth_factor}\n"
            f"        tikhonov_order: {self.tikhonov_order}\n"
            f"                    dx: {self.dx}\n"
            f"                    dz: {self.dz}\n"
            f"                    nx: {self.nx}\n"
            f"                    nz: {self.nz}\n"
        )
        return info

    def __repr__(self):
        return str(self)

    def copy(self):
        return copy.deepcopy(self)

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    def to_bmodel(self, m):
        return m

    def add_regularization(self):
        nx = self.nx
        nz = self.nz
        tikhonov_order = self.tikhonov_order

        if tikhonov_order == 0:
            self.matL = np.eye(nx * nz)
        elif tikhonov_order == 1:
            self.matL = np.zeros(((nx - 1) * (nz - 1), nx * nz))
            k = 0
            for i in range(nx - 1):
                for j in range(nz - 1):
                    M = np.zeros((nx, nz))
                    M[i, j] = -0.5
                    M[i, j + 1] = 0.25
                    M[i + 1, j] = 0.25
                    self.matL[k, :] = M.flatten()
                    k += 1
        elif tikhonov_order == 2:
            self.matL = np.zeros(((nx - 2) * (nz - 2), nx * nz))
            k = 0
            for i in range(1, nx - 1):
                for j in range(1, nz - 1):
                    M = np.zeros((nx, nz))
                    M[i, j] = -0.5
                    M[i, j + 1] = 0.125
                    M[i, j - 1] = 0.125
                    M[i + 1, j] = 0.125
                    M[i - 1, j] = 0.125
                    self.matL[k, :] = M.flatten()
                    k += 1
        else:
            raise ValueError("'tikhonov_order' must be 0, 1, or 2")

    def process_grad(self, grad):
        # grad mask
        if self.mask is not None:
            grad = grad * self.mask

        # grad smooth
        if self.smooth_size is not None:
            size_x, size_z = self.smooth_size
            grad = grad.reshape(self.nx, self.nz)
            grad = smooth2d(grad, size_x, size_z).flatten()

        return grad

    def calculate(self):
        # model residual
        dm = self.to_bmodel(self.m) - self.to_bmodel(self.m_ref)

        # misfit and gradient
        m_num = self.nx * self.nz
        L = self.matL
        res = L @ dm
        misfit = 1 / 2 * self.smooth_factor / m_num * np.sum(res**2)
        grad = self.smooth_factor / m_num * (L.T @ res)

        # grad mask
        if self.mask is not None:
            grad = grad * self.mask

        # grad smooth??
        if self.smooth_size is not None:
            size_x, size_z = self.smooth_size
            grad = grad.reshape(self.nx, self.nz)
            grad = smooth2d(grad, size_x, size_z).flatten()

        # update information
        self.misfit = misfit
        self.grad = grad

    def forward(
        self,
        source,
        receiver,
        nsweep=2,
        raytrace=True,
        stepsize=None,
        max_step=None,
        honor_grid=True,
        cache_path="./cache_tt",
        jobs=1,
    ):
        m = self.m
        m = self.to_bmodel(m).reshape(self.nx, self.nz)
        source = np.array(source).reshape(-1, 2)
        receiver = np.array(receiver).reshape(-1, 2)

        return forward2d(
            m,
            self.dx,
            self.dz,
            source,
            receiver,
            nsweep=nsweep,
            raytrace=raytrace,
            stepsize=stepsize,
            max_step=max_step,
            honor_grid=honor_grid,
            cache_path=cache_path,
            jobs=jobs,
        )

    def plot(
        self,
        source=None,
        receiver=None,
        ray=None,
        show_model=True,
        show_mask=False,
        colorbar=True,
        cmap="jet_r",
        alpha=1,
        source_marker="*",
        source_color="red",
        source_alpha=1,
        source_size=50,
        receiver_marker="^",
        receiver_color="deepskyblue",
        receiver_alpha=1,
        receiver_size=30,
        ray_color="black",
        ray_alpha=1,
        ray_linewidth=0.6,
        ray_linestyle="-",
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
        dx = self.dx
        dz = self.dz
        nx = self.nx
        nz = self.nz

        if show_model:
            m = self.to_bmodel(self.m).reshape(nx, nz)
        else:
            m = None

        if show_mask and self.mask is not None:
            mask = self.mask.reshape(nx, nz)
        else:
            mask = None

        if source is not None:
            source = np.array(source).reshape(-1, 2)

        if receiver is not None:
            receiver = np.array(receiver).reshape(-1, 2)

        ax = plot_model2d(
            nx=nx,
            nz=nz,
            dx=dx,
            dz=dz,
            model=m,
            mask=mask,
            colorbar=colorbar,
            cmap=cmap,
            alpha=alpha,
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

        if ray is not None:
            ray = [item for r in ray for item in r]
            ax = plot_ray2d(
                ray=ray,
                color=ray_color,
                alpha=ray_alpha,
                linewidth=ray_linewidth,
                linestyle=ray_linestyle,
                xlim=xlim,
                ylim=ylim,
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


class GridModel2D(BaseModel2D):
    def __init__(
        self,
        dx,
        dz,
        nx,
        nz,
        m,
        m_ref=None,
        mask=None,
        smooth_size=None,
        regularization_flag=False,
        smooth_factor=1.0,
        tikhonov_order=0,
    ):
        self.type = "Model2D"
        self.dx = dx
        self.dz = dz
        self.nx = nx
        self.nz = nz
        self.x = np.arange(nx) * dx
        self.z = np.arange(nz) * dz
        self.m = m.flatten()

        # tikhonov regularization
        self.regularization_flag = regularization_flag
        self.smooth_factor = smooth_factor
        self.tikhonov_order = tikhonov_order
        if m_ref is None:
            self.m_ref = np.zeros(nx * nz)
        else:
            self.m_ref = m_ref.flatten()

        # grad processing
        self.smooth_size = smooth_size
        self.mask = mask

        # misfit and gradient
        self.misfit = None
        self.grad = None

        # inherit from parent class
        super().__init__(
            dx,
            dz,
            nx,
            nz,
            m,
            m_ref=m_ref,
            grad_flag=True,
            mask=mask,
            smooth_size=smooth_size,
            regularization_flag=regularization_flag,
            smooth_factor=smooth_factor,
            tikhonov_order=tikhonov_order,
        )

    def __str__(self):
        if self.mask is not None:
            mask = "Yes"
        else:
            mask = "No"

        info = (
            f"* Model2D\n"
            f"   regularization_flag: {self.regularization_flag}\n"
            f"         smooth_factor: {self.smooth_factor}\n"
            f"        tikhonov_order: {self.tikhonov_order}\n"
            f"                  mask: {mask}\n"
            f"           smooth_size: {self.smooth_size}\n"
            f"                    dx: {self.dx}\n"
            f"                    dz: {self.dz}\n"
            f"                    nx: {self.nx}\n"
            f"                    nz: {self.nz}\n"
        )
        return info


class RBFModel2D(BaseModel2D):
    def __init__(
        self,
        dx,
        dz,
        nx,
        nz,
        m,
        m_bl,
        centers,
        sigma,
        mask=None,
        smooth_size=None,
    ):
        self.type = "ModelRBF2D"
        self.dx = dx
        self.dz = dz
        self.nx = nx
        self.nz = nz
        self.x = np.arange(nx) * dx
        self.z = np.arange(nz) * dz
        self.m = m.flatten()  # np.zeros(centers.shape[0])
        self.m_bl = m_bl.flatten()
        self.centers = centers
        self.sigma = sigma
        self.rbf_num = centers.shape[0]

        # rbf model; r: distance between the grid and the RBF centers
        Z, X = np.meshgrid(self.z, self.x)
        grid = np.vstack((X.flatten(), Z.flatten())).T
        r = np.linalg.norm(grid[:, np.newaxis, :] - centers[np.newaxis, :, :], axis=2)
        self.jacobian = np.exp(-((r / sigma) ** 2))

        # grad processing
        self.smooth_size = smooth_size
        self.mask = mask

        # misfit and gradient
        self.misfit = None
        self.grad = None

        # inherit from parent class
        super().__init__(
            dx,
            dz,
            nx,
            nz,
            m,
            m_ref=None,
            grad_flag=True,
            mask=mask,
            smooth_size=smooth_size,
            regularization_flag=False,
        )

    def __str__(self):
        if self.mask is not None:
            mask = "Yes"
        else:
            mask = "No"

        info = (
            f"* ModelRBF2D\n"
            f"               rbf_num: {self.rbf_num}\n"
            f"                  mask: {mask}\n"
            f"           smooth_size: {self.smooth_size}\n"
            f"                    dx: {self.dx}\n"
            f"                    dz: {self.dz}\n"
            f"                    nx: {self.nx}\n"
            f"                    nz: {self.nz}\n"
        )
        return info

    def to_bmodel(self, m):
        # m_bl + m_rbf
        return self.m_bl + np.matmul(self.jacobian, m)

    def process_grad(self, grad):
        # grad mask
        if self.mask is not None:
            grad = grad * self.mask

        # grad smooth
        if self.smooth_size is not None:
            size_x, size_z = self.smooth_size
            grad = grad.reshape(self.nx, self.nz)
            grad = smooth2d(grad, size_x, size_z).flatten()

        grad = np.matmul(self.jacobian.T, grad)

        return grad

    def plot_rbf(
        self,
        prior=None,
        show_mask=False,
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
        figsize=(10, 4),
        show=True,
        save_path=None,
        dpi=100,
    ):
        nx = self.nx
        nz = self.nz
        dx = self.dx
        dz = self.dz
        centers = self.centers.copy()

        if show_mask:
            mask = self.mask.reshape(nx, nz)
        else:
            mask = None

        ax = plot_rbf2d(
            nx=nx,
            nz=nz,
            dx=dx,
            dz=dz,
            prior=prior,
            centers=centers,
            mask=mask,
            colorbar=colorbar,
            cmap=cmap,
            alpha=alpha,
            color=color,
            marker=marker,
            marker_size=marker_size,
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


class FixedShapeModel2D:
    def __init__(self, dx, dz, nx, nz, mask=None, smooth_size=None):
        self.dx = dx
        self.dz = dz
        self.nx = nx
        self.nz = nz
        self.x = np.arange(nx) * dx
        self.z = np.arange(nz) * dz
        self.centers = None
        self.sigma = None
        self.jacobian = None

        # grad processing
        self.smooth_size = smooth_size
        if mask is None:
            self.mask = np.ones(nx * nz)
        else:
            self.mask = mask.flatten()

        # model, misfit, and gradient
        self._grad = None
        self._model = None
        self._misfit = None

    def use_shapefixed_model(self, shapes, model):
        self.model_mode = "shapefixed"
        self.shapefixed_shapes = shapes
        self.shapefixed_model = model
