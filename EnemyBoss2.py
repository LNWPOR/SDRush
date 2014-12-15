from Enemy import*
from Beam3 import Beam3

class EnemyBoss2(Enemy):
	def __init__(self,gameDisplay,gameWidth,gameHeight,FPS):
		Enemy.__init__(self,gameDisplay, gameWidth, gameHeight, FPS)
		self.maxHP = 200
		self.HP = self.maxHP
		self.speed = 13
		self.initSP("res/sprites/enemyBoss2SP.png",2,225,175)
		self.beam = Beam3(gameDisplay,gameWidth,gameHeight)
		self.score = 1000
		self.isBoss = True
		self.randomRebornTime = randint(7,10)