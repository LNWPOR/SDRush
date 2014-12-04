from Enemy import*
from Beam2 import Beam2

class Enemy3(Enemy):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Enemy.__init__(self,gameDisplay, gameWidth, gameHeight, FPS)
		self.maxHP = 100
		self.HP = self.maxHP
		self.speed = 10
		self.initSP("res/sprites/enemy3SP.png",2,225,175)
		self.beam = Beam2(gameDisplay,gameWidth,gameHeight)
		self.score = 200