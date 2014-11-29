

class  MyScores:
	def __init__(self,gameDisplay,gameWidth,gameHeight):
		self.scaleScore = 100

	def setGokuScore(self,countPush):
		global gokuScore
		gokuScore = countPush*self.scaleScore

	def setVegetaScore(self,countPush):
		global vegetaScore
		vegetaScore = countPush*self.scaleScore

	def getGokuScore(self):
		return gokuScore

	def getVegetaScore(self):
		return vegetaScore


