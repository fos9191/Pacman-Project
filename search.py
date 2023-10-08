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
    #get start state
    actions = []
    start = problem.getStartState()
    current = (start, None)
    frontier = Stack()
    visited = Stack()
    parents = {}
    
    print("start", start)
    #push the first node to the frontier stack
    frontier.push(current)
    
    while not frontier.isEmpty():
        #take the next node from the frontier and put it in the visited list
        current = frontier.pop()
        visited.push(current)
        
        #if we are at the goal state, finish searching
        if problem.isGoalState(current[0]):
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

    
def breadthFirstSearch(problem: SearchProblem):
    frontier = Queue()
    visited = Queue()
    parents = {}
    actions = []
    start = problem.getStartState()
    current = (start, None)
    
    #start by pushing the start location into the frontier
    frontier.push(current)
    
    #while we still have positions to search
    while not frontier.isEmpty():
        current = frontier.pop()
        #if there are other nodes in the frontier that are the same as current, remove them.
        #this is cuz we have already found the fastest path to that node so don't need
        #to expand it again
        for item in frontier.list:
            if item == current:
                frontier.list.remove(item)
        
        visited.push(current)
        
        #if our current state is the goal state then finish searching
        if problem.isGoalState(current[0]):
            break
         
        #get the adjacent nodes from our current node    
        successors = problem.getSuccessors(current[0])
        for position, action, cost in successors:
            pair = (position, action)
            #if the node has already been visited or in the frontier, don't do anything
            if any(position == item[0] for item in visited.list) or any(position == item[0] for item in frontier.list):
                None
            else: #else add the successors to the queue
                frontier.push(pair)
                current = (current[0], action)
                parents[position] = current
    
    #work backwards to reconstruct the correct path   
    while current[0] != start:
        actions.append(parents[current[0]][1])
        next = parents[current[0]]
        current = next
    
    actions.reverse()
    
    return actions
    
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    startState = problem.getStartState()
    frontier = PriorityQueue()
    reached = []    
    
    #create the first node
    startNode = (startState, [], 0)
    frontier.push(startNode, 0)
    
    #while we haven't explored the whole maze
    while not frontier.isEmpty():
        #take the first node from frontier
        node = frontier.pop()
        
        #if it is the goal state then finish searching
        if problem.isGoalState(node[0]):
            return node[1]
        
        #if we havn't reached this node before
        if node[0] not in reached:
            reached.append(node[0])
            
            successors = problem.getSuccessors(node[0])
            
            #create nodes for each of the successors, adding them to the frontier
            for child, action, cost in successors:
                childNode = (child, node[1] + [action], node[2] + cost)
                frontier.push(childNode, childNode[2])           
    
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = PriorityQueue()
    reached = []
    startState = problem.getStartState()
    
    #start node is of the form: position, path to that position, cost of that path
    startNode = (startState, [], 0)
    frontier.push(startNode, heuristic(startState, problem))
    
    while not frontier.isEmpty():
        #take the first node from frontier
        node = frontier.pop()
        
        if problem.isGoalState(node[0]):
            return node[1] # return the path to get to that (goal) node
        
        if node[0] not in reached:
            reached.append(node[0])
            
            successors = problem.getSuccessors(node[0])
            
            #create nodes for each of the successors, adding them to the frontier
            for child, action, cost in successors:
                childNode = (child, node[1] + [action], node[2] + cost + heuristic(child, problem) - heuristic(node[0], problem))
                frontier.push(childNode, childNode[2])

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
