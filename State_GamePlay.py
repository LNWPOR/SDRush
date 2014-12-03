from StateController import *
from MySprite import MySprite
from MySound import MySound

class State_GamePlay(StateBase):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		StateBase.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.initMap(gameDisplay)

	def renderState(self):
		pass

	def updateState(self):
		pass

	def initSP(self,gameDisplay):
		pass

	def renderMap(self,mapLayerList,mapLayerPosXList,mapLayerPosYList,speed):
		mapLayerList[0].renderImg(mapLayerPosXList[0],mapLayerPosYList[0])
		mapLayerList[1].renderImg(mapLayerPosXList[1],mapLayerPosYList[1])
		
		for i in range(len(mapLayerPosXList)):
			mapLayerPosXList[i] -= speed
			if mapLayerPosXList[i] < -2*self.gameWidth:
				mapLayerPosXList[i] = 2*self.gameWidth-speed
		

	def initMap(self,gameDisplay):
		self.initMap1Layer1(gameDisplay)
		self.initMap1Layer2(gameDisplay)

	def initMap1Layer1(self,gameDisplay):
		self.map1Layer1 = MySprite(gameDisplay,"res/images/map1Layer1.png")
		self.map1Layer1List = [self.map1Layer1,self.map1Layer1,self.map1Layer1]
		self.map1Layer1PosXList = [0,2*self.gameWidth]
		self.map1Layer1PosYList = [0,0]

	def initMap1Layer2(self,gameDisplay):
		self.map1Layer2 = MySprite(gameDisplay,"res/images/map1Layer2.png")
		self.map1Layer2List = [self.map1Layer2,self.map1Layer2,self.map1Layer2]
		self.map1Layer2PosXList = [0,2*self.gameWidth]
		self.map1Layer2PosYList = [0,0]