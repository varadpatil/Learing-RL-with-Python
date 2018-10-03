#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:28:25 2018

@author: varad
"""

'''
Creating a k armed bandit problem for k = 10
action values q*(a), a = 1,2,...,10 were selected with normal distribution mean 0 and variance 1
actual reward for selected action At were selected with normal distribution with mean q*(At) and variance 1
in a particular seting there will be 2000 such k-armed bandits

'''

import numpy as np

# creating a k armmed bandit
class K_armmed_bandit:
    
    def __init__(self):
        self.q_star = np.random.normal(0, 1, 10)
        
    def run(self, i):
        mean = self.q_star[i-1]
        return np.random.normal(mean,1)
    
def epsilon_greedy(bandit, epsilon, n=1000):
    
    self.n = n
    r = np.zeros(10)
    