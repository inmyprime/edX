from random import randint
from BaseAI import BaseAI
import time, math
import numpy as np

timeLimit = 0.1

class State:
	def __init__(self, grid, move=None, depth=0):
		self.grid = grid
		self.move = move
		self.depth = depth
		self.score = heuristic(self)
		
	def getScore(self):
				return self.score

	def children(self, isMax=True):
		children = []

		if isMax:
			moves = self.grid.getAvailableMoves()
			for move in moves:
				child = self.grid.clone()
				child.move(move)
				children.append(State(child, move, self.depth + 1))

			children.sort(key=State.getScore, reverse=True)
		else:
			availableCells = self.grid.getAvailableCells()
			if len(availableCells) > 0:
				for cell in self.grid.getAvailableCells():
					child = self.grid.clone()
					child.setCellValue(cell, 2)
					children.append(State(child, self.move, self.depth + 1))
					child = self.grid.clone()
					child.setCellValue(cell, 4)
					children.append(State(child, self.move, self.depth + 1))

			children.sort(key=State.getScore)
		return children
	
def minimize(state, alpha, beta, maxDepth):
	if isTimeUp():
		raise (TimeUpException('Time is up!'))

	if state.depth >= maxDepth:
		return (None, state.getScore())

	children = state.children(False)
	if len(children) == 0:
		return (None, state.getScore())

	(minChild, minUtility) = (None, np.inf)

	for child in children:
		(_, utility) = maximize(child, alpha, beta, maxDepth)
		
		if utility < minUtility:
			(minChild, minUtility) = (child, utility)

		if minUtility <= alpha:
			break
	
		if minUtility < beta:
			beta = minUtility

	return (minChild, minUtility)

def maximize(state, alpha, beta, maxDepth):
	if isTimeUp():
		raise (TimeUpException('Time is up.'))

	if state.depth >= maxDepth:
		return (None, state.getScore())

	children = state.children()
	if len(children) == 0:
		return (None, state.getScore())

	(maxChild, maxUtility) = (None, -np.inf)
	
	for child in children:
		(_, utility) = minimize(child, alpha, beta, maxDepth)

		if utility > maxUtility:
			(maxChild, maxUtility) = (child, utility)

		if maxUtility >= beta:
			break

		if maxUtility > alpha:
			alpha = maxUtility

	return (maxChild, maxUtility)

def decision(state, maxDepth):
	(child, _) = maximize(state, -np.inf, np.inf, maxDepth)
	return child

def heuristic(state):
	#maxTile = state.grid.getMaxTile()
	availableCells = len(state.grid.getAvailableCells())
	#w = [32768,16384,8192,4096,2048,1024,512,256,128,64,32,16,8,4,2,1]
	m = state.grid.map
	score1 = m[3][0]*32768+ m[3][1]*16384 + m[3][2]*8192 + m[3][3]*4096 + \
			m[2][3]*2048 + m[2][2]*1024 + m[2][1]*512 + m[2][0]*256 + \
			m[1][0]*128 + m[1][1]*64 + m[1][2]*32+ m[1][3]*16+ \
			m[0][3]*8+ m[0][2]*4+ m[0][1]*2+ m[0][0]
	
	score2 = m[3][0]*32768+ m[2][0]*16384 + m[1][0]*8192 + m[0][0]*4096 + \
			m[0][1]*2048 + m[1][1]*1024 + m[2][1]*512 + m[3][1]*256 + \
			m[3][2]*128 + m[2][2]*64 + m[1][2]*32+ m[0][2]*16+ \
			m[0][3]*8+ m[1][3]*4+ m[2][3]*2+ m[3][3]

	score = max(score1, score2) * (1 + availableCells/16)
	return score

class TimeUpException (Exception):
	pass

def isTimeUp():
	global start_time
	return time.clock() - start_time >= timeLimit

class PlayerAI(BaseAI):
	def getMove(self, grid):
		global start_time
		start_time = time.clock()

		max_depth = 2
		initial = State(grid)
		best_child = decision(initial, max_depth)
		while True:
			max_depth += 1
			try:
				best_child = decision(initial, max_depth)
			except TimeUpException:
				break
			
		return best_child.move


	
