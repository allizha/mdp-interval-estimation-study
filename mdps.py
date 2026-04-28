import numpy as np


class MDP:
    def __init__(self, n_states, n_actions):
        self.n_states = n_states
        self.n_actions = n_actions
        self.P = np.zeros([n_states, n_actions, n_states])
        self.R = np.zeros([n_states, n_actions])

    def get_transition_probability(self, state, action, next_state):
        return self.P[state, action, next_state]

    def generate_state(self, state, action):
        return np.random.choice(self.n_states, p=self.P[state, action])

    def get_reward(self, state, action):
        return self.R[state, action]


class RiverSwimMDP(MDP):
    def __init__(self):
        super().__init__(6, 2)
        self.P = np.array(
            [  # action 0           #action 1
                [[1, 0, 0, 0, 0, 0], [0.7, 0.3, 0, 0, 0, 0]],  # state 0
                [[1, 0, 0, 0, 0, 0], [0.1, 0.6, 0.3, 0, 0, 0]],  # state 1
                [[0, 1, 0, 0, 0, 0], [0, 0.1, 0.6, 0.3, 0, 0]],  # state 2
                [[0, 0, 1, 0, 0, 0], [0, 0, 0.1, 0.6, 0.3, 0]],  # state 3
                [[0, 0, 0, 1, 0, 0], [0, 0, 0, 0.1, 0.6, 0.3]],  # state 4
                [[0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0.7, 0.3]],  # state 5
            ]
        )

        self.R = np.array(
            [
                [5, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 3000],
            ]
        )


class SixArmsMDP(MDP):
    def __init__(self):
        super().__init__(7, 6)
