# list of common words (source: Collins Dictionary)
common_words = ("the", "of", "and", "a", "to", \
    "in", "is", "you", "that", "it", "he", \
    "was", "for", "on", "are", "as", "with", "his", \
        "they", "I", "at", "be", "this", "have", "from")

# Print out this list
title = "The original words"
print("\n" + title + "\n" + "-" * len(title))
print(common_words)

# How many are there?
title = "A - Number of words"
print("\n" + title + "\n" + "-" * len(title))
print(len(common_words))

# Show the first 5 words
title = "B - First 5 words"
print("\n" + title + "\n" + "-" * len(title))
print(common_words[:5])

# The last 3 words
title = "C - Last 3 words"
print("\n" + title + "\n" + "-" * len(title))
print(common_words[-3:])

# Every fifth word
title = "D - Every 5th word"
print("\n" + title + "\n" + "-" * len(title))
print(common_words[::5])

# Iterate over words, listing out the ones with four letters
title = "E - Four-letter words"
print("\n" + title + "\n" + "-" * len(title))

# for word in common_words:
#     if len(word) == 4:
#         print(word)

print([word for word in common_words if len(word) == 4])

# Words beginning with W
title = "F - Words starting with W"
print("\n" + title + "\n" + "-" * len(title))
print([word for word in common_words if word.lower().startswith("w")])

# for word in common_words:
#     if word.lower().startswith("w"):
#         print(word)

# Show the words in alphabetical order (need to convert to a list first)
title = "G - Words in order"
print("\n" + title + "\n" + "-" * len(title))

words = list(common_words)
words.sort()
print(words)