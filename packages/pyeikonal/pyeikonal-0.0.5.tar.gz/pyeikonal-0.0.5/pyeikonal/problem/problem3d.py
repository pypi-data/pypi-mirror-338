import copy
import pickle
import textwrap
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from joblib import Parallel, delayed
from pyeikonal.eikonal import Eikonal3D


def load_problem3d(filename):
    with open(filename, "rb") as f:
        prob = pickle.load(f)
    return prob


class Problem3D:
    def __init__(self, dx, dy, dz, nx, ny, nz):

        self.source = []
        self.receiver = []
        self.tt = []
        self.weight = []
        self.dx = dx
        self.dz = dz
        self.nx = nx
        self.nz = nz
        self.regularization_flag = False
        self.smooth_factor = 1
        self.tikhonov_order = 0
        self.matL = np.array([])

        # initial reference model
        self.ref_model = np.zeros(2)

        # config
        self.config()

    def __str__(self):
        pass

    def __repr__(self):
        return str(self)
