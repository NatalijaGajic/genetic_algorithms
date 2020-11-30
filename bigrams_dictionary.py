import bigrams as bigrams
bigrams_dictionary = {}
letters_dictionary = {}
bigrams_starting_with_letter = {}

bigrams_sum_of_frequencies = 0
for i in range(len(bigrams.bigrams)):
    #Set all frequencies of letters and bigrams starting with a letter to 0
    #Calculate sum of bigram frequencies
    bigrams_sum_of_frequencies+=bigrams.bigrams[i][1]
    letters_dictionary[bigrams.bigrams[i][0][0]]=0
    letters_dictionary[bigrams.bigrams[i][0][1]]=0
    bigrams_starting_with_letter[bigrams.bigrams[i][0][0]]=0

for i in range(len(bigrams.bigrams)):
    #Count the frequency of a letter
    #Count the frequency of a bigram starting with a letter
    letters_dictionary[bigrams.bigrams[i][0][0]]+= bigrams.bigrams[i][1]
    letters_dictionary[bigrams.bigrams[i][0][1]]+= bigrams.bigrams[i][1]
    bigrams_starting_with_letter[bigrams.bigrams[i][0][0]]+= bigrams.bigrams[i][1]

keys = list(letters_dictionary.keys())
values = list(letters_dictionary.values())
#Set the probability of a letter
for i in range(len(letters_dictionary)): 
    letters_dictionary[keys[i]] = values[i]/(bigrams_sum_of_frequencies*2)
#Set the probability of a bigram 
for i in range(len(bigrams.bigrams)):
    bigrams_dictionary[bigrams.bigrams[i][0]] = (bigrams.bigrams[i][1]+1)/(bigrams_starting_with_letter[bigrams.bigrams[i][0][0]]+26)

#print(bigrams_dictionary)
#print(letters_dictionary)
#print(bigrams_dictionary)
