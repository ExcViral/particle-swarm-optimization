from particle import *

particles = []

for i in range(10):
    particles.append(Particle(1, 2, 2, 2, [-1, 1]))

for l in range(1000):

    bestParticle = particles[0]

    for i in range(1, len(particles)):
        if particles[i].pbestFitness > bestParticle.pbestFitness:
            bestParticle = particles[i]

    gbest = bestParticle.pbest

    for i in range(len(particles)):
        particles[i].updateVelocity(gbest)
        particles[i].updatePosition()
        particles[i].updatePbest("max")

    print(bestParticle.pbestFitness)
