import pygame
from pygame.locals import *
from MyClock import MyClock
from State_Menu import State_Menu
from State_SelectMode import State_SelectMode
from State_GamePlaySingle  import State_GamePlaySingle
from State_GamePlayCoop import State_GamePlayCoop
from State_GameOverSingle import State_GameOverSingle
from State_GameOverCoop import State_GameOverCoop

gameWidth = 1024
gameHeight = 640
FPS = 60
myClockRef = MyClock(FPS)
gameDisplay = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption('SDRush')

def main():
	
	pygame.init()
	gameOver = False
	menuStateRef = State_Menu(gameDisplay,gameWidth,gameHeight,FPS,0)
	selectStateRef = State_SelectMode(gameDisplay,gameWidth,gameHeight,FPS,1)
	singleStateRef = State_GamePlaySingle(gameDisplay,gameWidth,gameHeight,FPS,2)
	coopStateRef = State_GamePlayCoop(gameDisplay,gameWidth,gameHeight,FPS,3)
	gameOverSingleRef = State_GameOverSingle(gameDisplay,gameWidth,gameHeight,FPS,4)
	gameOverCoopRef = State_GameOverCoop(gameDisplay,gameWidth,gameHeight,FPS,5)
	statelst = [menuStateRef,selectStateRef,singleStateRef,coopStateRef,gameOverSingleRef,gameOverCoopRef]
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
