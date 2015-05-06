# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:55:34 2015

@author: 3302744
"""

class defenseurStrategy(SoccerStrategy) :
    def __init__(self):
        self.name = "defenseurStrategy"
    def compute_strategy(self, state, player, teamid):
        if((player.position - self.player.position) <= BALL_RADIUS):
            pos = player.position - self.player.position
            shoot = Vector2D.create_random()
            return SoccerAction(pos,shoot)
        else :
            pos = self.player.position
            shoot = Vector2D.create_random()
            return SoccerAction(pos,shoot)
        