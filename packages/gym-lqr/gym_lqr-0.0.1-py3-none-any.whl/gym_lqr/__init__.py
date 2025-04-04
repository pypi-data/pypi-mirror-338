from gymnasium.envs.registration import register

__version__ = '0.0.1'

register(
    id='LQR-v0',
    entry_point='gym_lqr.envs:LQR',
    max_episode_steps=100,
)
