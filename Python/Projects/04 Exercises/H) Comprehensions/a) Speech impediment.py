
# Julius Caesar Act 4, Scene 3, 218–224

# Creating Print Title Function
def print_title(title:str) -> str:
    return title + "\n" + "-" * len(title)

# class for removing punctions
import string

brutus_speech = "There is a tide in the affairs of men \nWhich, taken at the flood, leads on to fortune; \nOmitted, all the voyage of their life \nIs bound in shallows and in miseries. \nOn such a full sea are we now afloat, \nAnd we must take the current when it serves, \nOr lose our ventures."

# Dictionary to hold the number of words and the count of it 
words_dict = {}
counter = 0
total_words = 0

# Removing the next line character from the  speech
new_brutus_speech = brutus_speech.replace("\n","")

# Remove the punctuations from the text
new_brutus_speech = new_brutus_speech.translate(str.maketrans('','',string.punctuation))

# Splitting into words
words = new_brutus_speech.split()

# Iterating the words
for word in words:
    # Getting the total words
    total_words += 1

    # Getting the word length
    word_length = len(word)
    
    if word_length in words_dict:
        counter = words_dict[word_length] + 1
    else:
        counter = 1
    
    words_dict[word_length] = counter

# Sorting the keys in the dictionary
word_keys = list(words_dict.keys())
word_keys.sort()

title = "Number of words in the speech is : "
print(print_title(title + str(total_words)))


for key in word_keys:

    # Printing the data
    print("{0}-letter words = {1}".format(key, words_dict[key]))

# List comprehensions
# number_of_words = [word for word in words if len(word) == 1]
# print(number_of_words)