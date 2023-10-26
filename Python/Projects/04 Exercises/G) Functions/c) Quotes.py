
# some quotations
great_quotes = (
    "And we danced, on the brink of an unknown future, to an echo from a vanished past. (John Wyndham) \n" + \
    "Life is what happens to you while you're busy making other plans. (wrongly attributed to John Lennon)\n" + \
    "You cannot overestimate the unimportance of practically everything. (John Maxwell)"
)

# 1) A list of the words in the string of text, with new line characters removed.
# 2) The number of items in the list of words (this should be a single line of code!).
# 3) The longest word in a list (see note below).

def get_words(sentence:tuple) -> str:
    lines = sentence.split("\n")

    for line in lines:
        print("{0} has {1} words in it, te longest word of it is '{2}'".format(line.strip().title(), count_words(line.strip()), longest_word_new(line.strip())))

def count_words(sentence:str) -> int:

    # Funtion to get the total number of words in the sentence
    sentence_list = sentence.split()
    return len(sentence_list)

def longest_word(sentence:str) -> int:
    
    # Function to get the longest word in the line
    sentence_list = sentence.split()

    return max(sentence_list, key=len).upper()

def longest_word_new(sentence:str) -> str:

    len_check = 0
    long_word = ""

    lines = sentence.split()

    for line in lines:
        if len(line) > len_check:
            len_check = len(line)
            long_word = line
    return long_word.upper()

# Main funciton to being the code execution
get_words(great_quotes)
