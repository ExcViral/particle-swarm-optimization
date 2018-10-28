# We will be testing our PSO implementation on the rosenbrock function for n = 3, and n = 4
# Rosenbrock function for n = 3: [100(x2-x1)^2 + (1-x1)^2]+[100(x3-x2)^2 + (1-x2)^2]
# Rosenbrock function for n = 4: [100(x2-x1)^2 + (1-x1)^2]+[100(x3-x2)^2 + (1-x2)^2]+[100(x4-x3)^2 + (1-x3)^2]
# domain search: -inf < xi < inf

# Problem formulation for three variables, i.e. dimension = 3
# Each particle will have three variables, let's take swarm population size = 10, maxiterations = 10000,
# bounds = [-1000, 1000], w = 1, c1 = 2, c2 = 2, and mode = "min"

from swarm import *

rosenbrock_swarm = Swarm(100, 3, 300000, [-10, 10], 1, 2, 2, "min")

optimal_sol = rosenbrock_swarm.optimize()

print(optimal_sol)

rosenbrock_swarm.plotConvergenceGraph()