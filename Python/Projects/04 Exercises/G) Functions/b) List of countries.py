
# Creating Print Title Function
def print_title(title:str) -> str:
    return title + "\n" + "-" * len(title)

# Function to get the details from the input file and send list as the output
def get_contents_of_file(file_path:str, file_name:str) -> list:

    # input file path validation
    if file_path[-1] == "\\":
        file_path = file_path
    else:
        file_path = file_path + "\\"
    
    # get details from the input file and return the data as a list
    with open(file_path + file_name) as continent_details:
        
        #fetching all the lines in the input file
        return continent_details.read().splitlines()

# Function to return a dictionary of country and their capitals
def get_country_dict(county_details:list) -> dict:

    country_capitals = {}

    # Iterating the list and populating the dictionary
    for item in county_details:

        # Splitting the country and capital
        country, capital = item.split(",")

        country_capitals[country] = capital

    return country_capitals

def print_results(continent_name:str, countries:dict) :

    # Print the continent name and loop through the country and print its capitals
    print(print_title("The below are the list of countries with its capital for the continent => : {0}".format(continent_name)))

    # Printin the countries and capitals
    for country, capital in countries.items():
        print(country[0:3].upper() + " - " + country + ", " + capital)

# choose continent to show data for
continent_name = "Asia"

# get text from file for given continent name
country_list = get_contents_of_file(r"D:\My_Learning\Python\SolutionsAndReferences\List of countries", continent_name + ".csv")

# from this extract a list of countries and cities
countries = get_country_dict(country_list)

# list them out
print_results(continent_name,countries)
