import numpy as np


def topsis_method(dataset, weights, criterion_type):
    X = np.copy(dataset)
    w = np.copy(weights)
    sum_cols = np.sum(X * X, axis=0)
    sum_cols = sum_cols ** (1 / 2)
    r_ij = X / sum_cols
    v_ij = r_ij * w
    p_ideal_A = np.zeros(X.shape[1])
    n_ideal_A = np.zeros(X.shape[1])

    for i in range(0, dataset.shape[1]):
        if (criterion_type[i] == 'max'):
            p_ideal_A[i] = np.max(v_ij[:, i])
            n_ideal_A[i] = np.min(v_ij[:, i])
        else:
            p_ideal_A[i] = np.min(v_ij[:, i])
            n_ideal_A[i] = np.max(v_ij[:, i])

    p_s_ij = (v_ij - p_ideal_A) ** 2
    p_s_ij = np.sum(p_s_ij, axis=1) ** (1 / 2)
    n_s_ij = (v_ij - n_ideal_A) ** 2
    n_s_ij = np.sum(n_s_ij, axis=1) ** (1 / 2)
    c_i = n_s_ij / (p_s_ij + n_s_ij)

    return c_i
