#Filename: Team.py

from Player import *
import sys
import requests
import json

class Team:
    def __init__(self):
        self.teamName = []
        self.teamID = []
        self.wins = []
        self.losses = []
        self.players = {}

    def SetTeamInfo(self,teamName, teamID, w, l):
        self.teamName = teamName
        self.teamID = teamID
        self.wins = w
        self.losses = l

    def AddPlayer(self,playerID, playerName):
        p = Player()
        p.playerID = playerID
        p.playerName = playerName
        self.players[playerName] = p

