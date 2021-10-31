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

import util
import copy

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

def depthFirstSearch(problem):

    from game import Directions

    open = util.Stack() #list of nodes to be explored
    route = util.Stack() #route to that node
    closed = []
    #stacks for the nodes to be explored, and the route that got us there
    open.push(problem.getStartState())
    route.push([])

    while open:   #while there are still open nodes left to explore
        #take the next node and the route that got there
        current = open.pop()
        currentRoute = route.pop()

        if problem.isGoalState(current):
            return currentRoute
        if not current in closed: #check to see if already been explored
            closed.append(current) #add to closed

            children = problem.getSuccessors(current) #explore the current node
            for child in children:
                node = child[0]
                nextMove = child[1] #direction to get from parent to child
                nextStep = currentRoute + [nextMove]

                if not child[0] in closed:
                    open.push(node)
                    route.push(nextStep)

    return 0 #if it reaches this far the problem did not find the goal state

def breadthFirstSearch(problem):
    from game import Directions

    #open, closed, and route
    open = util.Queue()
    route = util.Queue()
    closed = []

    #initialize open and closed
    open.push(problem.getStartState())
    route.push([])

    while open:
        current = open.pop()
        currentRoute = route.pop()

        if problem.isGoalState(current): #if we've reached the goal state return the route
            return currentRoute

        if not current in closed:
            closed.append(current)
            children = problem.getSuccessors(current)

            for child in children: #explore the children of current and add to list
                move = currentRoute + [child[1]]
                node = child[0]
                if not child[0] in closed:
                    open.push(node)
                    route.push(move)

    return 0 #if we reach here no route was found

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    #heuristic = g(n) + h(n) -> g(n) = steps to reach that state, h(n) appoximate distance to goal state
    #treats frontier as a high priority queueu
    #selects the node on the frontier with lowest estimated total distance

    open = util.PriorityQueue()
    cost = 0 #cost of reaching a point, starting with 0
    #queue must be ordered with f(p) = cost(p) + H(P)
    test = util.PriorityQueue()
    #PriorityQueue.push(test,1,1)
    test.push(2,2)
    #open = [start]
    open = util.PriorityQueue()
    closed = {} #dict of closed nodes [keys] and their proirity values f(n) = g(n) + h(n)
    # route = util.PriorityQueue
    route = {} #dict where key will be node and value will be [[route], heuristic]

    #add start state to open & route
    open.push(problem.getStartState(), heuristic(problem.getStartState(), problem))
    route[problem.getStartState()] = [[], heuristic(problem.getStartState(), problem),0]


    i = 0
    while (not open.isEmpty()): #while there are nodes left to explore
        current = open.pop() #take the item with the highest priority
        if (problem.isGoalState(current)): #if current = goal return path to current
            print(route[current][0])
            print(current)
            print(problem.isGoalState(current))
            print("above is the  goal route  returned ")
            #return ['North', 'North', 'West', 'West']
            return route[current][0]
        children = problem.getSuccessors(current) #generate children of current
        for child in children:

            if child[0] in route: #if already in open or close
                if route[current][2] < route[child[0]][2]-1: #if child has already been explored but a better route was found
                    childRoute = copy.deepcopy(route[current])
                    childRoute[0].append(child[1])
                    route[child[0]] = [childRoute[0], heuristic(child[0], problem), childRoute[2]+1]
            elif not child[0] in route: #first time a node has been encountered, add to open and route
                #route1 = copy.deepcopy(route)
                childRoute = copy.deepcopy(route[current])
                #childRoute = route1[current]
                #childRoute = childRoute[0]
                childRoute[0].append(child[1])
                route[child[0]] = [childRoute[0], heuristic(child[0], problem), childRoute[2]+1]
                open.update(child[0], heuristic(child[0], problem)) #update or add child to priority queue

        closed[current] = heuristic(current, problem) #put current to closed

    #return fail
    print("error should  not have reached")
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
