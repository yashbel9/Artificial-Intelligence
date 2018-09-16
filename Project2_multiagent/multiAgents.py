
# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        ghostPosition = newGhostStates[0].getPosition()
        foodPos = newFood.asList()
        "*** YOUR CODE HERE ***"
        #print newScaredTimes
        #print successorGameState.getScore()
        newscore=successorGameState.getScore()
    	ghostDist=util.manhattanDistance(newPos, ghostPosition)
    	if ghostDist > 0:
    		newscore -= 10.0/ghostDist
    	foodDist = [util.manhattanDistance(newPos, x) for x in newFood.asList()]
    	if len(foodDist):
    		newscore += 10.0/min(foodDist)
        return newscore

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
    	
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(0)
        v=-99999.00
        for action in actions:
        	minv=v
        	v=max(v, self.minvalue(gameState.generateSuccessor(0,action),0,1))
        	if v>minv:
        		actionsTaken=action
        return actionsTaken		   
        
    def maxvalue(self, gameState, depth):
    	if self.depth==depth or gameState.isLose()==True or gameState.isWin()==True:
    		return self.evaluationFunction(gameState)
    	v=-99999.00
    	actions = gameState.getLegalActions(0)
    	for action in actions:
    		v=max(v,self.minvalue(gameState.generateSuccessor(0,action), depth, 1))
    	return v
    	
    def minvalue(self, gameState, depth, ghostIndex):
    	if self.depth==depth or gameState.isLose()==True or gameState.isWin()==True:
    		return self.evaluationFunction(gameState)
    	v=99999.00
    	actions = gameState.getLegalActions(ghostIndex)
    	for action in actions:
    		if (ghostIndex==gameState.getNumAgents()-1):
    			v=min(v,self.maxvalue(gameState.generateSuccessor(ghostIndex,action), depth+1))
    		else:
    			v=min(v,self.minvalue(gameState.generateSuccessor(ghostIndex,action), depth, ghostIndex+1))
    	return v
        #util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(0)
        beta=99999.00
        alpha=-99999.00
        v=-99999.00
        best = None
        for action in actions:
        	tmp= self.minvalue(gameState.generateSuccessor(0,action),0,1,alpha,beta)
        	if tmp>v:
        		v=tmp
        		best=action
        	if tmp>beta:
        		return best
        	alpha=max(alpha,tmp)
        return best	
        util.raiseNotDefined()
        
    def maxvalue(self, gameState, depth, alpha, beta):

    	if self.depth==depth or gameState.isLose()==True or gameState.isWin()==True:
    		return self.evaluationFunction(gameState)
    	v=-99999.00
    	actions = gameState.getLegalActions(0)
    	for action in actions:
    		v=max(v,self.minvalue(gameState.generateSuccessor(0,action), depth, 1,alpha,beta))
    		if v > beta:
    			return v;
    		alpha = max(alpha,v)
    	return v
    	
    def minvalue(self, gameState, depth, ghostIndex, alpha, beta):
      	if self.depth==depth or gameState.isLose()==True or gameState.isWin()==True:
    		return self.evaluationFunction(gameState)
    	v=99999.00
    	actions = gameState.getLegalActions(ghostIndex)
    	for action in actions:
    		if (ghostIndex==gameState.getNumAgents()-1):
    			v=min(v,self.maxvalue(gameState.generateSuccessor(ghostIndex,action), depth+1,alpha,beta))
    		else:
    			v=min(v,self.minvalue(gameState.generateSuccessor(ghostIndex,action), depth, ghostIndex+1,alpha,beta))
    		if v<alpha:
    			return v;
    		beta = min(beta,v)
    	return v

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        actions = gameState.getLegalActions(0)
        v=-99999.00
        successors = [gameState.generateSuccessor(0, action) for action in actions]
        allvalues = [self.expecti(successor, 0, 1) for successor in successors]
        actionnode = []
        for i in range(len(allvalues)):
        	if allvalues[i] == max(allvalues):
        		actionnode = actions[i]
        return actionnode		   
        
    def maxvalue(self, gameState, depth):
    	if self.depth==depth or gameState.isLose()==True or gameState.isWin()==True:
    		return self.evaluationFunction(gameState)
    	#v=-99999.00
    	actions = gameState.getLegalActions(0)
    	successors = [gameState.generateSuccessor(0, action) for action in actions]	
    	allvalues = [self.expecti(successor, depth, 1) for successor in successors]
    	return max(allvalues)
    	
    def expecti(self, gameState, depth, ghostIndex):
    	if self.depth==depth or gameState.isLose()==True or gameState.isWin()==True:
    		return self.evaluationFunction(gameState)
    	#v=99999.00
    	actions = gameState.getLegalActions(ghostIndex)
    	successors = [gameState.generateSuccessor(ghostIndex, action) for action in actions]
    	if ghostIndex == gameState.getNumAgents()-1:
    		allvalues=[self.maxvalue(successor, depth+1) for successor in successors]
    	else:
    		allvalues=[self.expecti(successor, depth, ghostIndex+1) for successor in successors]
    	average=sum(allvalues)/len(allvalues)
    	return average
		
def newEval(minFood,maxGhost):
	muliplier=1
    	if minFood == 0:
    		muliplier=0
    		minFood = 10.0
    	if maxGhost == 0:
    		muliplier=0
    		maxGhost = 10.0
    	return muliplier*(25.0/maxGhost)# - (10.0/minFood)*muliplier
def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    
    #util.raiseNotDefined()
    maxGhost = 0
    minFood = 0
    #successorGameState = currentGameState.generatePacmanSuccessor(action)

    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    ghostPositionList = [g.getPosition() for g in newGhostStates]
    foodPos = newFood.asList()
    newscore=currentGameState.getScore()
    ghostDistList=[util.manhattanDistance(newPos, x) for x in ghostPositionList]
    #if ghostDist > 0:
     #   newscore -= 10.0/ghostDist
    foodDist = [util.manhattanDistance(newPos, x) for x in newFood.asList()]
    if len(foodDist):
        minFood = min(foodDist)
   	
   	if len(ghostPositionList):
   		maxGhost = max(ghostDistList)
    
    return newscore + newEval(minFood,maxGhost)

    

# Abbreviation
better = betterEvaluationFunction

