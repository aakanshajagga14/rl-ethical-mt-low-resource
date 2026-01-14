import numpy as np

def bias_score(a, b):
    return abs(np.mean(a) - np.mean(b))
