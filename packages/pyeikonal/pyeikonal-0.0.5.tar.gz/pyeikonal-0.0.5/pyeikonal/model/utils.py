import pickle
import shutil
import numpy as np
from pathlib import Path
from joblib import Parallel, delayed
from pyeikonal.eikonal import Eikonal2D


def load_model(filename):
    with open(filename, "rb") as f:
        model = pickle.load(f)
    return model


def _job_forward2d(
    source_index,
    m,
    dx,
    dz,
    source,
    receiver,
    nsweep=2,
    raytrace=True,
    stepsize=None,
    max_step=None,
    honor_grid=True,
    cache_path="./.cache_pyeikonal_tt",
):
    if raytrace:
        tt_gradient = True
    else:
        tt_gradient = False

    eik = Eikonal2D(m, dx, dz)
    eik.set_source(source)
    eik.set_receiver(receiver)
    eik.forward(nsweep=nsweep, tt_gradient=tt_gradient)
    tt = eik.calculate_tt()
    tt_file = cache_path / f"eikonal_tt_{source_index}.npz"
    np.savez(tt_file, tt=tt)

    if raytrace:
        ray = eik.raytrace(stepsize=stepsize, max_step=max_step, honor_grid=honor_grid)
        ray_file = cache_path / f"eikonal_ray_{source_index}.npy"
        np.save(ray_file, np.array(ray, dtype=object))


def forward2d(
    m,
    dx,
    dz,
    source,
    receiver,
    nsweep=2,
    raytrace=True,
    stepsize=None,
    max_step=None,
    honor_grid=True,
    cache_path="./.cache_forward",
    jobs=1,
):
    # check cache path
    cache_path = Path(cache_path)
    if cache_path.exists():
        shutil.rmtree(cache_path)
    cache_path.mkdir(parents=True, exist_ok=True)

    # calculate
    source_num = len(source)
    if jobs == 1:
        for i in range(source_num):
            _job_forward2d(
                i,
                m,
                dx,
                dz,
                source[i],
                receiver,
                nsweep,
                raytrace,
                stepsize,
                max_step,
                honor_grid,
                cache_path,
            )

    elif jobs > 1:
        Parallel(n_jobs=jobs, backend="loky")(
            delayed(_job_forward2d)(
                i,
                m,
                dx,
                dz,
                source[i],
                receiver,
                nsweep,
                raytrace,
                stepsize,
                max_step,
                honor_grid,
                cache_path,
            )
            for i in range(source_num)
        )

    # read cache
    tts = []
    rays = []
    for i in range(source_num):
        tt_file = cache_path / f"eikonal_tt_{i}.npz"
        data = np.load(tt_file)
        tts.append(data["tt"])
        if raytrace:
            ray_file = cache_path / f"eikonal_ray_{i}.npy"
            data = np.load(ray_file, allow_pickle=True).tolist()
            rays.append(data[:])

    return tts, rays
