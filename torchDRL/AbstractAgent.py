#!/usr/bin/env python
""" 
    An abstract agent
"""
__author__ = "AL-Tam Faroq"
__copyright__ = "Copyright 2020, UALG"
__credits__ = ["Faroq AL-Tam"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Faroq AL-Tam"
__email__ = "ftam@ualg.pt"
__status__ = "Production"

#from abc import ABC
from MLS.torchDRL.utl.ReplayMemory import ReplayMemory
from MLS.torchDRL.DNN import DNN 

class AbstractAgent():
    def __init__(self,
                 actor:DNN, 
                 critic:DNN, 
                 replay_memory:ReplayMemory, 
                 state_size, 
                 action_space,
                 mini_batch_size=64):
        self.actor = actor
        self.critic = critic
        self.replay_memory = replay_memory
        self.state_size = state_size
        self.action_space = action_space
        self.mini_batch_size = mini_batch_size

    def validate(self):
        return True
            # TO BE FINISHED LATER
            #assert self.state_size is not None, 'state shape can not be None'
            #assert self.state_size < 1
    
    def learn(self, *args):
        raise NotImplementedError

    def get_action(self, state):
        raise NotImplementedError

    def get_critic(self):
        raise NotImplementedError

    def get_actor(self):
        raise NotImplementedError