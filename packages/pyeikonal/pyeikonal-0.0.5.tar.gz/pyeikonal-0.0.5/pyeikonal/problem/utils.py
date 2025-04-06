import pickle
import numpy as np
from joblib import Parallel, delayed
from pyeikonal.eikonal import Eikonal2D


def load_problem(filename):
    with open(filename, "rb") as f:
        prob = pickle.load(f)
    return prob


def _eikonal2d(
    source_index,
    source,
    receiver,
    tt,
    weight,
    m,
    dx,
    dz,
    grad_flag,
    nsweep,
    method,
    adjoint_method,
    adjoint_device,
    cache_path=None,
):
    if method == "adjoint":
        tt_gradient = False
    elif method == "raytrace":
        tt_gradient = True

    # forward
    eik = Eikonal2D(m, dx, dz)
    eik.set_source(source)
    eik.set_receiver(receiver)
    eik.forward(nsweep=nsweep, tt_gradient=tt_gradient)
    tt_forward = eik.calculate_tt()

    # misfit
    n = len(tt)
    res = tt_forward - tt
    misfit = 1 / 2 * np.sum(weight * res**2) / n

    # gradient
    if grad_flag:
        wres = weight * res
        if method == "adjoint":
            jac = eik.adjoint(
                wres, method=adjoint_method, device=adjoint_device
            ).flatten()
            jac = jac / n
        elif method == "raytrace":
            ray = eik.raytrace()
            G = eik.calculate_G(ray)
            ds_dm = -(1 / m.flatten() ** 2)
            jac = (G.T @ wres) * ds_dm
            jac = jac / n
        else:
            raise ValueError("method must be 'adjoint' or 'raytrace'")
    else:
        jac = np.array([0])

    # save cache
    cache_file = cache_path / f"eikonal_{source_index}.npz"
    np.savez(cache_file, misfit=misfit, jac=jac)


def run2d(
    model,
    source,
    receiver,
    tt,
    weight,
    nsweep,
    method,
    adjoint_method,
    adjoint_device,
    forward_jobs,
    cache_path,
):
    # init paras
    dx = model.dx
    dz = model.dz
    nx = model.nx
    nz = model.nz
    m = model.to_bmodel(model.m).reshape(nx, nz)
    grad_flag = model.grad_flag

    # calculate
    misfit = 0
    grad = np.zeros(nx * nz)
    source_num = len(source)
    if forward_jobs == 1:
        for i in range(source_num):
            _eikonal2d(
                i,
                source[i],
                receiver[i],
                tt[i],
                weight[i],
                m,
                dx,
                dz,
                grad_flag,
                nsweep,
                method,
                adjoint_method,
                adjoint_device,
                cache_path=cache_path,
            )

    elif forward_jobs > 1:
        Parallel(n_jobs=forward_jobs, backend="loky")(
            delayed(_eikonal2d)(
                i,
                source[i],
                receiver[i],
                tt[i],
                weight[i],
                m,
                dx,
                dz,
                grad_flag,
                nsweep,
                method,
                adjoint_method,
                adjoint_device,
                cache_path=cache_path,
            )
            for i in range(source_num)
        )

    # read cache
    for i in range(source_num):
        cache_file = cache_path / f"eikonal_{i}.npz"
        data = np.load(cache_file)
        misfit += data["misfit"].item()
        if grad_flag:
            grad += data["jac"]

    # grad processing
    if grad_flag:
        grad = model.process_grad(grad)

    # return
    misfit /= source_num
    grad /= source_num

    return misfit, grad
