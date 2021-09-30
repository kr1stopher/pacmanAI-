Author: Kris Swartzbaugh 
CWID: 890939184 
Email: kswartzb@csu.fullerton.edu 


Summary:
	Build general search algorithms and apply them to Pacman scenarios as he  attempts to nagivate his maze world. 



Submitted Contents: 
	(1) README [this fill]
	(2) search.py 
		(a) depthFirstSearch alg 
		(b) breadthFirstSearch alg
	
	
Project Requirements:
	search.py algorithms will be placed here 
	pacman.py - The main file that runs Pacman games. This file describes a Pacman Game State type, which you use in this project.
	game.py - The logic behind how the Pacman world works. This file describes several
supporting types like Agent State, Agent, Direction, and Grid.
	util.py Useful data structures for implementing search algorithms.
	searchAgents.py A variety of different types of Pacman agents. test_cases/ Directory containing the test cases for each question
	
	
	(1) Finding a Fixed food dot using depth search 
		implement the depth-first search (DFS) algorithm in the depthFirstSearch function in search.py 
		Your code should quickly find a solution for:
			python3.6 pacman.py -l tinyMaze -p SearchAgent
			python3.6 pacman.py -l mediumMaze -p SearchAgent
			python3.6 pacman.py -l bigMaze -z .5 -p SearchAgent
		
		
		eg. python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
			above command tells pacman to use tinyMazeSearch as the search agent to find the dot. 
			Search nodes must contain a state but also the information necessary to reconstruct the path (plan) which gets to that state
			Search functions must return a list of actions that will lead the agent from the start to the goal. Actions must be all legal moves (valid directions, no moving through walls)
			use stack, queue, and PriorityQueue data structures provided in util.py (for autograder comtatability)
			
			
	(2) Question 2: Breadth first Search 
		breadthFirstSearch function in search.py
		test code:
			python3.6 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
			python3.6 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
			
			
			
