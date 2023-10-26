# 1) Print the first 3 letters of the word catastrophe.
# 2) Print letters 4 to 6 from The Dogs of War.
# 3) Print the last 3 letters from The Trouble with Lichen.
# 4) Print every other character from Springy.
# 5) Print every other character from meagre, starting with the penultimate one and going backwards.

# Working on the point 1
word1 = "catastrophe"

print(word1[:3:])

# Working on the point 2
word2 = "The Dogs of War"

print(word2[4:7:])

# Working on the point 3
word3 = "The Trouble with Lichen"

print(word3[-3::])

# Working on the point 4
word4 = "Springy"

print(word4[::2])

# Working on the point 5
word5 = "meagre"

print(word5[-2::-2])