# list of common words (source: Collins Dictionary)
common_words = ("the", "of", "and", "a", "to", \
    "in", "is", "you", "that", "it", "he", \
    "was", "for", "on", "are", "as", "with", "his", \
        "they", "I", "at", "be", "this", "have", "from")

# print out this list
title = "The original words"
print("\n" + title + "\n" + "-" * len(title))
print(common_words)

# how many are there?
title = "A - Number of words"
print("\n" + title + "\n" + "-" * len(title))

# show the first 5 words
title = "B - First 5 words"
print("\n" + title + "\n" + "-" * len(title))

# the last 3 words
title = "C - Last 3 words"
print("\n" + title + "\n" + "-" * len(title))

# every fifth word
title = "D - Every 5th word"
print("\n" + title + "\n" + "-" * len(title))

# iterate over words, listing out the ones with four letters
title = "E - Four-letter words"
print("\n" + title + "\n" + "-" * len(title))

# words beginning with W
title = "F - Words starting with W"
print("\n" + title + "\n" + "-" * len(title))

# show the words in alphabetical order (need to convert to a list first)
title = "G - Words in order"
print("\n" + title + "\n" + "-" * len(title))
