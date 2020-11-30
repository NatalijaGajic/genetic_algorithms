import numpy as np
from ypstruct import structure
import bigrams_dictionary as bigrams

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
def costfunction(decoded_text):
    """Returns the probability of a decoded text"""
    prob = np.math.log(letters_dictionary[decoded_text[0]]) 
    for i in range(1,len(decoded_text)):
        prob+= np.math.log(bigrams_dictionary[decoded_text[i-1]+decoded_text[i]])
    return prob

random_permutation = np.random.permutation(letters)
#print(random_permutation)
open_text = 'helloworld'
cipher = encode_open_text(open_text, random_permutation)
print(cipher)
decoded_text = decode_chiper(cipher, random_permutation)
print(decoded_text)

prob_open_text = costfunction(decoded_text)
print(prob_open_text)
prob_cipher = costfunction(cipher)
print(prob_cipher)
print('over')

#Problem
problem = structure()
problem.costfunction = costfunction