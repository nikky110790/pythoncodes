# Create a tuple containing the following three things:

# A list of the names of your favourite colours
# The name of your favourite film
# Your lucky number

favourite_colours = ["Red", "Blue", "Black", "White"]
favourite_film = "Padayappa"
lucky_number = 7

complete_details = (favourite_colours, favourite_film, lucky_number)

print(type(complete_details))
print(complete_details)

counter = 0

# for item in complete_details:
#     print(type(item) )
#     print(item)

while counter < len(complete_details):
    print("Item {0} has type {1} : {2}".format(counter + 1, type(complete_details[counter]), complete_details[counter]))
    counter += 1