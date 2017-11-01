# Simulation parameters
MAX_THRUST = 5
MIN_THRUST = -5
GRAVITY = 0
FLIGHT_PROFILE = [100, 200, 50] # List of setpoints to follow, one after the other

# Fitness check parameters
STABILITY_THRESHOLD = 0.001
TIMEOUT = 10000
CONVERGENCE_CUTOFF = 3
ACCURACY_MULTIPLIER = 500

# Evolution parameters
GENERATION_SIZE = 100
EVOLUTION_STEPS = 10
MUTATION_RATE = .90
MUTATION_MULTIPLIER = 100
CROSSOVER_RATE = 1 # 0-1: lower numbers favor the 2nd best candidate, higher numbers the first best
START_PID_1 = [0, 0, 0]
START_PID_2 = [1, 1, 1]
