# Genetic Algorithm for Traveling Salesman Problem (TSP)

## Overview

This Python script implements a genetic algorithm to solve the Traveling Salesman Problem (TSP). The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits each city exactly once and returns to the original city.

## Functionality

The algorithm follows these steps:

1. **Initialization**: It initializes a population of potential solutions randomly.
2. **Evaluation**: It evaluates the fitness of each individual in the population by calculating the total distance traveled for each potential solution.
3. **Selection**: It selects pairs of parents from the population based on their fitness scores.
4. **Crossover**: It generates offspring by combining the genetic material of the selected parents.
5. **Mutation**: It introduces random changes to the offspring to maintain genetic diversity.
6. **Replacement**: It replaces the old generation with the new generation of offspring.
7. **Termination**: It terminates after a certain number of generations or when a satisfactory solution is found.

## Dependencies

The script requires the `time`, `random`, `math`, and `sys` modules, which are standard libraries in Python.

## Usage

To use the script, follow these steps:

1. Define your graph representation in a text file where each line corresponds to a vertex and its neighbors with respective distances.
2. Update the filename in the script to point to your graph file.
3. Optionally, adjust parameters such as `max_generations`, `population_size`, and `mutation_rate` according to your problem requirements.
4. Run the script. It will output the best path found and its distance, along with the runtime of the genetic algorithm.

## Example

```python
if __name__ == '__main__':
    # Load the graph from a file
    g = adjMatFromFile("complete_graph_n08.txt")

    # Run the genetic algorithm to find the best solution
    start_time = time.time()
    res_ga = genetic_algo(g, max_generations=100, population_size=100, mutation_rate=0.1)
    elapsed_time_ga = time.time() - start_time
    print(f"Genetic Algorithm runtime: {elapsed_time_ga:.2f} seconds")
    print(f"Best path: {res_ga['path']}")
    print(f"Path distance: {res_ga['path_distance']}")
