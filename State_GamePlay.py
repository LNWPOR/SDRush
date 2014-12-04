from StateController import *
from MyClock import MyClock
from MySprite import MySprite
from MySound import MySound
from Enemy1 import Enemy1
from Enemy2 import Enemy2
from Enemy3 import Enemy3
from MyScore import MyScore

class State_GamePlay(StateBase):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		StateBase.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.initMap(gameDisplay)
		self.themeSound = MySound("res/sounds/gamePlayTheme.ogg")
		self.enemy1Num = 2
		self.enemy2Num = 2
		self.enemy3Num = 2
		self.myClockRef = MyClock(FPS)
		self.setUpState(gameDisplay,gameWidth,gameHeight,FPS)
		self.cPlayerDead = 0
		self.myScoreRef = MyScore()

	def renderState(self):
		self.renderMap()
		self.renderEnemy()
		self.renderPlayer()

	def updateState(self):
		self.myClockRef.update()
		self.playThemeSound(self.themeSound)
		self.updatePlayer()
		if self.summonEnemy or self.myClockRef.isSec(5):
			self.summonEnemy = True
			self.updateEnemy()
			self.checkCollide()
		self.updateScore()
		self.checkGameOver(self.gameDisplay, self.gameWidth,self.gameHeight,self.FPS)

	def checkGameOver(self,gameDisplay, gameWidth, gameHeight, FPS):
		cPlayerDead = 0
		for player in self.playerList:
			if player.HP < 0 :
				cPlayerDead += 1
				if cPlayerDead == len(self.playerList):
					self.setUpState(gameDisplay, gameWidth, gameHeight, FPS)
					self.themeSound.stop()
					self.setCurrentStateID(self.nextStateId)
	def initSP(self,gameDisplay):
		pass

	def renderMapLayer(self,mapLayerList,mapLayerPosXList,mapLayerPosYList,speed):
		mapLayerList[0].renderImg(mapLayerPosXList[0],mapLayerPosYList[0])
		mapLayerList[1].renderImg(mapLayerPosXList[1],mapLayerPosYList[1])
		
		for i in range(len(mapLayerPosXList)):
			mapLayerPosXList[i] -= speed
			if mapLayerPosXList[i] < -2*self.gameWidth:
				mapLayerPosXList[i] = 2*self.gameWidth-speed

	def initMap(self,gameDisplay):
		self.fadeOutBG = MySprite(gameDisplay,"res/images/fadeOut.png")
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

	def renderMap(self):
		self.renderMapLayer(self.map1Layer2List,self.map1Layer2PosXList,self.map1Layer2PosYList,1)
		self.renderMapLayer(self.map1Layer1List,self.map1Layer1PosXList,self.map1Layer1PosYList,2)
		self.renderFadeIn()

	def renderFadeIn(self):
		self.fadeOutBG.setFadeOutImg(10)
		self.fadeOutBG.renderImgConvert(0, 0)

	def initEnemy(self,gameDisplay,gameWidth,gameHeight,FPS):
		self.enemyList = []
		self.enemyBeamList = []
		for i in range(self.enemy1Num):
			enemy1Ref = Enemy1(gameDisplay,gameWidth,gameHeight,FPS)
			self.enemyList.append(enemy1Ref)
			self.enemyBeamList.append(enemy1Ref.beam)

		for i in range(self.enemy2Num):
			enemy2Ref = Enemy2(gameDisplay,gameWidth,gameHeight,FPS)
			self.enemyList.append(enemy2Ref)
			self.enemyBeamList.append(enemy2Ref.beam)	

		for i in range(self.enemy3Num):
			enemy3Ref = Enemy3(gameDisplay,gameWidth,gameHeight,FPS)
			self.enemyList.append(enemy3Ref)
			self.enemyBeamList.append(enemy2Ref.beam)

	def renderEnemy(self):
		for enemy in self.enemyList:
			enemy.render()

	def updateEnemy(self):
		for enemy in self.enemyList:
			enemy.update()

	def checkCollidePlayerAndEnemy(self):
		for player in self.playerList:
			for sp in player.SPList:
				for enemy in self.enemyList:
					if sp.isCollide(enemy.SP):
						if player.currentMotion == 5:
							enemy.HPdamage(player.power)
						else:
							player.HPdamage(enemy.power)

	def checkCollidePlayerAndEnemyBeam(self):
		for player in self.playerList:
			for sp in player.SPList:
				for beam in self.enemyBeamList:
					if sp.isCollide(beam.enemyBeamSP):
						player.HPdamage(beam.power)

	def checkCollidePlayerBeamAndEnemy(self):
		for player in self.playerList:
			for beam in player.beamList:
				for enemy in self.enemyList:
					if beam.beamSP.isCollide(enemy.SP):
						enemy.HPdamage(beam.power)
						player.score += enemy.score

	def checkCollide(self):
		self.checkCollidePlayerAndEnemy()
		self.checkCollidePlayerAndEnemyBeam()
		self.checkCollidePlayerBeamAndEnemy()		

	def renderPlayer(self):
		for player in self.playerList:
			player.render()

	def updatePlayer(self):
		for player in self.playerList:
			player.update()

	def initPlayer(self):
		pass

	def setUpState(self,gameDisplay,gameWidth,gameHeight,FPS):
		self.initPlayer(gameDisplay, gameWidth, gameHeight, FPS)
		self.initEnemy(gameDisplay,gameWidth,gameHeight,FPS)
		self.summonEnemy = False

	def updateScore(self):
		pass