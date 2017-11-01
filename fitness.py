import config
import pid


def fitness_check(organism):
    num_ticks = 0
    accuracy = 0
    height = 0
    velocity = 0
    previous_height = None
    previous_height_2 = None
    for idx, i in enumerate(config.FLIGHT_PROFILE):
        while True:
            thrust = organism.calculate(i - height)
            thrust = max(min([thrust, config.MAX_THRUST]), config.MIN_THRUST)
            velocity += thrust
            velocity += config.GRAVITY
            height = velocity + height
            if previous_height and previous_height_2 is not None:
                if abs(previous_height - height) + abs(previous_height_2 - height) < config.STABILITY_THRESHOLD:
                    accuracy += abs(i - height)
                    # print("Success! Stabilized at height {}".format(i))
                    break
            previous_height_2 = previous_height
            previous_height = height
            num_ticks += 1
            if num_ticks > config.TIMEOUT * (idx + 1):
                # print("Took too long")
                return
            if abs(height - i) > i * config.CONVERGENCE_CUTOFF:
                # print("Failed to converge at height {}".format(i))
                return
    # print("Fitness check done")
    return -num_ticks - (accuracy * config.ACCURACY_MULTIPLIER)  # This is the fitness for this individual


def survival_of_fittest(generation):
    ranked_genes = []
    for i in generation:
        val = fitness_check(i)
        if val is not None:
            ranked_genes.append((i, val))
    return sorted(ranked_genes, key=lambda x: x[1])[-2:]


def breed_next_gen(pair):
    next_gen = []
    for _ in range(config.GENERATION_SIZE):
        next_gen.append(pair[0] + pair[1])
    return next_gen


def evolve():
    adam = pid.PidGenome(*config.START_PID_1)
    eve = pid.PidGenome(*config.START_PID_2)
    generation = breed_next_gen((adam, eve))
    i = 0
    while i < config.EVOLUTION_STEPS:
        next_pair = survival_of_fittest(generation)
        if len(next_pair) < 2:
            generation = breed_next_gen((adam, eve))
            i = 0
            print("Starting evolution over from scratch")
            continue
        print("Step {0}, best pair {1}".format(i, next_pair))
        generation = breed_next_gen((next_pair[0][0], next_pair[1][0]))
        i += 1
    return next_pair[1][0]


if __name__ == "__main__":
    best_pid = evolve()
    print("Maybe-not-optimal P,I,D: {}".format(best_pid))
