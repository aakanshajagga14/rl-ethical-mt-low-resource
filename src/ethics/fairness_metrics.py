import numpy as np

def fairness_index(scores):
    return np.std(scores)
