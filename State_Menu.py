from StateController import *
from MySprite import MySprite
class State_Menu(StateBase):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		StateBase.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.BG = MySprite(gameDisplay,"res/images/menuBG4.png")
	def renderState(self):
		self.BG.fadeInImg(0,0,1)
		self.BG.renderImg(0,0)
		
	def updateState(self):
		if pygame.key.get_pressed()[K_1]:
			self.setCurrentStateID(1)
	

