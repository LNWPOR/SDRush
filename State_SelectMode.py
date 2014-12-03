from StateController import *
from MySprite import MySprite
from MySound import MySound

class State_SelectMode(StateBase):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		StateBase.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.initSP(gameDisplay)
		self.themeSound = MySound("res/sounds/selectModeTheme.ogg")
		self.currentMode = 1

	def renderState(self):
		self.renderSelectMode()


	def updateState(self):
		self.playThemeSound(self.themeSound)
		self.selectMode()

	def selectMode(self):
		if pygame.key.get_pressed()[K_1]:
			self.currentMode = 1
			self.coopModeSP.resetCountAndDelay()
		elif pygame.key.get_pressed()[K_2]:
			self.currentMode = 2
			self.singleModeSP.resetCountAndDelay()

		if self.currentMode == 1 and pygame.key.get_pressed()[K_RETURN]:
			self.singleModeSP.resetCountAndDelay()
			self.themeSound.stop()
			self.setCurrentStateID(2)
		
		if self.currentMode == 2 and pygame.key.get_pressed()[K_RETURN]:
			self.singleModeSP.resetCountAndDelay()
			self.themeSound.stop()
			self.setCurrentStateID(3)

	def renderSelectMode(self):
		if self.currentMode == 1:
			self.singleModeSP.setFadeInImg(10)
			self.singleModeSP.renderImgConvert(0,0)
		elif self.currentMode == 2:
			self.coopModeSP.setFadeInImg(10)
			self.coopModeSP.renderImgConvert(0,0)

	def initSP(self,gameDisplay):
		self.singleModeSP = MySprite(gameDisplay,"res/images/singleMode.png")
		self.coopModeSP = MySprite(gameDisplay,"res/images/coopMode.png")
