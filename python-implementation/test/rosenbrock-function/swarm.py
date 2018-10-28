from numpy import *
import matplotlib.pyplot as plt
import scipy.linalg
import sys
import math

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
        self.maxiterations = maxiterations  # maximum number of iterations allowed
        self.mode = mode  # store the mode of the problem

        # initialize population
        self.swarm = []
        for i in range(population_size):
            self.swarm.append(Particle(w, c1, c2, dimension, bounds))

        # initialize gbest
        self.gbest = self.updateGbest(self.swarm)
        # print(self.gbest)

    def optimize(self):
        """
        This function will start the optimization process of PSO.

        -----Steps-----
        Step 1 : evaluate gbest of whole population
        Step 2 : Update particles' velocity
        Step 3 : Update particles' position
        Step 4 : Update pbest of each particle
        Step 5 : Check for convergence, stop and return gbest, if convergence is achieved, else GOTO: Step 1

        :return: gbest - the solution of the optimization process
        """
        for i in range(self.maxiterations):
            # print("Iteration number: ",i)
            self.updateGbest(self.swarm)
            self.allGbests.append(self.gbest)
            # print(self.gbest, self.bestParticle.pbestFitness)

            for j in range(len(self.swarm)):
                self.swarm[j].updateVelocity(self.gbest)
                self.swarm[j].updatePosition()
                self.swarm[j].updatePbest(self.mode)
            if self.checknstop():
                break
        return self.bestParticle.pbestFitness

    def updateGbest(self, population):
        """
        This function finds the global best position any particle from the population has achieved.

        :param population: population (swarm) containing particles
        :param mode: mode indicates whether the problem is to be minimized or maximized
        :return: gbest
        """
        self.bestParticle = population[0]

        for i in range(1, len(population)):
            if population[i].pbestFitness > self.bestParticle.pbestFitness:
                self.bestParticle = population[i]

        self.gbest = self.bestParticle.pbest

    def checknstop(self):
        """
        This function will check if convergence or max iterations has reached, and stop the optimization process. It is
        assumed that the convergence is reached if the value of gbests is not changing over a few iterations.

        :param iteration_number: indicates the current iteration number of the process
        :return: True, if convergence is reached, else False
        """
        if len(self.allGbests) > 50:
            self.allGbests.pop(0)
            return self.allGbests[1:] == self.allGbests[:-1]