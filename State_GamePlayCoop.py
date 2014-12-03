from State_GamePlay import *
from MySprite import MySprite
from MySound import MySound

class State_GamePlayCoop(State_GamePlay):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		State_GamePlay.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)

	def renderState(self):
		self.renderMap(self.map1Layer2List,self.map1Layer2PosXList,self.map1Layer2PosYList,1)
		self.renderMap(self.map1Layer1List,self.map1Layer1PosXList,self.map1Layer1PosYList,2)


	def updateState(self):
		pass
