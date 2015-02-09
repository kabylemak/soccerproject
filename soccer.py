# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
/users/Etu4/3302744/.spyder2/.temp.py
"""
from soccersimulator import Vector2D
from soccersimulator import SoccerAction 
from soccersimulator import SoccerStrategy
from soccersimulator import SoccerPlayer
from soccersimulator import SoccerTeam
from soccersimulator import SoccerBall
from soccersimulator import SoccerState, pyglet, SoccerBattle, PygletObserver


class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        pos = Vector2D.create_random()
        shoot = Vector2D.create_random()
        return SoccerAction(pos,shoot)
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()
################################################################################################################
class FonceurStrategy(SoccerStrategy):
    def __init__(self , name):
        self.name ="fonceur"
        self.pos = Vector2D()
        self.shoot = Vector2D()
    def start_battle(self,state):
        pass
    def finish_battle(self,won) :
        pass
    def compute_strategy(self,state,player,teamid) :
        self.pos = state.ball.position - player.position 
        self.shoot = Vector2D().create_random() 
        return SoccerAction(self.pos, self.shoot)
  
############################################################################################"
class DefenseurStrategy(SoccerStrategy):
    def __init__(self,name) :
        self.name = "defenseur"
     def start_battle(self,state):
        pass
    def finish_battle(self,won) :
        pass
    def compute_strategy(self,state,player,teamid) :
        self.position = state.ball.position - player.position 
        if (self.position > 2*(PLAYER_RADIUS + BALL_RADIUS)) :
            if(self.teamid == 1) :
                point = Vector2D(GAME_WIDTH/4.,state.ball.position.y)
                dir = point-player.position
                    if(self.position < GAME_WIDTH):
                        pos = Vector2D(GAME_WIDTH/4.-state.ball.position.x, state.ball.position.y)
                        direction = pos - player.position
                        tir = 
                        return SoccerAction(direction,tir)
                        
            if (self.teamid == 2) :
                return SoccerAction(Vector2D(self.width*(3/4),self.height),Vector2D(self.width*(3/4),self.height))
            raise SoccerStateException("compute_strategy : team demandé != 1 ou 2 : %s" % i)
   
##################################################################################################
class GoalStrategy(SoccerStrategy):
    def __init__(self,name):
        self.name = "goal"
    def start_battle(self, state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        if(self.teamid == 1) :
            self.shoot = 
            self.pos = Vector2D(0,state.ball.position.y-state.ball.position.y *self.shoot.y/self.shoot.x)
            
        
        
            
        
        
                
        
        


