import pygame
from pygame.locals import *

class MyClock:
	def __init__(self,FPS):
		self.clock = pygame.time.Clock()
		self.FPS = FPS
		self.currentTime = 0
		self.oneSec = 0
		self.countSec = 0

	def update(self):
		self.clock.tick(self.FPS)
		if self.getTime() - self.currentTime == 1:
			self.oneSec = 1
		else:
			self.oneSec = 0
		self.currentTime = self.getTime()

	def getTime(self):
		return pygame.time.get_ticks()/1000

	def isSec(self,Sec):
		if self.oneSec == 1:
			self.countSec += 1
		if self.countSec >= Sec:
			self.countSec = 0
			return True
