import os, time, sys, math, heapq
from collections import deque

##class State:
##    def __init__(self, state, path=[]):
##        self.state = state
##        self.path = path
##        self.cost = len(self.path)

class PriorityQueue:
    """
    Priority Queue Implementation
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def isEmpty(self):
        return len(self.heap) == 0

    def insert(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def deleteMin(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def decreaseKey(self, item, priority):
        """
        Replaces a repeated item with the minimum cost
        """
        for i in xrange(len(self.heap)):
            if self.heap[i][2] == item:
                break

        isLast = i == len(self.heap) - 1
        if self.heap[i][0] > priority:
            self.heap[i] = self.heap[-1]
            self.heap.pop()
            if not isLast:
                heapq._siftup(self.heap, i)
                heapq._siftdown(self.heap, 0, i)
            self.insert(item, priority)
        
    def __len__(self):
        return len(self.heap)

def manhattanDistance(state):
    manDist = 0
    board = state['board']
    n  = int(math.sqrt(len(board)))
    for i in range(len(board)):
        row_current = i / n
        col_current = i % n
        row_goal = board[i] / n
        col_goal = board[i] % n
        manDist += abs(row_current - row_goal) + abs(col_current - col_goal)
    return manDist

def f(state, h):
    return state['depth'] + h(state)

def getMem():
    if os.name == 'posix':
        import resource
        max_ram_usage = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
    else:
        try:
            import psutil
            max_ram_usage = psutil.Process(os.getpid()).memory_info().rss / 2.**20
        except:
            max_ram_usage = 0
    
    return max_ram_usage

def GetNeighbors(state):
    neighbors = []
    board = state['board']
    n  = int(math.sqrt(len(board)))
    depth = state['depth'] + 1
    idx1 = board.index(0)
    
    # Up
    idx2 = idx1 - n
    if idx2 >= 0:
        upState = board[:]
        upState[idx1], upState[idx2] = upState[idx2], upState[idx1]
        neighbors.append({'board':upState, 'parent':state, 'depth':depth, 'move':'Up'})

    # Down
    idx2 = idx1 + n
    if idx2 < n*n:
        downState = board[:]
        downState[idx1], downState[idx2] = downState[idx2], downState[idx1]
        neighbors.append({'board':downState, 'parent':state, 'depth':depth, 'move':'Down'})

    # Left
    if idx1 % n != 0:
        idx2 = idx1 - 1
        leftState = board[:]
        leftState[idx1], leftState[idx2] = leftState[idx2], leftState[idx1]
        neighbors.append({'board':leftState, 'parent':state, 'depth':depth, 'move':'Left'})

    # Right
    if idx1 % n != n - 1:
        idx2 = idx1 + 1
        rightState = board[:]
        rightState[idx1], rightState[idx2] = rightState[idx2], rightState[idx1]
        neighbors.append({'board':rightState, 'parent':state, 'depth':depth, 'move':'Right'})

    return neighbors

##    def __cmp__(self, x):
##        return self.state == x.state
            
def SolveBFS(initialState):
    start = time.clock()
    goal = [i for i in range(len(initialState))]
    
    frontier = deque()
    frontier.append({'board':initialState, 'parent':None, 'depth':0, 'move':None})
    # duplicate frontier as a 'set' to avoid the O(N) issue
    stateStr = ''.join(str(e) for e in initialState)
    duplicate_frontier = set()
    duplicate_frontier.add(stateStr)
    
    explored = set()
    
    nodes_expanded = 0
    max_fringe_size = 1
    max_search_depth = 0
    while frontier:
        fringe_size = len(frontier)
        if fringe_size > max_fringe_size:
            max_fringe_size = fringe_size
            
        state = frontier.popleft()
        
        boardStr = ''.join(str(e) for e in state['board'])
        duplicate_frontier.remove(boardStr)
        explored.add(boardStr)
        
        if state['board'] == goal:
            break

        neighbors = GetNeighbors(state)

        if neighbors:
            nodes_expanded += 1
        
        for neighbor in neighbors:
            boardStr = ''.join(str(e) for e in neighbor['board'])
            if boardStr not in duplicate_frontier:
                if boardStr not in explored:
                    frontier.append(neighbor)
                    duplicate_frontier.add(boardStr)
                    depth = neighbor['depth']
                    if depth > max_search_depth:
                        max_search_depth = depth

    end = time.clock()
    running_time = end - start
    
    path = []
    search_depth = state['depth']
    while state['parent'] != None:
        path.insert(0, state['move'])
        state = state['parent']
    fringe_size = len(frontier)
    
    max_ram_usage = getMem()

    OutputToFile(path, nodes_expanded, fringe_size, max_fringe_size, search_depth, \
                 max_search_depth, running_time, max_ram_usage)

def SolveDFS(initialState):
    start = time.clock()
    goal = [i for i in range(len(initialState))]
    
    frontier = deque()
    frontier.append({'board':initialState, 'parent':None, 'depth':0, 'move':None})
    # duplicate frontier as a 'set' to avoid the O(N) issue
    stateStr = ''.join(str(e) for e in initialState)
    duplicate_frontier = set()
    duplicate_frontier.add(stateStr)
    
    explored = set()
    
    nodes_expanded = 0
    max_fringe_size = 1
    max_search_depth = 0
    while frontier:
        fringe_size = len(frontier)
        if fringe_size > max_fringe_size:
            max_fringe_size = fringe_size
            
        state = frontier.pop()
        
        boardStr = ''.join(str(e) for e in state['board'])
        duplicate_frontier.remove(boardStr)
        explored.add(boardStr)
        
        if state['board'] == goal:
            break

        neighbors = GetNeighbors(state)

        if neighbors:
            neighbors.reverse()
            nodes_expanded += 1
        
        for neighbor in neighbors:
            boardStr = ''.join(str(e) for e in neighbor['board'])
            if boardStr not in duplicate_frontier:
                if boardStr not in explored:
                    frontier.append(neighbor)
                    duplicate_frontier.add(boardStr)
                    depth = neighbor['depth']
                    if depth > max_search_depth:
                        max_search_depth = depth

    end = time.clock()
    running_time = end - start
    
    path = []
    search_depth = state['depth']
    while state['parent'] != None:
        path.insert(0, state['move'])
        state = state['parent']
    fringe_size = len(frontier)
    
    max_ram_usage = getMem()

    OutputToFile(path, nodes_expanded, fringe_size, max_fringe_size, search_depth, \
                 max_search_depth, running_time, max_ram_usage)

def SolveAST(initialState, h = manhattanDistance):
    start = time.clock()
    goal = [i for i in range(len(initialState))]
    
    frontier = PriorityQueue()
    frontier.insert({'board':initialState, 'parent':None, 'depth':0, 'move':None}, 0)
    # duplicate frontier as a 'set' to avoid the O(N) issue
    stateStr = ''.join(str(e) for e in initialState)
    duplicate_frontier = set()
    duplicate_frontier.add(stateStr)
    
    explored = set()
    
    nodes_expanded = 0
    max_fringe_size = 1
    max_search_depth = 0
    while not frontier.isEmpty():
        fringe_size = len(frontier)
        if fringe_size > max_fringe_size:
            max_fringe_size = fringe_size
            
        state = frontier.deleteMin()
        
        boardStr = ''.join(str(e) for e in state['board'])
        duplicate_frontier.remove(boardStr)
        explored.add(boardStr)
        
        if state['board'] == goal:
            break

        neighbors = GetNeighbors(state)

        if neighbors:
            nodes_expanded += 1
        
        for neighbor in neighbors:
            boardStr = ''.join(str(e) for e in neighbor['board'])
            if boardStr not in explored:
                if boardStr not in duplicate_frontier:
                    frontier.insert(neighbor, f(neighbor, h))
                    duplicate_frontier.add(boardStr)
                    depth = neighbor['depth']
                    if depth > max_search_depth:
                        max_search_depth = depth
                else:
                    frontier.decreaseKey(neighbor, f(neighbor, h))

    end = time.clock()
    running_time = end - start
    
    path = []
    search_depth = state['depth']
    while state['parent'] != None:
        path.insert(0, state['move'])
        state = state['parent']
    fringe_size = len(frontier)
    
    max_ram_usage = getMem()

    OutputToFile(path, nodes_expanded, fringe_size, max_fringe_size, search_depth, \
                 max_search_depth, running_time, max_ram_usage)

def SolveIDA(initialState, maxBound = 100, h = manhattanDistance):
    start = time.clock()
    bound = h({'board':initialState})
    goal = [i for i in range(len(initialState))]
    
    solved = False
    
    nodes_expanded = 0
    
    while not solved:
        frontier = deque()
        frontier.append({'board':initialState, 'parent':None, 'depth':0, 'move':None})
        max_fringe_size = 1
        max_search_depth = 0
        while frontier:
            fringe_size = len(frontier)
            if fringe_size > max_fringe_size:
                max_fringe_size = fringe_size
                
            state = frontier.pop()
            
            if state['board'] == goal:
                solved = True
                break

            neighbors = GetNeighbors(state)

            if neighbors:
                neighbors.reverse()
                nodes_expanded += 1
            
            for neighbor in neighbors:
                f_value = f(neighbor, h)
                if f_value <= bound:
                    frontier.append(neighbor)
                    depth = neighbor['depth']
                    if depth > max_search_depth:
                        max_search_depth = depth

        bound += 1
        if bound > maxBound:
            break

    end = time.clock()
    running_time = end - start
    
    path = []
    search_depth = state['depth']
    while state['parent'] != None:
        path.insert(0, state['move'])
        state = state['parent']
    fringe_size = len(frontier)
    
    max_ram_usage = getMem()

    OutputToFile(path, nodes_expanded, fringe_size, max_fringe_size, search_depth, \
                 max_search_depth, running_time, max_ram_usage)

def OutputToFile(path, nodes_expanded, fringe_size, max_fringe_size, search_depth, \
                 max_search_depth, running_time, max_ram_usage):
    output = open("output.txt", "w")
    output.write('path_to_goal: {}\n'.format(path))
    output.write('cost_of_path: {}\n'.format(len(path)))
    output.write('nodes_expanded: {}\n'.format(nodes_expanded))
    output.write('fringe_size: {}\n'.format(fringe_size))
    output.write('max_fringe_size: {}\n'.format(max_fringe_size))
    output.write('search_depth: {}\n'.format(search_depth))
    output.write('max_search_depth: {}\n'.format(max_search_depth))
    output.write('running_time: {}\n'.format(running_time))
    output.write('max_ram_usage: {}\n'.format(max_ram_usage))
    output.close()
    
if __name__ == '__main__':
    method = sys.argv[1]
    initialState = [int(x) for x in sys.argv[2].split(',')]

    #method = 'ida'
    # test case 2
    #initialState = [1,2,5,3,4,0,6,7,8]
    # test case 1
    #initialState = [3,1,2,0,4,5,6,7,8]
    
    #initialState = [1,8,5,4,3,0,6,7,2]
    # additional test case
    #initialState = [3,1,2,4,7,0,6,8,5]
    #initialState = [0,1,3,2]
    if method == 'bfs':
        SolveBFS(initialState)
    elif method == 'dfs':
        SolveDFS(initialState)
    elif method == 'ast':
        SolveAST(initialState)
    elif method == 'ida':
        SolveIDA(initialState)
    
