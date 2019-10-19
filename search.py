# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())[0][0]
    # util.raiseNotDefined()

    # This holds the expanded nodes currently explored and corresponding current path
    frontier = util.Stack()
    path = util.Stack()

    # Push initial values to each stack
    frontier.push(problem.getStartState())
    path.push([])

    # Keep track of expanded nodes
    seen = []
    curr_path = []

    if problem.isGoalState(problem.getStartState()):
      return curr_path

    seen.append(problem.getStartState())

    while not frontier.isEmpty():
      curr_node = frontier.pop()
      curr_path = path.pop()

      for node in problem.getSuccessors(curr_node):
        # See if position has been seen before
        if not node[0] in seen:
          # Check if that position is a goal state
          if problem.isGoalState(node[0]):
            return curr_path + [node[1]]

          # Add the expanded node to previously seen  
          seen.append(node[0])
	  seen.append(curr_node)
          frontier.push(node[0])
          path.push(curr_path + [node[1]])
    
    return []


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    # This holds the expanded nodes currently explored and corresponding current path
    frontier = util.Queue()
    path = util.Queue()

    # Push initial values to each queue
    frontier.push(problem.getStartState())
    path.push([])

    # Keep track of expanded nodes
    seen = []
    curr_path = []
    if problem.isGoalState(problem.getStartState()):
      return curr_path

    while not frontier.isEmpty():
      curr_node = frontier.pop()
      curr_path = path.pop()

      #for node in problem.getSuccessors(curr_node):
        ## See if position has been seen before
        #if not node[0] in seen:
          ## Check if that position is a goal state
          #if problem.isGoalState(node[0]):
            #return curr_path + [node[1]]

          ## Add the expanded node to previously seen  
          #seen.append(curr_node)  
          #frontier.push(node[0])
          #path.push(curr_path + [node[1]]) 
      for position, direction, cost in problem.getSuccessors(curr_node):
        if not position in seen:
          if problem.isGoalState(position):
            return curr_path + [direction]

          seen.append(position)
          seen.append(curr_node)
          frontier.push(position)
          path.push(curr_path + [direction])

    return []


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    frontier = util.PriorityQueue()
    # path = util.PriorityQueue()

    frontier.push((problem.getStartState(), []), 0)
    # path.push(([], 0), 0)

    seen = []
    curr_path = []
    if problem.isGoalState(problem.getStartState()):
      return curr_path

    while not frontier.isEmpty():
      f_pop = frontier.pop()
      curr_node = f_pop[0]
      curr_path = f_pop[1]

      # print curr_node
      # print curr_cost
      # print curr_path

      if problem.isGoalState(curr_node):
        return curr_path

      seen.append(curr_node)

      for position, direction, cost in problem.getSuccessors(curr_node): 
        if not position in seen:
          #seen.append(position)
          #seen.append(curr_node)
          total_cost = problem.getCostOfActions(curr_path + [direction])
          frontier.push((position, curr_path + [direction]), total_cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    # util.raiseNotDefined()
    frontier = util.PriorityQueue()
    # path = util.PriorityQueue()

    frontier.push((problem.getStartState(), []), 0)
    # path.push(([], 0), 0)

    seen = []
    curr_path = []
    if problem.isGoalState(problem.getStartState()):
      return curr_path

    while not frontier.isEmpty():
      f_pop = frontier.pop()
      curr_node = f_pop[0]
      curr_path = f_pop[1]

      # print curr_node
      # print curr_cost
      # print curr_path

      if problem.isGoalState(curr_node):
        return curr_path

      seen.append(curr_node)

      for position, direction, cost in problem.getSuccessors(curr_node): 
        if not position in seen:
          total_cost = problem.getCostOfActions(curr_path + [direction]) + heuristic(position, problem)
          frontier.push((position, curr_path + [direction]), total_cost)

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
