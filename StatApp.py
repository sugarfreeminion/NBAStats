#! /usr/bin/env python

#Filename: StatApp.py

import sys
import requests
import json
import csv
from StatAppGUI import *
from PyQt4.QtGui import *
from Team import *

'''
    Function Name:  RetrieveTeamData
    Description:    gets data from stats.nba.com
                    looks at the teamplayerdashboard
'''
def RetrieveTeamData(teamID):
    team_url = "http://stats.nba.com/stats/teamplayerdashboard?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N&Rank=N&Season=2015-16&SeasonSegment=&SeasonType=Regular+Season&TeamID="+str(teamID)+"&VsConference=&VsDivision=" 
 
    response = requests.get(team_url)
    response.raise_for_status()
    
    data = json.loads(response.text)

    return data

def ParseTeamData(headers,teamData):  
    teamIDLocation = headers.index('TEAM_ID')

    teamID = teamData[0][teamIDLocation]

    teamNameLocation = headers.index('TEAM_NAME')

    teamName = teamData[0][teamNameLocation]

    teamWinsLocation = headers.index('W')

    teamWins = teamData[0][teamWinsLocation]

    teamLossLocation = headers.index('L')

    teamLoss = teamData[0][teamLossLocation]

    return (teamID, teamName, teamWins, teamLoss)

def ParsePlayerData(headers,playerData):
    playerIDLocation = headers.index('PLAYER_ID')
    playerNameLocation = headers.index('PLAYER_NAME')

    playerID = playerData[playerIDLocation]
    playerName = playerData[playerNameLocation]

    return (playerID, playerName)

def main():
    statAppGUIObj = QApplication(sys.argv)
       
    #nbaTeams = []
    #players = {}
    
    #team = Team()

    #nbaTeams = ParseTeamsFile()

    statAppGui = StatAppGUI()

    #selectedTeam = statAppGui.ReturnSelectedTeam();

    #print selectedTeam

    sys.exit(statAppGUIObj.exec_()) 

def t():
    print nbaTeams[0][1]

    data = RetrieveTeamData(nbaTeams[0][1])

    teamHeaders = data['resultSets'][0]['headers']
    playerHeaders = data['resultSets'][1]['headers']
    teamData = data['resultSets'][0]['rowSet']
    playerData = data['resultSets'][1]['rowSet'] 

    (teamID,teamName,teamWins,teamLoss) = ParseTeamData(teamHeaders,teamData)

    for p in playerData:
        (playerID,playerName) = ParsePlayerData(playerHeaders,p)
        team.AddPlayer(playerID,playerName)

    team.SetTeamInfo(teamName,teamID,teamWins,teamLoss)

    print str(team.teamName) + " Info:"
    print "    Wins: " + str(team.wins)
    print "    Losses: " + str(team.losses)

    print "    Players:"
    for players in team.players:
        print "        " + str(players.playerName)

    
if __name__ == "__main__":
    w = main()
