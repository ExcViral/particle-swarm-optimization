from numpy import *
import matplotlib.pyplot as plt
import scipy.linalg
import sys

from particle import *

class Swarm:
    """
    This class is an implementation of the swarm in particle swarm implementation.

    PSO is initialized with a group (swarm) of random particles (solutions) and then searches for optima by updating
    generations.

    In every iteration, each particle is updated by following two "best" values. The first one is the best solution
    (fitness) it has achieved so far. (The fitness value is also stored.) This value is called pbest. Another "best"
    value that is tracked by the particle swarm optimizer is the best value, obtained so far by any particle in the
    population. This best value is a global best and called gbest.

    """

    def __init__(self, population_size, dimension, maxiterations, bounds, w, c1, c2, mode):
        """
        Function to initialize the swarm, and store the constant parameters

        :param population_size: number of particles in the population
        :param dimension: number of variables in each particle
        :param bounds: [lower-bound, upper-bound] range of the variables, assuming each variable has same domain bounds
        :param w: inertia weight of the particle
        :param c1: constant 1 for controlling velocity update
        :param c2: constant 2 for controlling velocity update
        """
        # initialize global variables
        self.allGbests = []  # list to store all the gbests till some iteration

        # initialize population
        self.swarm = []
        for i in range(population_size):
            self.swarm.append(Particle(w, c1, c2, dimension, bounds))

        # initialize gbest
        self.gbest = self.updateGbest(self.swarm, mode)


    def updateGbest(self, population, mode):
        """
        This function finds the global best position any particle from the population has achieved.

        :param population: population (swarm) containing particles
        :param mode: mode indicates whether the problem is to be minimized or maximized
        :return: gbest
        """

        # initially assign the first particle's position as global best position
        gbest = population[0].position
        gbestFitness = self.fitness(gbest)
        # now look through all the remaining members, check their fitnesses, and update gbest accordingly
        for i in range(1, len(population)):
            currentPosition = population[i].position
            currentPosFitness = self.fitness(currentPosition)
            if mode == "min":
                if currentPosFitness < gbestFitness:
                    gbest = currentPosition
                    gbestFitness = currentPosFitness
                    break
            elif mode == "max":
                if currentPosFitness > gbestFitness:
                    gbest = currentPosition
                    gbestFitness = currentPosFitness
                    break
            else:
                raise Exception(mode, "is not a valid parameter, accepted parameters: 'min' or 'max'")

        self.allGbests.append(gbest)  # append gbest to allGbests list
        return gbest

    def checknstop(self):
        """
        This function will check if convergence or max iterations has reached, and stop the optimization process. It is
        assumed that the convergence is reached if the value of gbests is not changing over a few iterations.

        :return: True, if convergence is reached, else False
        """
        if len(self.allGbests) > 30:
            self.allGbests.pop(0)
        return self.allGbests[1:] == self.allGbests[:-1]


    def fitness(self, position):
        """
        Function to check the fitness of the particle. The fitness of the particle is the indication of how near the
        position of the particle is to that of the solution.

        :param position: position (solution) whose fitness is to be evaluated
        :return: fitness value of the particle
        """

        # TODO: Implement your fitness function here

        fitness = 0

        return fitness


a = Swarm(10, 2, 500, [-100,100], 1, 0.1, 0.2, "max")