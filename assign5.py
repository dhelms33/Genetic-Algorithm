import time
import random
import math
import sys

INF = sys.maxsize

def adjMatFromFile(filename):
    """ Create an adj/weight matrix from a file with verts, neighbors, and weights. """
    with open(filename, "r") as f:
        n_verts = int(f.readline())
        print(f" n_verts = {n_verts}")
        adjmat = [[None] * n_verts for _ in range(n_verts)]
        for i in range(n_verts):
            adjmat[i][i] = 0
        for line in f:
            int_list = [int(i) for i in line.split()]
            vert = int_list.pop(0)
            assert len(int_list) % 2 == 0
            n_neighbors = len(int_list) // 2
            neighbors = [int_list[n] for n in range(0, len(int_list), 2)]
            distances = [int_list[d] for d in range(1, len(int_list), 2)]
            for i in range(n_neighbors):
                adjmat[vert][neighbors[i]] = distances[i]
    return adjmat

def initialize_population(g, population_size):
    """Create a population for the genetic algorithm"""
    population = [] #initialize to blank list
    verts = len(g) #verts for MST problem
    for _ in range(population_size):
        population.append([0] + random.sample(range(1, len(g)), len(g) - 1)) #uses dynamic programming to initialize population
    return population

def evaluate_fitness(individual, g):
    """Calculate the fitness of an individual"""
    distance = 0
    for i in range(len(individual) - 1):
        start = individual[i]
        end = individual[i + 1]
        if g[start][end] is None: #if no ind exists, return infinity
            return float('inf')  # Invalid path, return infinity
        distance += g[start][end]
    # Add distance from last vertex back to the starting vertex
    distance += g[individual[-1]][individual[0]]
    return distance
        
def select_parents(population, g):
    """Select parents for the next generation"""
    return random.sample(population, 2) #radnomly select parents
    
def crossover(parent1, parent2, g):
    """Crossover operation to generate offspring"""
    crossover_section = random.randint(0, len(parent1) - 1) # Randomly determine crossover section
    child1 = parent1[:crossover_section] + parent2[crossover_section:]
    child2 = parent2[:crossover_section] + parent1[crossover_section:] #creates crossover using list functions
    return child1, child2

def mutate(individual, mutation_rate):
    """Mutate an individual with given mutation rate"""
    for i in range(len(individual)):
        if random.random() < mutation_rate: #if random number is less than mutation rate
            individual[i] = random.randint(0, len(individual) - 1) #mutate individual
    return individual

def genetic_algo(g, max_generations=150, population_size=200, mutation_rate=0.02, explore_rate=0.6):
    avg_path_dist_each_generation = []
    path = []
    path_distance = INF
    population = initialize_population(g, population_size)

    for generation in range(max_generations):
        # Evaluate fitness of each individual
        fitness_scores = [evaluate_fitness(individual, g) for individual in population]
        for i in range(len(population)):
            if fitness_scores[i] < path_distance:
                path_distance = fitness_scores[i]
                path = population[i]
        avg_path_dist_each_generation.append(sum(fitness_scores) / len(fitness_scores))

        # Select parents
        parents = [select_parents(population, g) for _ in range(population_size // 2)] #integer divison and lambda operator to ensure code conciseness

        # Generate offspring via crossover
        offspring = []
        for parent1, parent2 in parents:
            child1, child2 = crossover(parent1, parent2, g)
            offspring.extend([child1, child2])

        # Mutate offspring
        for individual in offspring:
            mutate(individual, mutation_rate)

        # Replace old generation with new generation
        population = offspring

    # Final solution
    best_individual = min(population, key=lambda x: evaluate_fitness(x, g))
    path = best_individual + [best_individual[0]]  # Complete the cycle
    path_distance = evaluate_fitness(best_individual, g)

    return {'path': path, 'path_distance': path_distance, 'path_evolution': avg_path_dist_each_generation}

if __name__ == '__main__':
    """ Load the graph (change the filename when you're ready to test larger ones) """
    g = adjMatFromFile("complete_graph_n08.txt")

    # Run genetic algorithm to find best solution possible
    start_time = time.time()
    res_ga = genetic_algo(g, max_generations=100, population_size=100, mutation_rate=0.1)
    elapsed_time_ga = time.time() - start_time
    print(f"GenAlgo runtime: {elapsed_time_ga:.2f}")
    print(f"  path: {res_ga['path']}")
    print(f"  path dist: {res_ga['path_distance']}")
