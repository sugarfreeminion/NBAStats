#Filename: Player.py

class Player:
    def __init__(self):
        self.playerName = []
        self.playerID = []
        
    def PlayerInfo(self,playerID, playerName):
        self.playerName = playerName
        self.playerID = playerID
