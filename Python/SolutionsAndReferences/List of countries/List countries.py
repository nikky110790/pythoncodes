
def get_contents_of_file(Argument_or_arguments_to_go_here):

    # this needs writing!
    pass

def get_country_dict(Argument_or_arguments_to_go_here):

    # this needs writing!
    pass

def print_results(Argument_or_arguments_to_go_here):

    # this needs writing!
    pass

# choose continent to show data for
continent_name = "Oceania"

# get text from file for given continent name
country_list = get_contents_of_file(continent_name)

# from this extract a list of countries and cities
countries = get_country_dict(country_list)

# list them out
print_results(continent_name,countries)

