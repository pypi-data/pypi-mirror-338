import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from joblib import Parallel, delayed
from pathlib import Path
from traceback import print_exc
from contextlib import redirect_stdout, redirect_stderr
from func_timeout import func_timeout, FunctionTimedOut
from scipy.optimize import minimize
from pyeikonal.viz import plot_lcurve
from pyeikonal.solver import SciPyCallbackRecorder


class LCurveInv:
    def __init__(
        self,
        problem,
        smooth_factors,
        tikhonov_order,
        options=None,
        bounds=None,
    ):
        # check
        if not problem.model.regularization_flag:
            raise ValueError("The model must have regularization enabled.")
        self.problem = problem
        self.smooth_factors = smooth_factors
        self.tikhonov_order = tikhonov_order
        self.options = options
        self.bounds = bounds
        self.success_rate = None

    def __str__(self):
        n_factor = len(self.smooth_factors)

        if self.bounds is None:
            bounds_str = "None"
        else:
            bounds_str = "too long to show"

        info = (
            "* RandomInv\n",
            f"         n_factor: {n_factor}\n",
            f"   tikhonov_order: {self.tikhonov_order}\n",
            f"          options: {self.options}\n",
            f"     success_rate: {self.success_rate}\n",
            f"           bounds: {bounds_str}\n",
        )
        return "".join(info)

    def __repr__(self):
        return str(self)

    def plot(
        self,
        log=True,
        grid=True,
        ax=None,
        figsize=(12, 6),
        show=True,
        save_path=None,
        dpi=100,
    ):
        ax = plot_lcurve(
            self.misfit_data,
            self.misfit_model,
            self.misfit_factors,
            log=log,
            grid=grid,
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

    def job(self, smooth_factor, i, cache_path, log_file_path):
        prob = self.problem.copy()
        prob.ngrad = 0
        prob.model.smooth_factor = smooth_factor
        prob.cache_path = cache_path / f".cache_inv_{i}"
        prob.cache_reset()

        m0 = prob.model.m
        recorder = SciPyCallbackRecorder(prob, self.options, show=True)
        with open(log_file_path, "w") as log_file:
            with redirect_stdout(log_file), redirect_stderr(log_file):
                recorder(m0)
                results = minimize(
                    fun=prob.obj_func,
                    x0=m0,
                    jac=prob.grad_func,
                    method="L-BFGS-B",
                    bounds=self.bounds,
                    options=self.options,
                    callback=recorder,
                )
                print(f"\nRuntime: {recorder.runtime} seconds\n\n----\n{results}\n")
                return recorder

    def process(self, i, smooth_factor, cache_path, timeout):
        log_file_path = cache_path / f"inv_{i}.log"
        data_file_path = cache_path / f"data_{i}.npy"

        try:
            if timeout is None:
                recorder = self.job(smooth_factor, i, cache_path, log_file_path)
            else:
                recorder = func_timeout(
                    timeout,
                    self.job,
                    args=(smooth_factor, i, cache_path, log_file_path),
                )
            misfit_data = recorder.info["misfit_data"][-1]
            misfit_model = recorder.info["misfit_model"][-1]
            arr = np.array([misfit_data, misfit_model, smooth_factor], dtype=np.float64)
            np.save(data_file_path, arr)

        except FunctionTimedOut:
            with open(log_file_path, "a") as log_file:
                log_file.write(
                    f"The job function timed out after {timeout}s and was terminated:\n"
                )
                print_exc(file=log_file)
            arr = np.array([-1, -1, smooth_factor], dtype=np.float64)
            np.save(data_file_path, arr)

        except Exception:
            with open(log_file_path, "a") as log_file:
                log_file.write(f"An error occurred:\n")
                print_exc(file=log_file)
            arr = np.array([-1, -1, smooth_factor], dtype=np.float64)
            np.save(data_file_path, arr)

    def run(self, jobs=1, flag=True, cache_path="./.cache_lcurve", timeout=None):
        cache_path = Path(cache_path)
        cache_path.mkdir(parents=True, exist_ok=True)

        # job
        n_factor = len(self.smooth_factors)
        if flag:
            pbar = tqdm(range(0, n_factor), desc=f"Calculate via {jobs} jobs")
        else:
            pbar = range(0, n_factor)
        if jobs == 1:
            for i in pbar:
                self.process(
                    i,
                    self.smooth_factors[i],
                    cache_path,
                    timeout,
                )

        else:
            Parallel(n_jobs=jobs, backend="loky")(
                delayed(self.process)(
                    i,
                    self.smooth_factors[i],
                    cache_path,
                    timeout,
                )
                for i in pbar
            )

        # read cache
        results = np.zeros((n_factor, 3), dtype=np.float64)
        for i in range(n_factor):
            data_file_path = cache_path / f"data_{i}.npy"
            arr = np.load(data_file_path)
            misfit_data = arr[0]
            misfit_model = arr[1]
            smooth_factor = arr[2]
            results[i] = [misfit_data, misfit_model, smooth_factor]

        count = 0
        misfit_data = []
        misfit_model = []
        misfit_factors = []
        for i in range(len(results)):
            if results[i, 0] != -1.0 and results[i, 1] != -1.0:
                m_data = results[i, 0]
                m_model = results[i, 1]
                smooth_factor = results[i, 2]
                misfit_factors.append(smooth_factor)
                misfit_data.append(m_data)
                misfit_model.append(m_model / smooth_factor)
            else:
                count += 1

        self.misfit_data = misfit_data
        self.misfit_model = misfit_model
        self.misfit_factors = misfit_factors
        self.success_rate = (n_factor - count) / n_factor

        if flag:
            pbar.close()

        return (
            self.misfit_data,
            self.misfit_model,
            self.misfit_factors,
            self.success_rate,
        )
