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
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    print("Start:", problem.getStartState())
    a = problem.getStartState()
    print(a, "\n")
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors((5,4)))



    #from starting point s = problem.getStartState()
    #chose one successor, chose its successor etc etc
    #keep searching until exhausted or goal found
    #stack, queue, priority queue from util functions avail
    open = [problem.getStartState()]
    closed = []
    moves = []
    parent = problem.getStartState()
    routeMap = []
    parentMap = {}
    while (open != []):
        current = open[len(open)-1]
        parent = open[len(open)-1]
        #if current is not a child -> remove last direction
        if (problem.isGoalState(current)):
            print("I hit the goalllllllll")
            endGoal = current
            break;
            #return [s, s, w, s, w, w, s, w] #return the path to current
        else:
            children = problem.getSuccessors(current) #get the children of current
            closed.append(open.pop()) #move the newly explored node to the closed section
            for kid in children:  #do I need to reverse this
                i=0
                j =0
                shouldAdd = True
                while (open != [] and i<len(open)):
                    if (open[i] == kid[0]):
                        shouldAdd = False
                    i = i+1
                while (closed != [] and j<len(closed)):
                    if (closed[j] == kid[0]):
                        shouldAdd = False
                    j=j+1
                if shouldAdd:
                    open.append(kid[0])
                    parentMap[kid[0]] = current, kid[1]
                if (i== len(children)-1):
                    pass
                    #routeMap.append(kid[1])

    endGoal = (endGoal, "void") #keep everything same format
    while (endGoal[0] != problem.getStartState()):
        if (parentMap[endGoal[0]][1] == 'North'):
            routeMap.append(n)
        if (parentMap[endGoal[0]][1] == 'South'):
            routeMap.append(s)
        if (parentMap[endGoal[0]][1] == 'East'):
            routeMap.append(e)
        if (parentMap[endGoal[0]][1] == 'West'):
            routeMap.append(w)
        #routeMap.append(parentMap[endGoal[0]][1])
        endGoal = parentMap[endGoal[0]]


    #need to reverse route map, can adjust to using a stack later
    finalRoute = []
    i = len(routeMap)-1
    while (i>=0) :
        finalRoute.append(routeMap[i])
        i=i-1

    return finalRoute
    #return [w, s, s, e, s, s, w, w, w, w]
    #return  [s, s, w, s, w, w, s, w] #proper answer
    """
    open  = [start]
    closed = []
    while open != []
        remove leftmost state from open [x]
            if  x =  goal return successor
            else
                generate children of x
                put x to closed
                discard children of x if already open or closed
                put remaining children on open
            end
        end
        return fail
    end
    """


    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    util.raiseNotDefined()
    """
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
