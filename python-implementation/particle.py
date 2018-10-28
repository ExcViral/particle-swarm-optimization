from numpy import *
import matplotlib.pyplot as plt
import scipy.linalg
import sys
import math


class Particle:
    """
    This class is an implementation of the "particles" in the particle swarm optimization algorithm.

    Every solution in the solution space is called a particle. Philosophically, the particles change their components
    and move/fly in the space, with an intent to reach their destination, which may be food (solution), or anything else.

    Each particle is characterized by a position vector, and a velocity vector.

    Each particle has individual knowledge pbest-its own best-so-far position, and social knowledge gbest-pbest of its
    best neighbours.

    """

    def __init__(self, w, c1, c2, dimension, bounds):
        """
        Function to initialize a particle within a given range, and also to store the constants for the particle.

        NOTE: this implementation assumes that all the variables of the problem will lie within a common range provided
        in the bounds, if this is not true, you may have to modify this feature.

        :param w: inertia weight of the particle
        :param c1: constant 1 for controlling velocity update
        :param c2: constant 2 for controlling velocity update
        :param dimension: dimension of the vector, viz, number of variables in the problem
        :param bounds: [lower-bound, upper-bound] within which the particle must lie
        """
        self.position = random.uniform(low=bounds[0], high=bounds[1], size=dimension)  # randomly initialize start pos
        self.velocity = random.uniform(-0.5, 0.5, size=dimension)  # randomly initialize start velocity
        self.pbest = self.position  # initially the first position will be best position of the particle
        self.pbestFitness = self.fitness(self.pbest)  # store the fitness of the initial best position
        self.w = w  # storing w as global class variable
        self.c1 = c1  # storing c1 as global class variable
        self.c2 = c2  # storing c2 as global class variable
        self.bounds = bounds  # storing bounds for use in update position function
        self.dimension = dimension  # storing dimensions for use in update position function

    def updateVelocity(self, gbest):
        """
        Function to update the velocity of the particle according to the following expression:

        Velocity(T+1) = w * Velocity(T) + c1 * random_num1 * (pbest - position) + c2 * random_num2 * (gbest - position)

        :param gbest: global best position of the swarm
        """
        self.velocity = self.w * self.velocity + (self.c1 * random.uniform(0, 1) * (self.pbest - self.position)) + (
                    self.c2 * random.uniform(0, 1) * (gbest - self.position))

    def updatePosition(self):
        """
        Function to update the position of the particle according to the following expression:

        Position(T+1) = Position(T) + Velocity(T+1)

        NOTE: As you can see from the above expression, the position update has to be made only after the velocity is
        updated, so call this function only after the velocity has been updated.

        :return:
        """
        self.position = self.position + self.velocity

        # TODO: implement custom checking bounds for the updated position here.
        for i in range(len(self.position)):
            if (self.position[i] > self.bounds[1]) or (self.position[i] < self.bounds[0]) :
                self.position[i] = random.uniform(low=self.bounds[0], high=self.bounds[1])

    def updatePbest(self, mode):
        """
        This function checks the fitness of the particle at its current position, and compares it with its previous best
        position, i.e. previous pbest, and updates pbest with current position if current postion is better, else pbest
        is not changed.

        :param mode: mode indicates whether the problem is to be minimized or maximized
        """
        if mode == "min":
            currentPosFitness = self.fitness(self.position)
            if currentPosFitness < self.pbestFitness:
                self.pbest = self.position
                self.pbestFitness = currentPosFitness
                return
        elif mode == "max":
            currentPosFitness = self.fitness(self.position)
            if currentPosFitness > self.pbestFitness:
                self.pbest = self.position
                self.pbestFitness = currentPosFitness
                return
        else:
            raise Exception(mode, "is not a valid parameter, accepted parameters: 'min' or 'max'")

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