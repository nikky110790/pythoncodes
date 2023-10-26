# As you grow older, you may want a reminder of some basic facts about yourself to tide you over those senior moments:

# Your name
# Where you live
# A personal detail to help orient yourself

# Writing the personal details to the text file
with open(file:=r"D:\My_Learning\Python\Solutions\Personal Details\Personal Details.txt", "w") as personal_details:
    personal_details.write("My name is Keerthikumar C M")
    personal_details.write("\nI live in India")
    personal_details.write("\nI love to code applications and to automate the tasks")

personal_details.close()

print("Personal details text file is generated")

# Reading back the personal details and printing them in the output window

with open(r"D:\My_Learning\Python\Solutions\Personal Details\Personal Details.txt","r") as personl_details_read:
    # personl_details_read.read()

    # Printing the read data in the output window
    print(personl_details_read.read())

personl_details_read.close()