from numpy import *
import matplotlib.pyplot as plt
import scipy.linalg
import sys

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
        function to initialize a particle within a given range, and also to store the constants for the particle.

        NOTE: this implementation assumes that all the variables of the problem will lie within a common range provided
        in the bounds, if this is not true, you may have to modify this feature.

        :param w: inertia weight of the particle
        :param c1: constant 1 for controlling velocity update
        :param c2: constant 2 for controlling velocity update
        :param dimension: dimension of the vector, viz, number of variables in the problem
        :param bounds: [lower-bound, upper-bound] within which the particle must lie
        """
        self.position = random.uniform(low=bounds[0], high=bounds[1], size=dimension) # randomly initialize start pos
        self.velocity = random.uniform(low=bounds[0], high=bounds[1], size=dimension) # randomly initialize start vel
        self.pbest = self.position # initially the first position will be best position of the particle

