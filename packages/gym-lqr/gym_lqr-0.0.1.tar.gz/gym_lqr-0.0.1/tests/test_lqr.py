import pytest

import numpy as np
from numpy.testing import assert_array_almost_equal
import gymnasium

import gym_lqr
from gym_lqr.utils import solve_inf_horizon_dare, solve_finite_horizon_iterative


@pytest.fixture()
def env_deterministic():
    env = gymnasium.make('LQR-v0', env_id='HE1', dt=0.1, force_deterministic=True)
    return env


@pytest.fixture()
def env_stochastic():
    env = gymnasium.make('LQR-v0', env_id='HE1', dt=0.1, force_deterministic=False)
    return env


def test_env_creation(env_stochastic):
    env = env_stochastic
    assert env is not None
    spec = env.spec
    assert spec is not None
    assert spec.id == 'LQR-v0'
    assert spec.max_episode_steps == 100


def test_seeding(env_stochastic):
    # sources of stochasticity:
    # 1) transition dynamics, As + Ba + Gw
    # 2) initial state, s0
    # 3) action space sampling, a'

    env = env_stochastic

    # action sampling
    env.action_space.seed(1337)
    action1 = env.action_space.sample()
    action2 = env.action_space.sample()
    assert_array_almost_equal(action1, np.array([0.03826822, 0.47393644]))
    assert_array_almost_equal(action2, np.array([-0.13774592, -1.3893344]))

    # reset()
    obs, info = env.reset(seed=42)
    assert_array_almost_equal(obs, np.array([0.30471708, -1.03998411, 0.7504512, 0.94056472]))

    obs, info = env.reset(seed=1337)
    assert_array_almost_equal(obs, np.array([0.03826822, 0.47393644, -0.13774592, -1.38933444]))

    # step()
    obs, reward, terminated, truncated, info = env.step(action1)
    assert_array_almost_equal(obs, np.array([0.11384688, 0.63419139, -0.11328475, -1.40240975]))

    obs, reward, terminated, truncated, info = env.step(action2)
    assert_array_almost_equal(obs, np.array([0.1507082, 2.07405245, -0.77862635, -1.44799034]))


def test_step_reset(env_deterministic):
    env = env_deterministic

    # reset
    state1, _ = env.reset(seed=42)
    assert_array_almost_equal(state1, np.array([[0.30471708], [-1.03998411], [0.7504512], [0.94056472]]).flatten(),
                              decimal=7)
    # assert_array_almost_equal(env._state, np.array([[0.30471708], [-1.03998411], [0.7504512], [0.94056472]]),
    #                           decimal=7)

    state2, _ = env.reset()
    assert_array_almost_equal(state2, np.array([[-1.95103519], [-1.30217951], [0.1278404], [-0.31624259]]).flatten(),
                              decimal=7)
    # assert_array_almost_equal(env._state, np.array([[-1.95103519], [-1.30217951], [0.1278404], [-0.31624259]]),
    #                           decimal=7)

    # step
    env.action_space.seed(42)
    random_action = env.action_space.sample()
    assert_array_almost_equal(random_action, np.array([[0.3047171], [-1.0399841]]).flatten(), decimal=7)

    # print(random_action)
    obs, reward, terminated, truncated, info = env.step(random_action)

    # reward
    Q = -np.eye(4)
    R = -np.eye(2)
    r = state2.T @ Q @ state2 + random_action.T @ R @ random_action
    assert r == pytest.approx(reward, abs=1e-15)

    r2 = state2.reshape((-1, 1)).T @ Q @ state2.reshape((-1, 1)) \
         + random_action.reshape((-1, 1)).T @ R @ random_action.reshape((-1, 1))
    assert r2 == pytest.approx(reward, abs=1e-15)

    # assert -6.7929817713975975 == pytest.approx(reward, abs=1e-15)

    assert_array_almost_equal(obs, np.array([[-1.93655611], [-0.2090532], [-0.58341538], [-0.33974853]]).flatten(),
                              decimal=7)
    # assert_array_almost_equal(env._state, np.array([[-1.93655611], [-0.2090532], [-0.58341538], [-0.33974853]]),
    #                           decimal=7)


def test_analytical_solution_dare(env_deterministic):
    env = env_deterministic
    gamma = 0.9

    A, B, Q, R, G = env.unwrapped.get_model()

    P_star, K_star, H_star = solve_inf_horizon_dare(A, B, Q, R, gamma)

    K_true = np.array([
        [-0.24757138, 0.06913417, 0.59584428, 0.50203523],
        [-0.06863856, 0.50626815, -0.06780187, -0.42363873]
    ])
    assert_array_almost_equal(K_star, K_true, decimal=8)

    P_true = np.array([
        [-8.58665047, -0.29239307, -0.23409396, 2.32563724],
        [-0.29239307, -2.18316686, -0.8961866, 0.27412515],
        [-0.23409396, -0.8961866, -2.67158614, -0.9236831],
        [2.32563724, 0.27412515, -0.9236831, -9.46760938],
    ])
    assert_array_almost_equal(P_star, P_true, decimal=8)

    print(H_star)

    H_true = np.array([
        [-8.67650749, -0.27626009, -0.01354423, 2.51820535, -0.36805357, 0.01839361],
        [-0.27626009, -2.65747334, -0.71029154, 0.78424786, -0.20223606, 0.96448474],
        [-0.01354423, -0.71029154, -3.32077629, -1.6568806, 1.03171548, -0.50807435],
        [2.51820535, 0.78424786, -1.6568806, -10.50966887, 1.09878706, -1.15766013],
        [-0.36805357, -0.20223606, 1.03171548, 1.09878706, -1.66026439, 0.6261841, ],
        [0.01839361, 0.96448474, -0.50807435, -1.15766013, 0.6261841, -1.99059621]
    ])
    assert_array_almost_equal(H_star, H_true, decimal=8)


def test_analytical_solution_iterative(env_deterministic):
    env = env_deterministic
    gamma = 0.9

    A, B, Q, R, G = env.unwrapped.get_model()
    P_star, K_star = solve_finite_horizon_iterative(A, B, Q, R, gamma=gamma, horizon=500)

    K_true = np.array([
        [-0.24757138, 0.06913417, 0.59584428, 0.50203523],
        [-0.06863856, 0.50626815, -0.06780187, -0.42363873]
    ])

    P_true = np.array([
        [-8.58665047, -0.29239307, -0.23409396, 2.32563724],
        [-0.29239307, -2.18316686, -0.8961866, 0.27412515],
        [-0.23409396, -0.8961866, -2.67158614, -0.9236831],
        [2.32563724, 0.27412515, -0.9236831, -9.46760938],
    ])

    assert_array_almost_equal(P_star, P_true, decimal=7)
    assert_array_almost_equal(K_star, K_true, decimal=7)


def test_stochastic_lqr(env_stochastic):
    env = env_stochastic

    action_map = {
        0: np.array([0.3047171, -1.0399841]),
        1: np.array([0.7504512, 0.9405647]),

    }

    obs_map = {
        0: np.array([0.25296043, -0.45615528, 0.19469813, 0.98759694]),
        1: np.array([0.25436311, -1.21962304, 0.29844235, 1.01256345]),
    }

    r_map = {
        0: -3.7966778729800703,
        1: -2.7331606444645304,
    }

    # env = gymnasium.make('LQR-v0', env_id='AC1', dt=0.1, deterministic=False)

    # fix seeding
    env.action_space.seed(42)
    obs, info = env.reset(seed=42)

    # iterate
    for i in range(2):
        action = env.action_space.sample()
        assert_array_almost_equal(action, action_map[i])

        obs, reward, terminated, truncated, info = env.step(action)
        assert_array_almost_equal(obs, obs_map[i])
        assert_array_almost_equal(reward, r_map[i])


def test_external_initial_distro():
    # DEFAULT
    env = gymnasium.make('LQR-v0', env_id='AC1', dt=0.1)

    obs1, _ = env.reset(seed=42)
    assert_array_almost_equal(obs1, np.array([0.30471708, -1.03998411, 0.7504512, 0.94056472, -1.95103519]))

    obs2, _ = env.reset()
    assert_array_almost_equal(obs2, np.array([-1.30217951, 0.1278404, -0.31624259, -0.01680116, -0.85304393]))

    env.close()

    # CUSTOM - NORMAL
    env = gymnasium.make('LQR-v0', env_id='AC1', dt=0.1, reset_settings=('normal', 100.0, 500.0))

    obs1, _ = env.reset(seed=42)
    assert_array_almost_equal(obs1, np.array([252.35853988, -419.99205312, 475.2255979, 570.2823582, -875.51759433]))

    obs2, _ = env.reset()
    assert_array_almost_equal(obs2, np.array([-551.08975343, 163.92020158, -58.12129617, 91.59942125, -326.52196379]))
    env.close()

    # CUSTOM - MVN
    d_means = np.array([0., 0., 500., 100., -50.0])
    d_covar = np.eye(5)

    env = gymnasium.make('LQR-v0', env_id='AC1', dt=0.1, reset_settings=('mvn', d_means, d_covar))
    obs1, _ = env.reset(seed=42)
    assert_array_almost_equal(obs1, np.array([0.30471708, -1.03998411, 500.7504512, 100.94056472, -51.95103519]))

    obs2, _ = env.reset()
    assert_array_almost_equal(obs2, np.array([-1.30217951, 0.1278404, 499.68375741, 99.98319884, -50.85304393]))
    env.close()


def test_truncation(env_stochastic):
    env = env_stochastic

    # fix seeds
    truncated = False
    env.action_space.seed(42)
    obs, info = env.reset(seed=42)

    # iterate
    for i in range(100):
        obs, reward, terminated, truncated, info = env.step(env.action_space.sample())

    assert truncated
