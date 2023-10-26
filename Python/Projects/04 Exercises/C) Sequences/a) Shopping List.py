# Creating a shopping list to make an Apple Pie

shopping_list = [
    "Lard",
    "Margarine",
    "Plain flour",
    "Sugar",
    "Eggs",
    "Bramley apples",
    "Cinnamon",
    "Cream"
]

# Printing the shopping list as complete list prepared to double check
# print(shopping_list)

# Printing the list by looping over each items in the list

# for item in shopping_list:
#     print(item)

# Modifying the list - Cream to Double Cream
# index_of_cream = shopping_list.index("Cream")

# shopping_list[index_of_cream] = "Double cream"

# # Printing the new modified list

# for item in shopping_list:
#     print(item)

# how to get the index of a list using enumerate

for shop_index, shop_value in enumerate(shopping_list):
    print("Shop index ==> {0} \t Shop value ==> {1}".format(shop_index, shop_value))