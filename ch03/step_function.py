# coding: utf-8
import numpy as np


def step_function(x):
    y = x > 0
    return y.astype(np.int)

        
