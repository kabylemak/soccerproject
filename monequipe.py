from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import RandomStrategy
from main import * 
from soccer import *

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("Ayew",FonceurStrategy()))
team1.add_player(SoccerPlayer("Asamoah",RandomStrategy()))
team2.add_player(SoccerPlayer("Gerrard",DefenseurStrategy())
team2.add_player(SoccerPlayer("Sturridge",FonceurStrategy())

teams =[team1,team2]


"""teams =[team1,team1.copy()]"""
