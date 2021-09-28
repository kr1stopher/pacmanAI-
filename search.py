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
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState() ============(5,5)
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())   ============True
    print "Start's successors:", problem.getSuccessors(problem.getStartState())  ===========[((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
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
                direction = child[1] #direction to get from parent to child
                nextStep = currentRoute + [direction]
                open.push(node)
                route.push(nextStep)

    return 0 #if it reaches this far the problem did not find the goal state

def breadthFirstSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH


    #from starting point s = problem.getStartState()
    #chose one successor, chose its successor etc etc
    #keep searching until exhausted or goal found
    #stack, queue, priority queue from util functions avail
    open = [problem.getStartState()]
    closed = []
    routeMap = []
    parentMap = {}
    while (open != []):
        current = open[0]

        #if current is goal state exit the loop
        if (problem.isGoalState(current)):
            endGoal = current
            break;
        else:
            children = problem.getSuccessors(current) #get the children of current
            closed.append(open.pop(0)) #move the newly explored current to the closed section
            for kid in children:
                i=0
                j =0
                shouldAdd = True
                while (open != [] and i<len(open)): #check to see if kid is already in open
                    if (open[i] == kid[0]):
                        shouldAdd = False
                    i = i+1
                while (closed != [] and j<len(closed)): #check to see if kid is already in closed
                    if (closed[j] == kid[0]):
                        shouldAdd = False
                    j=j+1
                if shouldAdd:  #add the kid to the right side of open if not already in open or closed
                    open.append(kid[0])
                    parentMap[kid[0]] = current, kid[1] #update parentMap
                if (i== len(children)-1):
                    pass
                    #routeMap.append(kid[1])

    endGoal = (endGoal, "void") #keep everything same format
    while (endGoal[0] != problem.getStartState()):
        if (parentMap[endGoal[0]][1] == 'North'):
            routeMap.insert(0,n)
        if (parentMap[endGoal[0]][1] == 'South'):
            routeMap.insert(0,s)
        if (parentMap[endGoal[0]][1] == 'East'):
            routeMap.insert(0,e)
        if (parentMap[endGoal[0]][1] == 'West'):
            routeMap.insert(0,w)
        #routeMap.append(parentMap[endGoal[0]][1])
        endGoal = parentMap[endGoal[0]]

    return routeMap

    #return [w, s, s, e, s, s, w, w, w, w]
    #return  [s, s, w, s, w, w, s, w] #proper answer

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
