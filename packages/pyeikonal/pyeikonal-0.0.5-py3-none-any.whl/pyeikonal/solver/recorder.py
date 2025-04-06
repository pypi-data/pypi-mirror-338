import time
import copy
import scipy
import pickle
import numpy as np


def load_recorder(filename):
    with open(filename, "rb") as f:
        recorder = pickle.load(f)
    return recorder


class SciPyCallbackRecorder:
    def __init__(self, problem, options=None, show=True):
        self.iter = 0
        self.info = {
            "m": [],
            "misfit": [],
            "misfit_data": [],
            "misfit_model": [],
            "gradient": [],
            "gradient_data": [],
            "gradient_model": [],
        }
        self.problem = problem
        self.options = options
        self.show = show
        self.__starttime = None
        self.__endtime = None
        self.runtime = None

    def __call__(self, intermediate_result):
        # start time
        if self.iter == 0:
            self.__starttime = time.time()

        # check input
        if type(intermediate_result) == scipy.optimize.OptimizeResult:
            m = intermediate_result.x.copy()
        else:
            m = intermediate_result.copy()

        # calculate
        ngrad = self.problem.ngrad
        grad, misfit = self.calculate(m)

        # print message
        if self.show:
            if self.iter == 0:
                print("******************************************************")
                print("                   SciPy Optimizer                     ")
                print("******************************************************")
                if "maxiter" in self.options:
                    print(f"\tmaxiter: {self.options['maxiter']}")
                if "ftol" in self.options:
                    print(f"\tftol: {self.options['ftol']}")
                if "gtol" in self.options:
                    print(f"\tgtol: {self.options['gtol']}")
                if "c1" in self.options:
                    print(f"\tc1: {self.options['c1']}")
                if "c2" in self.options:
                    print(f"\tc2: {self.options['c2']}")
                print("******************************************************\n")
                print(f"   {'Niter':<12}{'obj_value':<15}{'ngrad':<13}{'max_grad':<15}")

            index = np.argmax(np.abs(grad))
            max_grad = grad[index]
            print(f"     {self.iter:<9}{misfit:<18.6e}{ngrad:<9}{max_grad:<18.6e}")

        self.iter += 1
        self.__endtime = time.time()
        self.runtime = self.__endtime - self.__starttime

    def __str__(self):
        info = (
            f"* SciPyCallbackRecorder\n"
            f"           runtime: {self.runtime} seconds\n"
            f"              iter: {self.iter}\n"
            f"           options: {self.options}\n"
            f"              info: check more keys in {self.info.keys()}\n"
        )

        return info

    def __repr__(self):
        return str(self)

    def calculate(self, m):
        # misfit
        misfit_data = self.problem.current_data_misfit

        # gradient
        grad_data = self.problem.current_data_grad

        # regularization
        model = self.problem.model
        if model.regularization_flag:
            misfit_model = self.problem.current_model_misfit
            grad_model = self.problem.current_model_grad
            misfit = misfit_data + misfit_model
            grad = grad_data + grad_model
        else:
            misfit = misfit_data
            grad = grad_data

        # save info
        self.info["m"].append(m.copy())
        self.info["misfit"].append(misfit)
        self.info["misfit_data"].append(misfit_data)

        if model.grad_flag:
            self.info["gradient"].append(grad)
            self.info["gradient_data"].append(grad_data)

        if model.regularization_flag:
            self.info["misfit_model"].append(misfit_model)
            self.info["gradient_model"].append(grad_model)

        return grad, misfit

    def copy(self):
        return copy.deepcopy(self)

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
