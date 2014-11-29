import pygame
from pygame.locals import *
from MyClock import MyClock
from State_Menu import State_Menu
gameWidth = 1280
gameHeight = 720
FPS = 30
myClockRef = MyClock(FPS)
gameDisplay = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption('SDRush')

def main():
	
	pygame.init()
	gameOver = False
	menuStateRef = State_Menu(gameDisplay,gameWidth,gameHeight,FPS,0)
	
	statelst = [menuStateRef]
	#--------------------------------------------------------------------
	while not gameOver:
		for state in statelst:
			if state.getID() == state.getCurrentStateID():
				state.updateState()
				state.renderState()
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True

		pygame.display.update()
		myClockRef.update()

main()
pygame.quit()