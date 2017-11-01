import random
import config


class PidGenome(object):
    def __init__(self, kp, ki, kd):
        self.genome = [kp, ki, kd]  # Genome consists of the p, i, d constants
        self.prev = 0
        self.sum = 0

    def calculate(self, error):
        self.sum += error
        slope = error - self.prev
        self.prev = error
        p = self.genome[0] * error
        i = self.genome[1] * self.sum
        d = self.genome[2] * slope
        return p + i + d

    def mutate(self):
        new_genome = []
        for val in self.genome:
            fate = random.random()
            if fate <= config.MUTATION_RATE:
                new_genome.append(val + random.random() * config.MUTATION_MULTIPLIER)
            else:
                new_genome.append(val)
        return new_genome

    def __add__(self, other):
        gamete1 = self.mutate()
        gamete2 = other.mutate()
        child_genome = []
        for i in range(0, len(gamete1)):
            crossover = random.random()
            if crossover > config.CROSSOVER_RATE:
                child_genome.append(gamete1[i])
            else:
                child_genome.append(gamete2[i])
        return PidGenome(*child_genome)

    def __repr__(self):
        return str(self.genome)
