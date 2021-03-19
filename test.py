import numpy as np
from ypstruct import structure

def crossover (p1, p2):
    c1 = p1.deepcopy()
    c2 = p2.deepcopy()
    indexes = list(range(25))
    indexes = np.random.permutation(indexes)[0:5]
    print('Mesta za ukrstanje:')
    print(indexes)
    #For c1 keep letters at positions from indexes, add the rest from p2 (skip letters from p2 that match letters from p1)
    cross(c1, p2, indexes)
    cross(c2, p1, indexes)
    #For c2 keep letters at posi`tions from indexes, add the rest from p1 (skip letters from p1 that match ones letters p2)
    return c1, c2

def cross(c, p, indexes):
    #Passing c and p by reference
    skip_indexes = []
    for i in range(len(indexes)):
        #np.where vraca nizove
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

v = np.random.randn(10)
#print(v)
maximum = np.max(v)
minimum = np.min(v)
#print(maximum, minimum)

index_of_maximum = np.where(v == maximum)
index_of_minimum = np.where(v == minimum)
#print(v[index_of_minimum])


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w','x','y','z']
random_result = np.random.random_integers(0,25,5)
#print(random_result)
chromosome = structure()
chromosome.key = None

population = chromosome.repeat(2)
population[0].key = np.random.permutation(letters)
population[1].key = np.random.permutation(letters)
print('prvi roditelj:')
print(population[0].key)
print('drugi roditelj:')
print(population[1].key)

c1, c2 = crossover(population[0], population[1])
print('prvo dete:')
print(c1.key)
print('drugo dete:')
print(c2.key)

