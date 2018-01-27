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
                #return (None, heuristic(state))

	children = state.children(False)
	if len(children) == 0:
		return (None, state.getScore())
                #return (None, heuristic(state))

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
                #return (None, heuristic(state))

	children = state.children()
	if len(children) == 0:
		return (None, state.getScore())
                #return (None, heuristic(state))

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
	#availableCells = len(state.grid.getAvailableCells())

	r = 0.5
	score1 = state.grid.map[3][0] + state.grid.map[3][1]*r
	score1 += state.grid.map[3][2]*r**2 + state.grid.map[3][3]*r**3
	score1 += state.grid.map[2][3]*r**4 + state.grid.map[2][2]*r**5 + state.grid.map[2][1]*r**6
	score1 += state.grid.map[2][0]*r**7 + state.grid.map[1][0]*r**8 + state.grid.map[1][1]*r**9
	score1 += state.grid.map[1][2]*r**10 + state.grid.map[1][3]*r**11 + state.grid.map[0][3]*r**12
	score1 += state.grid.map[0][2]*r**13 + state.grid.map[0][1]*r**14 + state.grid.map[0][0]*r**15
	
	score2 = state.grid.map[3][0] + state.grid.map[2][0]*r
	score2 += state.grid.map[1][0]*r**2 + state.grid.map[0][0]*r**3
	score2 += state.grid.map[0][1]*r**4 + state.grid.map[1][1]*r**5 + state.grid.map[2][1]*r**6
	score2 += state.grid.map[3][1]*r**7 + state.grid.map[3][2]*r**8 + state.grid.map[2][2]*r**9
	score2 += state.grid.map[1][2]*r**10 + state.grid.map[0][2]*r**11 + state.grid.map[0][3]*r**12
	score2 += state.grid.map[1][3]*r**13 + state.grid.map[2][3]*r**14 + state.grid.map[3][3]*r**15
	#return maxTile + 10*max(score1, score2) + 3*availableCells
	return max(score1, score2)

def heuristic1(state):
	#maxTile = state.grid.getMaxTile()
	#availableCells = len(state.grid.getAvailableCells())

        m = state.grid.map
	score1 = m[3][0]      + m[3][1]*w[1] + m[3][2]*w[2] + m[3][3]*w[3] + \
                 m[2][3]*w[4] + m[2][2]*w[5] + m[2][1]*w[6] + m[2][0]*w[7] + \
                 m[1][0]*w[8] + m[1][1]*w[9] + m[1][2]*w[10]+ m[1][3]*w[11]+ \
                 m[0][3]*w[12]+ m[0][2]*w[13]+ m[0][1]*w[14]+ m[0][0]*w[15]
	
	score2 = m[3][0]      + m[2][0]*w[1] + m[1][0]*w[2] + m[0][0]*w[3] + \
                 m[0][1]*w[4] + m[1][1]*w[5] + m[2][1]*w[6] + m[3][1]*w[7] + \
                 m[3][2]*w[8] + m[2][2]*w[9] + m[1][2]*w[10]+ m[0][2]*w[11]+ \
                 m[0][3]*w[12]+ m[1][3]*w[13]+ m[2][3]*w[14]+ m[3][3]*w[15]

	score = max(score1, score2)
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


	
