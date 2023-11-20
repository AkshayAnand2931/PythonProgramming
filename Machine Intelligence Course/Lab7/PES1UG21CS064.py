import torch

class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of states
        emissions: list of observations
        B: Emission probabilities
    """

    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between states and indexes
        """
        self.states_dict = {state: i for i, state in enumerate(self.states)}
        self.emissions_dict = {emission: i for i, emission in enumerate(self.emissions)}

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations, must be in the emissions dict)
        Returns:
            Most likely sequence of hidden states given the observation sequence
        """
        T = len(seq)
        delta = [[0.0] * self.N for i in range(T)]
        delta_argmax = [[0] * self.N for i in range(T)]

        for j in range(self.N):
            delta[0][j] = self.pi[j] * self.B[j][self.emissions_dict[seq[0]]]

        for t in range(1, T):
            for j in range(self.N):
                probabilities = [delta[t - 1][i] * self.A[i][j] * self.B[j][self.emissions_dict[seq[0]]] for i in range(self.N)]
                delta[t][j] = max(probabilities)
                delta_argmax[t][j] = max(range(self.N),key = lambda i: probabilities[i])
        
        best_path = [0] * T
        best_path[-1] = max(range(self.N), key = lambda j: delta[-1][j])

        for t in range(T - 2, -1, -1):
            best_path[t] = delta_argmax[t + 1][best_path[t + 1]]
  
        best_path_states = [self.states[i] for i in best_path]
        return best_path_states