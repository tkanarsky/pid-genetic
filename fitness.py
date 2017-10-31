import config
import time
import pid

def fitness_check(pid):
    num_ticks = 0
    accuracy = 0
    height = 0
    velocity = 0
    previous_height = None
    previous_height_2 = None
    previous_time = time.time()
    for idx, i in enumerate(config.flight_profile):
        while True:
            thrust = pid.calculate(i-height)
            thrust = max(min([thrust, config.max_thrust]), config.min_thrust)
            velocity += thrust
            # print("tick: {0}, height: {1}, velocity: {2}".format(num_ticks, height, velocity))
            height = velocity + height
            if previous_height and previous_height_2 is not None:
                if abs(previous_height - height) + abs(previous_height_2-height) < .001:
                    accuracy += abs(i-height)
                    print("______________Complete phase {}!________________".format(idx))
                    break
            # print("tick {}".format(height))
            previous_height_2 = previous_height
            previous_height = height
            num_ticks += 1
            if num_ticks > 10000 * (idx + 1):
                print("Took too long")
                return
            if abs(height-i) > i*3:
                print("failed to converge {}".format(i))
                print(num_ticks)
                return
    return -num_ticks - (accuracy * 500) # This is the fitness for this individual


def survival_of_fittest(generation):
    ranked_genes = []
    for i in generation:
        val = fitness_check(i)
        if val is not None:
            ranked_genes.append((i, val))
        else:
            pass
    print("we done")
    print(ranked_genes)
    return sorted(ranked_genes, key=lambda x: x[1])[-2:]

def breed_next_gen(pair):
    next_gen = []
    for i in range(config.generation_size):
        next_gen.append(pair[0] + pair[1])
    return next_gen

def evolve():
    adam = pid.PidGenome(0, 0, 0)
    eve = pid.PidGenome(1, 1, 1)
    generation = breed_next_gen((adam, eve))
    i = 0
    while i < config.evolution_steps:
        next_pair = survival_of_fittest(generation)
        if len(next_pair) < 2:
            generation = breed_next_gen((adam, eve))
            i = 0
            print("Starting evolution over from scratch")
            continue
        print("Step {0}, best pair {1}".format(i, next_pair))
        generation = breed_next_gen((next_pair[0][0], next_pair[1][0]))
        i+=1
    print(next_pair[0][0])

if __name__ == "__main__":
    evolve()








