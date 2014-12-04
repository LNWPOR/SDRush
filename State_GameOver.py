from StateController import *
from MySprite import MySprite
from MySound import MySound
from MyScore import MyScore


class State_GameOver(StateBase):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		StateBase.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.themeSound = MySound("res/sounds/gameOverSound.ogg")
		self.myScoreRef = MyScore()

	def renderState(self):
		self.renderSP()
		self.renderScore()

	def updateState(self):

		self.playThemeSound(self.themeSound)
		if pygame.key.get_pressed()[K_6]:
			self.BG.resetCountAndDelay()
			self.themeSound.stop()
			self.setCurrentStateID(0)

	def initSP(self,path):
		self.BG = MySprite(self.gameDisplay,path)
		
	
	def renderSP(self):
		self.BG.setFadeInImg(1)
		self.BG.renderImgConvert(0,0)

	def renderScore(self):
		pass
