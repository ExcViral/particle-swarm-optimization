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
        self.w = w # storing w as global class variable
        self.c1 = c1 # storing c1 as global class variable
        self.c2 = c2 # storing c2 as global class variable

    def updateVelocity(self, gbest):
        """
        function to update the velocity of the particle according to the following expression:

        Velocity(T+1) = w * Velocity(T) + c1 * random_num1 * (pbest - position) + c2 * random_num2 * (gbest - position)

        :param gbest: global best position of the swarm
        """
        self.velocity = self.w * self.velocity + self.c1 * random.uniform(-0.5, 0.5) * (self.pbest - self.position) \
                        + self.c2 * random.uniform(-0.5, 0.5) * (gbest - self.position)

    def updatePosition(self):
        """
        function to update the position of the particle according to the following expression:

        Position(T+1) = Position(T) + Velocity(T+1)

        NOTE: As you can see from the above expression, the position update has to be made only after the velocity is
        updated, so call this function only after the velocity has been updated.

        :return:
        """
        self.position = self.position + self.velocity