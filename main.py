# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 19:04:42 2015

@author: baskiotisn
"""


from soccersimulator import pyglet
from soccersimulator import PygletObserver
from monequipe import teams
from soccersimulateur import soccerTeam
from soccersimulator import Vector2D
from soccersimulator import SoccerAction 
from soccersimulator import SoccerStrategy
from soccersimulator import SoccerPlayer
from soccersimulator import SoccerTeam
from soccersimulator import SoccerBall
from soccersimulator import SoccerState, pyglet, SoccerBattle
from soccer import *



team1=teams[0]
if len(teams)>1:
    team2=teams[1]
else:
    team2=team1.copy()
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()


