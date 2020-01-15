#!/usr/bin/env python
""" 
    Implementaion of Deep Q network algorithm
"""
__author__ = "AL-Tam Faroq"
__copyright__ = "Copyright 2020, UALG"
__credits__ = ["Faroq AL-Tam"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Faroq AL-Tam"
__email__ = "ftam@ualg.pt"
__status__ = "Production"

from AbstractAgent import AbstractAgent
from DNN import DNN
from utl.ReplayMemory import ReplayMemory

class DQNAgent(AbstractAgent):
    def __init__(self, 
                 state_shape,
                 action_shape,
                 critic:DNN, # Online critic
                 target_critic:DNN,
                 replay_memory:ReplayMemory,
                 epsilon=0.99,
                 delta_epsilon=1e-4, # epsilon decay
                 smoothing_factor=1e-3,
                 smoothing_frequency=20): 

        super(DQNAgent, self).__init__(critic=critic,
                                       state_shape=state_shape,
                                       action_shape=action_shape,
                                       replay_memory=replay_memory)
        
        self.target_critic = target_critic
        self.epsilon = epsilon
        self.delta_epsilon = delta_epsilon
        self.smoothing_factor = smoothing_factor
        self.smoothing_frequency = smoothing_frequency


    def validate(self, parameter_list):
        super.validate()

    def train(self):
        print('here goes the training')
    





if __name__ == "__main__":
    # execute only if run as a script
   pass
    