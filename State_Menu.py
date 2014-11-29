from StateController import *

class State_Menu(StateBase):


	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS,stateID):
		StateBase.__init__(self,gameDisplay, gameWidth, gameHeight,FPS,stateID)
		self.BG = pygame.image.load("res/images/menuBG.png")
		
	def renderState(self):
		self.gameDisplay.blit(self.BG,(0,0))
	
	def updateState(self):
		if pygame.key.get_pressed()[K_1]:
			self.setCurrentStateID(1)
			
