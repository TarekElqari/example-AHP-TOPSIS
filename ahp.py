import numpy as np
from functools import reduce


def ahp_method(dataset, wd='m'):
    inc_rat = np.array([0, 0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51, 1.48, 1.56, 1.57, 1.59])
    X = np.copy(dataset)
    weights = np.zeros(X.shape[1])

    if (wd == 'm' or wd == 'mean'):
        weights = np.mean(X / np.sum(X, axis=0), axis=1)
        vector = np.sum(X * weights, axis=1) / weights
        lamb_max = np.mean(vector)
    elif (wd == 'g' or wd == 'geometric'):
        for i in range(0, X.shape[1]):
            weights[i] = reduce((lambda x, y: x * y), X[i, :]) ** (1 / X.shape[1])
        weights = weights / np.sum(weights)
        vector = np.sum(X * weights, axis=1) / weights
        lamb_max = np.mean(vector)
    elif (wd == 'me' or wd == 'max_eigen'):
        eigenvalues, eigenvectors = np.linalg.eig(X)
        eigenvalues_real = np.real(eigenvalues)
        lamb_max_index = np.argmax(eigenvalues_real)
        lamb_max = eigenvalues_real[lamb_max_index]
        principal_eigenvector = np.real(eigenvectors[:, lamb_max_index])
        weights = principal_eigenvector / principal_eigenvector.sum()

    cons_ind = (lamb_max - X.shape[1]) / (X.shape[1] - 1)
    rc = cons_ind / inc_rat[X.shape[1]]
    return weights, rc
