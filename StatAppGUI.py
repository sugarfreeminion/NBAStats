#Filename StatAppGUI.py

import sys
from PyQt4 import QtGui
import csv
import json
import requests
from Team import *

class StatAppGUI(QtGui.QMainWindow):
    def ParseTeamsFile(self,teams):
        with open('Teams.csv','rb') as teamFile:
            teamReader = csv.reader(teamFile, delimiter=',')
            for team in teamReader:
                teams[team[0]] = team[1]

    def __init__(self):
        super(StatAppGUI,self).__init__()

        self.team = Team()

        self.teams = {}

        self.ParseTeamsFile(self.teams)

        '''
        initialize all the gui variables
        '''
        self.cBoxLbl = []
        self.cBoxTeams = []
        self.winLbl = []
        self.lossLbl = []
        self.cBoxPlayerLbl = []
        self.cBoxPlayers = []

        self.CreateGUI()

    def CreateGUI(self):
        self.setGeometry(300,300,300,300)

        self.setWindowTitle('Stats')

        '''
        create a label for the team combo box
        '''
        self.cBoxLbl = QtGui.QLabel("Select Team:",self)
        self.cBoxLbl.move(25,25)

        '''
        create the combo box
        '''
        self.cBoxTeams = QtGui.QComboBox(self)
        for key,val in self.teams.items():
            #print key
            self.cBoxTeams.addItem(key)

        self.cBoxTeams.activated[str].connect(self.TeamComboBoxChange)
        self.cBoxTeams.move(110,25)
    
        self.winLbl = QtGui.QLabel("Wins: ",self)
        self.winLbl.move(25,50)

        self.lossLbl = QtGui.QLabel("Losses: ",self)
        self.lossLbl.move(25,75)

        self.cBoxPlayersLbl = QtGui.QLabel("Players:",self)
        self.cBoxPlayersLbl.move(25,100)

        self.cBoxPlayers = QtGui.QComboBox(self)
        self.cBoxPlayers.activated[str].connect(self.PlayerChange)
        self.cBoxPlayers.move(110,100)

        self.show()

    def TeamComboBoxChange(self,text):
        self.team = Team()
        
        self.cBoxPlayers.clear()

        data = self.RetrieveTeamData(self.teams[str(text)])

        teamHeaders = data['resultSets'][0]['headers']
        playerHeaders = data['resultSets'][1]['headers']
        teamData = data['resultSets'][0]['rowSet']
        playerData = data['resultSets'][1]['rowSet']

        (teamWins, teamLosses) = self.ParseTeamData(teamHeaders,teamData)
        
        self.team.losses = teamLosses
        self.team.teamName = str(text)
        self.team.teamID = self.teams[str(text)]

        self.winLbl.setText(str(teamWins))
        self.lossLbl.setText(str(teamLosses))

        self.ParsePlayerData(playerHeaders,playerData)

    def ParsePlayerData(self, playerHeaders, playerData):
        playerIDLocation = playerHeaders.index('PLAYER_ID')
        playerNameLocation = playerHeaders.index('PLAYER_NAME')

        for p in playerData:
            name = p[playerNameLocation]
            pID = p[playerIDLocation]
            self.team.AddPlayer(pID,name)
            self.cBoxPlayers.addItem(name)

    def ParseTeamData(self,teamHeaders,teamData):
        teamWinsLocation = teamHeaders.index('W')
        teamLossLocation = teamHeaders.index('L')

        teamWins = teamData[0][teamWinsLocation]
        teamLoss = teamData[0][teamLossLocation]

        return (teamWins, teamLoss)

    def RetrieveTeamData(self,teamID):
        teamURL = "http://stats.nba.com/stats/teamplayerdashboard?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&TeamID="+str(teamID)+"&VsConference=&VsDivision="

        response = requests.get(teamURL)
        response.raise_for_status()

        data = json.loads(response.text)

        return data

    def PlayerChange(self,text):
        print "HELLO"
