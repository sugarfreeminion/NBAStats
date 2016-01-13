#Filename: Player.py

class Player:
    def __init__(self):
        self.playerName = []
        self.playerID = []
        self.gamesPlayed = []
        self.reb = []
        self.ast = []
        self.stl = []
        self.blk = []
        self.pts = []
        self.plusMinus = []
        
    def PlayerInfo(self,playerID, playerName):
        self.playerName = playerName
        self.playerID = playerID

    def GamesPlayed(self,gp):
        if gp is not None:
            self.gamesPlayed = gp
        else:
            print "Games Played error"

    def Rebounds(self,rebounds):
        if rebounds is not None:
            self.reb = rebounds
        else:
            print "Rebounds error"

    def SetPlayerInfo(self,data):
        if data is not None:
            playerHeaders = data['resultSets'][1]['headers']
            playerData = data['resultSets'][1]['rowSet']

            playerGPLoc = playerHeaders.index('GP')
            playerREBLoc = playerHeaders.index('REB')
            playerASTLoc = playerHeaders.index('AST')
            playerSTLLoc = playerHeaders.index('STL')
            playerBLKLoc = playerHeaders.index('BLK')
            playerPTSLoc = playerHeaders.index('PTS')
            playerPMLoc = playerHeaders.index('PLUS_MINUS')

            self.gamesPlayed = playerData[0][playerGPLoc]
            self.reb = playerData[0][playerREBLoc]
            self.ast = playerData[0][playerASTLoc]
            self.stl = playerData[0][playerSTLLoc]
            self.blk = playerData[0][playerBLKLoc]
            self.pts = playerData[0][playerPTSLoc]
            self.plusMinus = playerData[0][playerPMLoc]
