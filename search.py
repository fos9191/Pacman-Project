# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from util import Stack, Queue, PriorityQueue
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    """
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    #get start state
    actions = []
    start = problem.getStartState()
    current = (start, None)
    frontier = Stack()
    visited = Stack()
    parents = {}
    
    
    #push the first node to the frontier stack
    frontier.push(current)
    print(start)
    
    while not frontier.isEmpty():
        #take the next node from the frontier and put it in the visited list
        current = frontier.pop()
        visited.push(current)
        
        #if we are at the goal state, finish searching
        if problem.isGoalState(current[0]):
            goal = current[0]
            break

        #find its successors. if any are not in the visited list then add them to the frontier
        successors = problem.getSuccessors(current[0])

        #if the successors are not yet in visited, add them
        for position, action, cost in successors:
            pair = (position, action)
            #checks if node / square is already explored
            if any(position == item[0] for item in visited.list):
                None # do nothing
            else: #if its not explored its pushed to the frontier and its parent recorded
                frontier.push(pair)
                current = (current[0], action)
                parents[position] = current
    
    #we have now found the goal, track back through the maze creating the path for pacman to follow
    while current[0] != start:
        actions.append(parents[current[0]][1])
        next = parents[current[0]]
        current = next
    
    #reverse the path so it is from the start to the finish
    actions.reverse() 
        
    return actions
    util.raiseNotDefined()
    
#takes a direction and returns its reverse, use for reverse path finding in maze   
def flipDirection(direction):
    if direction == 'South':
        return 'North'
    elif direction == 'North':
        return 'South'
    elif direction == 'East':
        return 'West'
    elif direction == 'West':
        return 'East'
    else:
        return 'Error'

def directionTaken(positionOne, positionTwo):
    """Takes two positions from the maze and returns the direction from positionOne -> positionTwo"""
    if (positionOne[0] - positionTwo[0] == 1):
        return 'West'
    elif (positionOne[0] - positionTwo[0] == -1):
        return 'East'
    elif (positionOne[1] - positionTwo[1] == 1):
        return 'South'
    elif (positionOne[1] - positionTwo[1] == -1):
        return 'North'
    else: 
        return 'Error'
    
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
