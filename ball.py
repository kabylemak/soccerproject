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
vect = Vector2D(0,1) 
vect1 = Vector2D(1,2)
vect2 = Vector2D(1,3)
v = vect + vect1
v.norm 
v.angle
v.distance(vect)
vect2.random(0,4)
vect1.create_random(1,2)
action = SoccerAction(vect1,vect2)

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


equipe1 = SoccerTeam("équipe1" ) 
equipe2 = SoccerTeam("équipe2")
player1 = SoccerPlayer("joueur1",RandomStrategy())
player2 = SoccerPlayer("joueur2",RandomStrategy())
player3 = SoccerPlayer("joueur3",RandomStrategy())
player4 = SoccerPlayer("joueur4",RandomStrategy())
equipe1.add_player(player1)
equipe2.add_player(player2)
equipe1.add_player(player3)
equipe2.add_player(player4)
battle=SoccerBattle(equipe1,equipe2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()

class FonceurStrategy(SoccerStrategy):
    def _init_(self):
        self.name ="fonceur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won) :
        pass
    def compute_strategy(self,state,player,teamid) :
        acceleration = state.ball.position + 
        


