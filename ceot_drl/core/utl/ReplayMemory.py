""" 
    An experience reply memory class used in many DLR models. 
    It is impelemented as a cyclic queue and is used manily for min-batch sampling
"""
  
import numpy as np

class ReplayMemory:
    def __init__(self, 
                state_size,
                action_size, 
                size=1e6,
                batch_size=64, 
                state_type=np.float32, 
                action_type=np.uint16):
        self.size = int(size)
        self.state_type = state_type
        self.action_type = action_type
        self.batch_size = batch_size
        self.state = np.zeros((self.size, state_size), dtype=self.state_type)
        self.state_ = np.zeros((self.size, state_size), dtype=self.state_type)
        self.reward = np.zeros(self.size, dtype=np.float32)
        self.action = np.zeros(self.size, dtype=self.action_type)
        self.done = np.zeros(self.size, dtype=np.bool)

        self.next_index = 0 # initial position in the memory
        self.folds = 0 # keep track of how many folds we traverssed the memory, useful for 



    def remember(self, state, state_, reward, action, done):
        """ Remeber an experience. 
            The memory is cyclic, therefore we use an index that continues cycling.
        
        Keyword arguments:
        state -- current state
        state_ -- next state
        reward -- obtained reward
        action -- action
        done -- true if the state_ is terminal
        """

        # store them
        self.state[self.next_index] = state
        self.action[self.next_index] = action
        self.reward[self.next_index] = reward
        self.state_[self.next_index] = state_
        self.done[self.next_index] = done
        
        # move to the next index
        self.folds += (self.next_index + 1) // self.size 
        self.next_index = (self.next_index + 1) % self.size 
        



    def sample(self, batch_size=0):

        """ Minibatch sampling from the reply memory
        The memory is cyclic, therefore we use an index that continues cycling.
        
        return values:
        state -- current state
        state_ -- next state
        reward -- obtained reward
        action -- action
        done -- true if the state_ is terminal
        """

        # check if a batch_size is provided, otherwise use the original one
        if batch_size <= 0:
            batch_size = self.batch_size
        
        size = self.size
        if self.folds < 1: # we still did not fill it all up
            size = self.next_index

        indices = np.random.choice(size, batch_size, replace=False)
        state = self.state[indices]
        state_ = self.state_[indices]
        reward = self.reward[indices]
        action = self.action[indices]
        done = self.done[indices]

        return state, state_, reward, action, done