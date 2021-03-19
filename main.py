import numpy as np
from ypstruct import structure
import bigrams_dictionary as bigrams
import genetic_algotithm as ga

bigrams_dictionary = bigrams.bigrams_dictionary
letters_dictionary = bigrams.letters_dictionary
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w','x','y','z']
letters = np.array(letters)

def encode_open_text(open_text, key):
    """Returns the encoded open text encoded with key"""
    cipher = ''
    for i in range(len(open_text)):
        cipher+=key[np.where(letters == open_text[i])][0]
    return cipher

def decode_chiper(cipher, key):
    """Returns the decoded cipher decoded with key"""
    decoded_text = ''
    for i in range(len(cipher)):
        decoded_text+=letters[np.where(key == cipher[i])][0]
    return decoded_text

#Cost function is the probability of a word being in the language
def costfunction(encoded_text, random_permutation):
    decoded_text = decode_chiper(encoded_text, random_permutation)
    """Returns the probability of a decoded text"""
    prob = np.math.log(letters_dictionary[decoded_text[0]]) 
    for i in range(1,len(decoded_text)):
        prob+= np.math.log(bigrams_dictionary[decoded_text[i-1]+decoded_text[i]])
    return prob

random_permutation = np.random.permutation(letters)
#print(random_permutation)
open_text = 'helloworld'
cipher = encode_open_text(open_text, random_permutation)
print("Endcoded text: {}".format(cipher))
decoded_text = decode_chiper(cipher, random_permutation)
print("Decoded text: {}".format(decoded_text))

prob_open_text = costfunction(decoded_text, letters)
# print(prob_open_text)
# prob_cipher = costfunction(cipher, random_permutation)
# print(prob_cipher)
# print('over')

#Problem
problem = structure()
problem.costfunction = costfunction
problem.key = letters
problem.encoded_text = cipher

#Parameters
params = structure()
params.max_iterations = 10
params.npop = 100
#Precentage of population in the offspring
params.pc = 1
#Probability of mutation
params.pm = 0.1
#Number of positions in a crossover
params.crossover_positions = 8
#Probability of selecting the individual with better fitness in tournament selection
params.pt = 0.9


#Run the GA
print("Running the GA...")
output = ga.run(problem, params)
print("Best cost is:{}".format(output.best_solution_cost))
print("Best solution is:{}".format(output.best_solution_key))
print("The cost of the real solution is:{}".format(prob_open_text))
print("The real solution is:{}".format(random_permutation))
print("The real open text is:{}".format(open_text))
encoded_text_from_algorithm = decode_chiper(cipher, output.best_solution_key)
print("Text decoded with the solution of the algorithm:{}".format(encoded_text_from_algorithm))
