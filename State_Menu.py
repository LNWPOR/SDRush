from StateController import *
from MySprite import MySprite
from MySound import MySound

class State_Menu(StateBase):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		StateBase.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.initSP(gameDisplay)
		self.themeSound = MySound("res/sounds/menuTheme.ogg")

	def renderState(self):
		self.renderSP()

	def updateState(self):

		self.playThemeSound(self.themeSound)
		if pygame.key.get_pressed()[K_SPACE]:
			self.BG.resetCountAndDelay()
			self.themeSound.stop()
			self.setCurrentStateID(1)

	def initSP(self,gameDisplay):
		self.BG = MySprite(gameDisplay,"res/images/menuBG4.png")
		self.spaceTostartBG = MySprite(gameDisplay,"res/sprites/spaceTostartSP.png",2,580,50)
	
	def renderSP(self):
		self.BG.setFadeInImg(1)
		self.BG.renderImgConvert(0,0)
		if self.BG.alpha > 40:
			self.spaceTostartBG.loop(self.gameWidth/2 - 280, self.gameHeight/2 +200,10)