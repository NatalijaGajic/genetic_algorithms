from ypstruct import structure
import numpy as np

key = []
def crossover (p1, p2, crossover_positions):
    c1 = p1.deepcopy()
    c2 = p2.deepcopy()
    indexes = list(range(25))
    indexes = np.random.permutation(indexes)[0:crossover_positions]
    #For c1 keep letters at positions from indexes, add the rest from p2 (skip letters from p2 that match letters from p1)
    #For c2 keep letters at positions from indexes, add the rest from p1 (skip letters from p1 that match ones letters p2)
    cross(c1, p2, indexes)
    cross(c2, p1, indexes)
    return c1, c2

def cross(c, p, indexes):
    #Passing c and p by reference
    skip_indexes = []
    for i in range(len(indexes)):
        skip_indexes.append(np.where(p.key == c.key[indexes[i]])[0][0])
    j = 0
    i = 0
    while i<len(c.key) and j<len(p.key):
        if i not in indexes:
            if j not in skip_indexes:
                c.key[i]=p.key[j]
                j+=1
                i+=1
            else: 
                j+=1
        else:
            i+=1

def mutate(c, probabilty_of_mutation):
    """Mutates the key with the given probability by switching values of two random positions"""
    n = probabilty_of_mutation*10
    array = list(range(10))
    value = np.random.permutation(array)[0]
    if value < n:
        array = list(range(26))
        position1 = np.random.permutation(array)[0]
        position2 = np.random.permutation(array)[0]
        temp = c.key[position1]
        c.key[position1] = c.key[position2]
        c.key[position2] = temp
    return c

def tournament_selection(population, pt, npop):
    population = sorted(population, key=lambda individual: individual.cost)
    n = (npop*(npop+1))/2
    array = np.random.permutation(list(range(n)))
    p1_index = array[0]
    p2_index = array[1]
    return None,None

def run(problem, params):
    #Problem
    cosfunction = problem.costfunction
    key = problem.key
    encoded_text = problem.encoded_text
    #Parameters
    max_iterations = params.max_iterations
    npop = params.npop
    pc = params.pc
    nc = np.round(npop*pc/2)*2
    crossover_positions = params.crossover_positions
    probabilty_of_mutation = params.pm
    pt = params.pt

    #Chromosome structure
    chromosome = structure()
    chromosome.key = None
    chromosome.cost = None

    #Best cost 
    best_solution = structure()
    best_solution.cost = -np.inf
    best_solution.key = None

    #Population
    population = chromosome.repeat(npop)
    for i in range(npop):
        #ovde mogu da se nadju dve iste permutacije
        population[i].key = np.random.permutation(key)
        population[i].cost = cosfunction(encoded_text, population[i].key)
        if population[i].cost > best_solution.cost:
            best_solution  = population[i]

    #Itterations
    for i in range(max_iterations):
        popc = []
        for j in range(int(nc//2)):
            #Selecting parents
            random_indexes = np.random.permutation(npop)

            p1 = population[random_indexes[0]]
            p2 = population[random_indexes[1]]
            #Stochastic tournament selection
            #p1, p2 = tournament_selection(population, pt, npop)

            #Crossover
            c1, c2 = crossover(p1, p2, crossover_positions)

            #Mutation
            c1 = mutate(c1, probabilty_of_mutation)
            c2 = mutate(c2, probabilty_of_mutation)
            c1.cost = cosfunction(encoded_text, c1.key)
            c2.cost = cosfunction(encoded_text, c2.key)
            if c1.cost > best_solution.cost:
                best_solution  = c1.deepcopy()
            if c2.cost > best_solution.cost:
                best_solution  = c2.deepcopy()
            popc.append(c1)
            popc.append(c2)

            print("Iteration {}: Best cost = {} ".format(i, best_solution.cost))

        population+=popc
        population = sorted(population, key=lambda individual: individual.cost)
        population = population[0:npop]          

    out = structure()
    out.population = population
    out.best_solution_key = best_solution.key
    out.best_solution_cost = best_solution.cost
    return out

