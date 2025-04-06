import jax
import jax.numpy as jnp
import numpy as np
from typing import Callable, Dict, List, Tuple, Any, Optional
import logging
from functools import partial

"""
Run Optimization module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)


def run_optimization(
    predictor_apply_fn: Callable,
    predictor_params: Dict,
    candidate_embeddings: np.ndarray,
    objectives: List[Dict[str, Any]] = None,
    num_generations: int = 50,
    population_size: int = 100,
    mutation_rate: float = 0.1,
    crossover_rate: float = 0.7,
    seed: Optional[int] = None,
) -> List[int]:
    """
    Run multi-objective optimization to find Pareto-optimal compositions.

    Args:
        predictor_apply_fn: Function to apply the prediction head
        predictor_params: Parameters for the prediction head
        candidate_embeddings: Embeddings of candidate compositions
        objectives: List of objective specifications (e.g., {"property": "Strength_MPa", "goal": "maximize"})
        num_generations: Number of generations for genetic algorithm
        population_size: Population size for genetic algorithm
        mutation_rate: Mutation rate for genetic algorithm
        crossover_rate: Crossover rate for genetic algorithm
        seed: Random seed for reproducibility

    Returns:
        List of indices of Pareto-optimal candidates
    """
    # Set up default objectives if not provided
    if objectives is None:
        objectives = [
            {"property": 0, "goal": "maximize"},  # Strength_MPa
            {"property": 1, "goal": "maximize"},  # Tvis
            {"property": 2, "goal": "maximize"},  # RR
        ]

    # Convert numpy arrays to jax arrays
    candidate_embeddings_jnp = jnp.array(candidate_embeddings)

    # Set up RNG
    if seed is not None:
        rng_key = jax.random.PRNGKey(seed)
    else:
        rng_key = jax.random.PRNGKey(0)

    # Define objective function
    def objective_fn(indices):
        """
        Compute objective values for a set of candidates.

        Args:
            indices: Indices of candidates to evaluate

        Returns:
            Array of objective values (population_size, num_objectives)
        """
        # Get embeddings for selected candidates
        selected_embeddings = jnp.take(candidate_embeddings_jnp, indices, axis=0)

        # Predict properties
        predictions = predictor_apply_fn(predictor_params, selected_embeddings, training=False)

        # Extract relevant properties and apply sign based on goal
        objective_values = []
        for obj in objectives:
            prop_idx = obj["property"]
            sign = 1.0 if obj["goal"] == "maximize" else -1.0
            objective_values.append(sign * predictions[:, prop_idx])

        return jnp.column_stack(objective_values)

    # Initialize population with random indices
    rng_key, subkey = jax.random.split(rng_key)
    population = jax.random.choice(
        subkey, jnp.arange(candidate_embeddings.shape[0]), shape=(population_size,), replace=False
    )

    # Evaluate initial population
    fitness = objective_fn(population)

    # NSGA-II implementation
    def non_dominated_sort(fitness):
        """
        Perform non-dominated sorting to find Pareto fronts.

        Args:
            fitness: Array of objective values (population_size, num_objectives)

        Returns:
            Array of front indices for each individual
        """
        n_individuals = fitness.shape[0]
        n_objectives = fitness.shape[1]

        # Initialize fronts
        fronts = jnp.zeros(n_individuals, dtype=jnp.int32)

        # Compute domination matrix
        # A dominates B if A is better than B in at least one objective and not worse in any
        domination = jnp.zeros((n_individuals, n_individuals), dtype=jnp.bool_)

        for i in range(n_individuals):
            for j in range(n_individuals):
                if i != j:
                    # Check if i dominates j
                    better_in_any = False
                    worse_in_any = False

                    for k in range(n_objectives):
                        if fitness[i, k] > fitness[j, k]:
                            better_in_any = True
                        elif fitness[i, k] < fitness[j, k]:
                            worse_in_any = True

                    domination = domination.at[i, j].set(better_in_any and not worse_in_any)

        # Count how many individuals dominate each individual
        domination_count = jnp.sum(domination, axis=0)

        # Assign fronts
        current_front = 0
        while jnp.any(fronts == 0):
            # Find individuals not dominated by any remaining individual
            front_indices = jnp.where(domination_count == 0)[0]

            # Assign current front
            for idx in front_indices:
                fronts = fronts.at[idx].set(current_front + 1)

                # Update domination count for individuals dominated by idx
                dominated_indices = jnp.where(domination[idx])[0]
                for dom_idx in dominated_indices:
                    domination_count = domination_count.at[dom_idx].add(-1)

            # Move to next front
            current_front += 1

        return fronts

    def crowding_distance(fitness, fronts):
        """
        Compute crowding distance for individuals in each front.

        Args:
            fitness: Array of objective values
            fronts: Array of front indices

        Returns:
            Array of crowding distances
        """
        n_individuals = fitness.shape[0]
        n_objectives = fitness.shape[1]

        # Initialize crowding distances
        crowding = jnp.zeros(n_individuals)

        # Compute for each front
        for front in jnp.unique(fronts):
            # Get indices of individuals in this front
            front_indices = jnp.where(fronts == front)[0]

            if front_indices.size <= 2:
                # If only 1 or 2 individuals, assign infinite distance
                for idx in front_indices:
                    crowding = crowding.at[idx].set(jnp.inf)
            else:
                # Compute crowding distance for each objective
                for obj in range(n_objectives):
                    # Sort by this objective
                    sorted_indices = front_indices[jnp.argsort(fitness[front_indices, obj])]

                    # Set boundary points to infinity
                    crowding = crowding.at[sorted_indices[0]].set(jnp.inf)
                    crowding = crowding.at[sorted_indices[-1]].set(jnp.inf)

                    # Compute distances for interior points
                    obj_range = jnp.max(fitness[:, obj]) - jnp.min(fitness[:, obj])
                    if obj_range > 0:
                        for i in range(1, len(sorted_indices) - 1):
                            distance = (
                                fitness[sorted_indices[i + 1], obj]
                                - fitness[sorted_indices[i - 1], obj]
                            ) / obj_range
                            crowding = crowding.at[sorted_indices[i]].add(distance)

        return crowding

    def tournament_selection(population, fronts, crowding, tournament_size=2):
        """
        Select individuals using tournament selection.

        Args:
            population: Current population
            fronts: Front indices
            crowding: Crowding distances
            tournament_size: Size of each tournament

        Returns:
            Selected individuals
        """
        n_individuals = population.shape[0]
        selected = []

        for _ in range(n_individuals):
            # Randomly select tournament_size individuals
            rng_key, subkey = jax.random.split(rng_key)
            tournament_indices = jax.random.choice(
                subkey, jnp.arange(n_individuals), shape=(tournament_size,), replace=False
            )

            # Select the best individual from the tournament
            best_idx = tournament_indices[0]
            for idx in tournament_indices[1:]:
                # Compare based on front and crowding distance
                if fronts[idx] < fronts[best_idx] or (
                    fronts[idx] == fronts[best_idx] and crowding[idx] > crowding[best_idx]
                ):
                    best_idx = idx

            selected.append(population[best_idx])

        return jnp.array(selected)

    def crossover(parent1, parent2):
        """
        Perform crossover between two parents.

        Args:
            parent1: First parent
            parent2: Second parent

        Returns:
            Two offspring
        """
        # For indices, we'll just swap them
        return parent2, parent1

    def mutate(individual, mutation_rate, n_candidates):
        """
        Mutate an individual.

        Args:
            individual: Individual to mutate
            mutation_rate: Probability of mutation
            n_candidates: Number of available candidates

        Returns:
            Mutated individual
        """
        rng_key, subkey = jax.random.split(rng_key)
        if jax.random.uniform(subkey) < mutation_rate:
            # Replace with a random index
            rng_key, subkey = jax.random.split(rng_key)
            new_idx = jax.random.randint(subkey, (), 0, n_candidates)
            return new_idx
        else:
            return individual

    # Main optimization loop
    for generation in range(num_generations):
        logger.info(f"Generation {generation+1}/{num_generations}")

        # Evaluate population
        fitness = objective_fn(population)

        # Non-dominated sorting
        fronts = non_dominated_sort(fitness)

        # Compute crowding distance
        crowding = crowding_distance(fitness, fronts)

        # Select parents
        parents = tournament_selection(population, fronts, crowding)

        # Create offspring through crossover and mutation
        offspring = []
        for i in range(0, population_size, 2):
            if i + 1 < population_size:
                rng_key, subkey = jax.random.split(rng_key)
                if jax.random.uniform(subkey) < crossover_rate:
                    child1, child2 = crossover(parents[i], parents[i + 1])
                else:
                    child1, child2 = parents[i], parents[i + 1]

                # Mutate
                child1 = mutate(child1, mutation_rate, candidate_embeddings.shape[0])
                child2 = mutate(child2, mutation_rate, candidate_embeddings.shape[0])

                offspring.extend([child1, child2])
            else:
                offspring.append(parents[i])

        # Replace population with offspring
        population = jnp.array(offspring)

    # Final evaluation
    fitness = objective_fn(population)
    fronts = non_dominated_sort(fitness)

    # Get Pareto-optimal solutions (front 1)
    pareto_indices = population[fronts == 1]

    return list(np.array(pareto_indices))
