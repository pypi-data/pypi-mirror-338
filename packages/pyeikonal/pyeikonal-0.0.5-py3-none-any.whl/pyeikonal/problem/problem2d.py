import copy
import pickle
import shutil
import warnings
import numpy as np
from pathlib import Path
from pyeikonal.problem.utils import run2d


class Problem2D:
    def __init__(self, model):
        self.source = []
        self.receiver = []
        self.tt = []
        self.weight = []
        self.model = model
        self.dx = model.dx
        self.dz = model.dz
        self.nx = model.nx
        self.nz = model.nz
        self.current_m = None
        self.current_data_misfit = None
        self.current_data_grad = None
        self.current_model_misfit = None
        self.current_model_grad = None
        self.ngrad = 0

        # config
        self.config()

    def __str__(self):
        info = (
            f"* Problem2D\n"
            f"            source_num: {self.source_num}\n"
            f"                    dx: {self.dx}\n"
            f"                    dz: {self.dz}\n"
            f"                    nx: {self.nx}\n"
            f"                    nz: {self.nz}\n"
            f"\n"
            f"* Config\n"
            f"                nsweep: {self.nsweep}\n"
            f"                method: {self.method}\n"
            f"        adjoint_method: {self.adjoint_method}\n"
            f"        adjoint_device: {self.adjoint_device}\n"
            f"          forward_jobs: {self.forward_jobs}\n"
        )
        return info

    def __repr__(self):
        return str(self)

    @property
    def source_num(self):
        return len(self.source)

    def copy(self):
        return copy.deepcopy(self)

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    def cache_reset(self):
        path = self.cache_path
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

    def config(
        self,
        nsweep=2,
        method="adjoint",  # "adjoint" or "raytrace"
        adjoint_method="lu",
        adjoint_device="cpu",
        forward_jobs=1,
        cache_path="./.cache_inv",
    ):
        self.nsweep = nsweep
        self.method = method
        self.adjoint_method = adjoint_method
        self.adjoint_device = adjoint_device
        self.forward_jobs = forward_jobs
        self.cache_path = Path(cache_path)
        self.cache_reset()

    def add_data(self, source, receiver, tt, weight=None):
        self.source.append(source)
        self.receiver.append(receiver)
        self.tt.append(tt)
        if weight is None:
            weight = np.ones(len(tt))
        self.weight.append(weight)

    def calculate_data(self, m):
        self.model.m = m
        misfit, grad = run2d(
            self.model,
            self.source,
            self.receiver,
            self.tt,
            self.weight,
            self.nsweep,
            self.method,
            self.adjoint_method,
            self.adjoint_device,
            self.forward_jobs,
            self.cache_path,
        )

        # save
        self.current_m = m
        self.current_data_misfit = misfit
        self.current_data_grad = grad

    def calculate_model(self, m):
        if self.model.regularization_flag:
            self.model.m = m
            self.model.calculate()
            self.current_model_misfit = self.model.misfit
            self.current_model_grad = self.model.grad

    def obj_func(self, m):
        # data
        self.calculate_data(m)
        misfit = self.current_data_misfit

        # model
        if self.model.regularization_flag:
            self.calculate_model(m)
            misfit += self.current_model_misfit

        return misfit

    def grad_func(self, m):
        self.ngrad += 1

        # data
        if np.array_equal(m, self.current_m):
            grad = self.current_data_grad
        else:
            self.calculate_data(m)
            grad = self.current_data_grad
            warnings.warn(
                "m is not equal to self.current_m, self.calculate_data/self.calculate_model is called"
            )

        # model
        if self.model.regularization_flag:
            if np.array_equal(m, self.current_m):
                grad += self.current_model_grad
            else:
                self.calculate_model(m)
                grad += self.current_model_grad

        return grad
