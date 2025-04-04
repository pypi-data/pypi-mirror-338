import pytest

import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal

import gym_lqr
from gym_lqr.compleib import get_model_from_compleib


def test_load_compleib_matrices():
    for supported_id in gym_lqr.compleib.SUPPORTED_COMPLEIB_SYSTEMS:
        # print(supported_id)

        # A, B1, B, C1, C, D11, D12, D21, nx, nw, nu, nz, ny = COMPleib(supported_id)
        is_cont, A, B, B1 = get_model_from_compleib(supported_id)

        assert is_cont

        # A
        assert isinstance(A, np.ndarray)
        n_x1, n_x2 = A.shape
        assert n_x1 == n_x2

        # B
        assert isinstance(B, np.ndarray)
        n_x, n_u = B.shape
        assert n_x == n_x1

        # B1
        # TODO check B1 matrices for all compleib examples
        if not isinstance(B1, list):
            assert isinstance(B1, np.ndarray)
            n_x3, n_w = B1.shape
            assert n_x3 == n_x1


def test_accuracy_compleib_matrices():
    selected_ids = ['AC1', 'HE1', 'NN1', ]

    for selected_id in selected_ids:
        A_true, B_true = _get_system_matrices_from_cache(selected_id)
        is_cont, A, B, B1 = get_model_from_compleib(selected_id)

        assert is_cont
        assert_array_equal(A_true, A)
        assert_array_equal(B_true, B)


def _get_system_matrices_from_cache(env_id: str):
    match env_id:
        case 'AC1':
            A = np.array(
                [
                    [0.0000, 0.0000, 1.1320, 0.0000, -1.000],
                    [0.0000, -0.0538, -0.1712, 0.0000, 0.0705],
                    [0.0000, 0.0000, 0.0000, 1.0000, 0.0000],
                    [0.0000, 0.0485, 0.0000, -0.8556, -1.013],
                    [0.0000, -0.2909, 0.0000, 1.0532, -0.6859],
                ]
            )

            B = np.array(
                [
                    [0.0000, 0.0000, 0.0000],
                    [-0.120, 1.0000, 0.0000],
                    [0.0000, 0.0000, 0.0000],
                    [4.4190, 0.0000, -1.665],
                    [1.5750, 0.0000, -0.0732],
                ]
            )

            return A, B

        case 'HE1':
            A = np.array(
                [
                    [-0.0366, 0.0271, 0.0188, -0.4555],
                    [0.0482, -1.01, 0.0024, -4.0208],
                    [0.1002, 0.3681, -0.707, 1.42],
                    [0, 0, 1, 0],
                ]
            )

            B = np.array(
                [
                    [0.4422, 0.1761],
                    [3.5446, -7.5922],
                    [-5.52, 4.49],
                    [0, 0],
                ]
            )
            return A, B
        case 'NN1':
            A = np.array(
                [
                    [0, 1, 0],
                    [0, 0, 1],
                    [0, 13, 0],
                ]
            )

            B = np.array(
                [
                    [0],
                    [0],
                    [1],
                ]
            )
            return A, B
        case _:
            raise NotImplementedError
