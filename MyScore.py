class  MyScore:
	def __init__(self):
		pass

	def setScoreFreedom(self,currentScore):
		global scoreFreedom
		scoreFreedom = currentScore

	def getScoreFreedom(self):
		return scoreFreedom

	def setScoreJustice(self,currentScore):
		global scoreJustice
		scoreJustice = currentScore

	def getScoreJustice(self):
		return scoreJustice
		


