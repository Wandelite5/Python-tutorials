country_name = input("enter country name: ")

countries = {'Nigeria': {'Abuja': 'Abaji','Ekiti': 'Ise-orun'}, 'Canada': {'Onatario': 'Dufferin', 'Alberta': 'Edmonton'}}

def return_state(countries, country_name):
    return countries.get(country_name, {}).keys

def return_local_govt(country_name, state):
    pass

if country_name in countries: print("The states in {} are {}.". format(country_name, ))
