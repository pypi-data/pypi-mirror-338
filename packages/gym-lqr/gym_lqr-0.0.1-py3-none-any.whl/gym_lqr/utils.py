from typing import Tuple

import numpy as np
from scipy.linalg import solve_discrete_are as dare


def diff(
        a: np.ndarray,
        b: np.ndarray,
        method='l2',
) -> float:
    # Note: Vector norms of (A-B)
    if method == 'inf':
        return np.max(np.abs(a - b))
    elif method == 'l2':
        # (numpy): If both axis and ord are None, the 2-norm of x.ravel will be returned.
        # i.e. ||vec(A-B)||_2
        return np.linalg.norm(a - b)
    else:
        raise ValueError(f'Method not recognized {method}.')


def solve_inf_horizon_dare(
        A: np.ndarray,
        B: np.ndarray,
        Q: np.ndarray,
        R: np.ndarray,
        gamma: float = 1.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # scale the problem to accommodate gamma<1
    A_scaled, B_scaled = A * np.sqrt(gamma), B * np.sqrt(gamma)

    # calculate the value function P with Riccati iterations
    P_star = dare(A_scaled, B_scaled, Q, R)

    # knowing P, find the policy K
    K_star = -np.linalg.solve(R + B_scaled.T @ P_star @ B_scaled, B_scaled.T @ P_star @ A_scaled)

    # knowing P, find the policy K
    H_ss = Q + gamma * A.T @ P_star @ A
    H_sa = gamma * A.T @ P_star @ B
    H_as = gamma * B.T @ P_star @ A
    H_aa = R + gamma * B.T @ P_star @ B
    H_star = np.block([
        [H_ss, H_sa],
        [H_as, H_aa],
    ])

    return P_star, K_star, H_star


def solve_finite_horizon_iterative(
        A: np.ndarray,
        B: np.ndarray,
        Q: np.ndarray,
        R: np.ndarray,
        horizon: int,
        gamma: float = 1.0,
        eps: float = 1e-8,
) -> Tuple[np.ndarray, np.ndarray]:
    # scale the problem to accommodate gamma<1
    A_scaled, B_scaled = A * np.sqrt(gamma), B * np.sqrt(gamma)

    # calculate P, K by iteratively updating P
    err = np.inf
    iter = 0
    P_star = Q
    while err > eps and iter < horizon:
        pa = P_star @ A_scaled
        pb = P_star @ B_scaled

        P_next = Q + A_scaled.T @ pa - A_scaled.T @ pb @ np.linalg.inv(
            R + B_scaled.T @ pb) @ B_scaled.T @ pa

        err = diff(P_next, P_star)

        P_star = P_next
        iter += 1

    K_star = - np.linalg.inv(R + B_scaled.T @ P_star @ B_scaled) @ B_scaled.T @ P_star @ A_scaled

    return P_star, K_star
