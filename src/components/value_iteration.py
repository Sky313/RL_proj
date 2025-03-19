from src.components.game_rules import *
import numpy as np

class ValueIterationSolver:
    def __init__(self, gamma=0.8, theta=1e-3):
        """Gamma: Discount factor, Theta: Threshold for convergence""" 
        self.theta = theta 
        self.gamma = gamma 
        self.values = {}
        self.policy = {}
        
    def initialize(self, states):
        """Initialize value function"""
        self.values = {s: 0 for s in states}
        for s in states:
            if is_terminal(s):
                self.values[s] = get_reward(s)
    
    def update(self, states):
        """Single iteration of value iteration"""
        delta = 0
        for s in states:
            if is_terminal(s):
                continue
                
            q_values = []
            for a in get_actions(s):
                s_prime = apply_action(s, a)
                
                if is_terminal(s_prime):
                    q = get_reward(s_prime)
                else:
                    # Opponent plays optimally (minimize our value)
                    opp_actions = get_actions(s_prime)
                    opp_values = [self.values[apply_action(s_prime, a_opp)] 
                                for a_opp in opp_actions]
                    q = self.gamma * (min(opp_values) if s.player == 'X' else max(opp_values))
                
                q_values.append(q)
            
            new_value = max(q_values) if s.player == 'X' else min(q_values)
            delta = max(delta, abs(self.values[s] - new_value))
            self.values[s] = new_value
        return delta
    
    def solve(self, states):
        self.initialize(states)
        iteration = 0
        while True:
            delta = self.update(states)
            iteration += 1
            print(f"Iteration {iteration}, Delta: {delta}")
            if delta < self.theta:
                break
                
    def derive_policy(self, states):
        """Extract the optimal policy from value function"""
        self.policy = {}
        for s in states:
            if is_terminal(s):
                continue
                
            best_action = None
            best_value = -np.inf if s.player == 'X' else np.inf
            
            for a in get_actions(s):
                s_prime = apply_action(s, a)
                value = self.values[s_prime]
                
                if (s.player == 'X' and value > best_value) or \
                   (s.player == 'O' and value < best_value):
                    best_value = value
                    best_action = a
                    
            self.policy[s] = best_action