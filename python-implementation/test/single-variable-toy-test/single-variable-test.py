from swarm import *

a = Swarm(10, 1, 1000, [-1, 1], 1, 2, 2, "max")

max = a.optimize()

print(max)