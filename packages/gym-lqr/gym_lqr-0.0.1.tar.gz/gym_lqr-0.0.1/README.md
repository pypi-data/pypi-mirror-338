## Gym Interface for LQR-Family Problems

Gym-LQR is a one-stop shop for data-driven
LQR research.

Gym-LQR creates a discrete-time LQR environment
from a subset of
[COMPleib](http://www.complib.de/) problems.
Currently supported systems:
- HEx - Helicopter models
- REAx - Reactor models
- DISx - Decentralized interconnected systems
- TG1 - 1072 MVA nuclear-powered turbo-generator
- AGS - Automobile gas turbine
- BDT1 - Realistic model of binary distillation tower
- MFP - Moored floating platform
- UWV - Control surface servo for underwater vehicle
- EBx - Euler-Bernoulli beam
- PAS - Piezoelectric bimorph actuator system design
- TF - Terrain following model
- PSM - Two-area interconnected power system
- NNx - Academic test problems
- DLRx - Models of space structure
- ROCx - Reduced order control problems


### Installation

```bash
pip install gym-lqr
```

Requires Python 3.10+.


### Basic Usage

#### Single-agent (Centralized LQR)

Single-agent interface follows a familiar Gymnasium (ex- OpenAI Gym) `gymnasium>=0.26` API.

```python
import gymnasium as gym
# Register the LQR environment
import gym_lqr

# Create a Linear HE1 helicopter model from the COMPleib example set
# Discretize at a sampling rate of dt=0.1
env = gym.make('LQR-v0', env_id='HE1', dt=0.1)

# Fix the random seed for reproducibility
env.action_space.seed(1337)

# Reset the environment to generate the first observation
observation, info = env.reset(seed=1337)
for _ in range(100):
    # this is where you would insert your policy
    action = env.action_space.sample()

    # step (transition) through the environment with the action
    # receiving the next observation, reward and if the episode has terminated or truncated
    observation, reward, terminated, truncated, info = env.step(action)

    # If the episode has ended then we can reset to start a new episode
    if terminated or truncated:
        observation, info = env.reset()

env.close()
```

#### Multi-agent (Distributed LQR)

In development.

### Future Releases

- Support for more COMPleib problems.
- Multi-agent (Distributed LQR) interface based on the
  [PettingZoo](https://pettingzoo.farama.org/index.html) API.

### References

1. Gymnasium - an API standard for reinforcement learning with a
   diverse collection of reference environments. Web: https://gymnasium.farama.org/index.html
2. COMPleib: COnstraint Matrix-optimization Problem library.
   Web: http://www.complib.de/
3. "Predictive Control for Linear and Hybrid Systems"
   by Francesco Borrelli, Alberto Bemporad, Manfred Morari (2017).
   Web: http://cse.lab.imtlucca.it/~bemporad/publications/papers/BBMbook.pdf
