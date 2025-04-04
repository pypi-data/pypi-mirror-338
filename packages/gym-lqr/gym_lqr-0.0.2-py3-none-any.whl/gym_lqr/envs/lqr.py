from typing import Tuple, Optional, Union, List, Dict, Sequence, Union

import numpy as np
from scipy.signal import cont2discrete
import gymnasium as gym
from gymnasium import spaces
from gymnasium.core import ActType, ObsType, RenderFrame

from gym_lqr.compleib import get_model_from_compleib
from gym_lqr.utils import solve_inf_horizon_dare


class LQR(gym.Env):
    def __init__(
            self,
            env_id: str,
            dt: float = 0.1,
            state_reward_matrix: Optional[np.ndarray] = None,
            action_reward_matrix: Optional[np.ndarray] = None,
            force_deterministic: bool = False,
            # initial state distribution
            reset_settings: Tuple[str, Union[float, np.ndarray], Union[float, np.ndarray]] = ('normal', 0.0, 1.0),
    ):
        self._deterministic = force_deterministic

        # get system matrices by ID
        res = get_model_from_compleib(env_id.strip().upper())
        if res is not None:
            is_continuous, *model = res

            if is_continuous:
                # discretize system
                Ac, Bc, Gc = model
                n_s, n_a = Bc.shape

                # discretize deterministic part with ZOH
                A, B, *_ = cont2discrete(
                    system=(Ac, Bc, np.zeros((1, n_s)), np.zeros((1, n_a))), dt=dt)

                # discretize stochastic part
                if Gc is not None:
                    G = Gc @ Gc.T * dt
            else:
                A, B, G = model
        else:
            raise ValueError(f'Env ID not recognized: {env_id}.')

        # save R(s,a) params
        n_s, n_a = B.shape
        Q = -np.eye(n_s) if state_reward_matrix is None else state_reward_matrix
        R = -np.eye(n_a) if action_reward_matrix is None else action_reward_matrix

        # assign internal variables
        self._A = A.astype(np.float32)
        self._B = B.astype(np.float32)
        self._Q = Q.astype(np.float32)
        self._R = R.astype(np.float32)
        self._n_s, self._n_a = B.shape

        if not force_deterministic:
            # handle stochasticity
            if not isinstance(G, np.ndarray):
                raise ValueError(f'Noise matrix not defined for a stochastic problem.')

            self._G = G.astype(np.float32)
            self._n_w = G.shape[1]
        else:
            self._G = None
            self._n_w = None

        # dimensions
        self._check_dimensions()

        # define spaces S and A
        # TODO consider switch to float64
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(n_s,), dtype=np.float32,
        )
        self.action_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(n_a,), dtype=np.float32,
        )

        # custom initial state distribution
        self._reset_settings = reset_settings

    def _check_dimensions(self):
        n, n_ = self._A.shape
        assert n == n_
        assert n == self._n_s
        n_, m = self._B.shape
        assert n == n_

        q_n, q_n_ = self._Q.shape
        assert q_n == self._n_s
        assert q_n_ == self._n_s

        r_m, r_m_ = self._R.shape
        assert r_m == self._n_a
        assert r_m_ == self._n_a

        if not self._deterministic:
            n_s1, n_w = self._G.shape
            assert n_s1 == self._n_s

    @property
    def n_s(self) -> int:
        return self._n_s

    @property
    def n_a(self) -> int:
        return self._n_a

    def step(self, action: ActType) -> Tuple[ObsType, float, bool, bool, dict]:
        # get current reward
        curr_reward = self._state.T @ self._Q @ self._state + action.T @ self._R @ action

        # transition to next state and update internal state
        obs = self._A @ self._state + self._B @ action

        if not self._deterministic:
            obs += self._G @ self.np_random.standard_normal(size=(self._n_w,))

        self._state = obs

        # TODO fill terminated
        # TODO fill info

        # !! truncated is filled by the TimeLimit wrapper

        # observation, reward, terminated, truncated, info
        return obs, curr_reward, False, False, {}

    def reset(
            self,
            *,
            seed: Optional[int] = None,
            options: Optional[dict] = None,
    ) -> Tuple[ObsType, dict]:
        super().reset(seed=seed)

        # TODO either cache or make a callable fn
        distro_id, *options = self._reset_settings
        if distro_id == 'normal':
            d_mean, d_var = options
            obs = self.np_random.normal(loc=d_mean, scale=d_var, size=(self._n_s,))
        elif distro_id == 'mvn':
            d_means, d_covs = options
            obs = self.np_random.multivariate_normal(mean=d_means, cov=d_covs, size=1)
            obs = np.reshape(obs, newshape=(-1,))
        else:
            raise ValueError(f'Initial State distribution not recognized: {distro_id}.')

        obs = obs.astype(np.float32)
        self._state = obs

        # TODO return copy?
        # return np.array(self._state), {}

        return obs, {}

    def get_model(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, Optional[np.ndarray]]:
        return self._A, self._B, self._Q, self._R, self._G
