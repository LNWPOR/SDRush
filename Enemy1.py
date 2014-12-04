from Enemy import*
from Beam1 import Beam1

class Enemy1(Enemy):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Enemy.__init__(self,gameDisplay, gameWidth, gameHeight, FPS)
		self.maxHP = 100
		self.HP = self.maxHP
		self.speed = 6
		self.initSP("res/sprites/enemy1SP.png",2,225,175)
		self.beam = Beam1(gameDisplay,gameWidth,gameHeight)
		self.score = 100