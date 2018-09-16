# Artificial-Intelligence

This repository includes all the projects for the course Artificial Intelligence.

# Project 0

- Add a buyLotsOfFruit(orderList) function to buyLotsOfFruit.py which takes a list of (fruit,pound) tuples and returns the cost of your list. If there is some fruit in the list which doesn't appear in fruitPrices it should print an error message and return None.

# Project 1

- Finding a Fixed Food Dot using Depth First Search
- Implement the breadth-first search (BFS) algorithm in the breadthFirstSearch function in search.py
- Implement the uniform-cost graph search algorithm
- Implement A* graph search in the empty function aStarSearch
- Implement the CornersProblem search problem in searchAgents.py
- Implement a non-trivial, consistent heuristic for the CornersProblem
- Fill in foodHeuristic in searchAgents.py with a heuristic for the FoodSearchProblem
- Write an agent that always greedily eats the closest dot. ClosestDotSearchAgent is implemented for you in searchAgents.py, but it's missing a key function that finds a path to the closest dot.

# Project 2

- Improve the ReflexAgent in multiAgents.py to play respectably.
- Write an adversarial search agent in the provided MinimaxAgent class stub in multiAgents.py
- Implement alpha-beta pruning for the agent
- Implement the ExpectimaxAgent, which is useful for modeling probabilistic behavior of agents who may make suboptimal choices.
- Write a better evaluation function for pacman in the provided function betterEvaluationFunction.

# Project 3

- Write a value iteration agent in ValueIterationAgent, which has been partially specified for you in valueIterationAgents.py.
- Change only ONE of the discount and noise parameters so that the optimal policy causes the agent to attempt to cross the bridge.
- Choose settings of the discount, noise, and living reward parameters for this MDP to produce optimal policies of several different types
- Write a Q-learning agent, which does very little on construction, but instead learns by trial and error from interactions with the environment through its update(state, action, nextState, reward) method.
- Complete your Q-learning agent by implementing epsilon-greedy action selection in getAction, meaning it chooses random actions an epsilon fraction of the time, and follows its current best Q-values otherwise.
- Run a completely random Q-learner with the default learning rate on the noiseless BridgeGrid for 50 episodes and observe whether it finds the optimal policy.
- Run Q-Learning agent

# Project 4

- Implementing the online belief update for observing new evidence
- Implement the elapseTime method in ExactInference. Your agent has access to the action distribution for any GhostAgent
- Implement the chooseAction method in GreedyBustersAgent in bustersAgents.py. Your agent should first find the most likely position of each remaining (uncaptured) ghost, then choose an action that minimizes the distance to the closest ghost
- Implement the functions initializeUniformly, getBeliefDistribution, and observe for the ParticleFilter class in inference.py. A correct implementation should also handle two special cases. (1) When all your particles receive zero weight based on the evidence, you should resample all particles from the prior to recover. (2) When a ghost is eaten, you should update all particles to place that ghost in its prison cell, as described in the comments of observe. When complete, you should be able to track ghosts nearly as effectively as with exact inference.
- Implement the elapseTime function for the ParticleFilter class in inference.py. When complete, you should be able to track ghosts nearly as effectively as with exact inference.
- Implement a particle filter that tracks multiple ghosts simultaneously. Each particle will represent a tuple of ghost positions that is a sample of where all the ghosts are at the present time.
- Completed the elapseTime method in JointParticleFilter in inference.py to resample each particle correctly for the Bayes net.
