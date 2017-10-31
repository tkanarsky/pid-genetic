import random
class PidGenome(object):

    def __init__(self, kp, ki, kd, km):
        self.genome = [kp, ki, kd, km]  # Genome consists of the p, i, d constants and also rate of mutation factor
        self.prev = 0
        self.sum = 0

    def calculate(self, error):
        self.sum += error
        slope = error - self.prev
        self.prev = error
        p = self.genome[0]*error
        i = self.genome[1]*self.sum
        d = self.genome[2]*slope
        return p+i+d

    def mutate(self):
        new_genome = []
        for val in self.genome:
            fate = random.random()
            if 0 <= fate < self.genome[3]/2:
                new_genome.append(val + random.random() * 10)
            elif (self.genome[3]/2) <= fate < self.genome[3]:
                new_genome.append(val - random.random() * 10)
            elif self.genome[3] <= fate < 1:
                new_genome.append(val)
        if new_genome[3] <= 0:
            new_genome[3] = 1 - random.random()
        return new_genome


    def __add__(self, other):
        gamete1 = self.mutate()
        gamete2 = other.mutate()
        child_genome = []
        for i in range(0, len(gamete1)):
            if random.choice([True, False]):  # crossover
                child_genome.append(gamete1[i])
            else:
                child_genome.append(gamete2[i])
        return PidGenome(*child_genome)

    def __str__(self):
        return str(self.genome)
