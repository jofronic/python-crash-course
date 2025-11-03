cities = {

    'new york' : {
                'country': 'USA',
                'population' : 13_000_000,
                'fact' : 'statue of liberty',

    },
    'florida' :
    {
                'country': 'USA',
                'population' : 18_000_000,
                'fact' : 'Oranges',

    }, 
    'georgia' : {
                'country': 'USA',
                'population' : 9_000_000,
                'fact' : 'hotlanta',

    }
}

for city, fact in cities.items():
    print(f"{city.title()} is full of great things to do located in {fact['country']}.")
    print(f"{city.title()} has a population of {fact['population']:,}.")
    print(f"Heres and instering face about this city: {fact['fact']}\n")

#adds new cities

cities['new jersey'] = {

                'country': 'USA',
                'population' : 3_000_000,
                'fact' : 'car jackings',


}

for city, fact in cities.items():
    print(f"{city.title()} is full of great things to do located in {fact['country']}.")
    print(f"{city.title()} has a population of {fact['population']:,}.")
    print(f"Heres and instering face about this city: {fact['fact']}\n")

cities['Texas'] = {

                'country': 'USA',
                'population' : 22_000_000,
                'fact' : 'Cows',

}

for city, fact in cities.items():
    print(f"{city.title()} is full of great things to do located in {fact['country']}.")
    print(f"{city.title()} has a population of {fact['population']:,}.")
    print(f"Heres and instering face about this city: {fact['fact']}\n")

print('\nWe have to delete texas\n')


del cities['Texas']

print('Texas is coming off the list\n')

for city, fact in cities.items():
    print(f"{city.title()} is full of great things to do located in {fact['country']}.")
    print(f"{city.title()} has a population of {fact['population']:,}.")
    print(f"Heres and instering face about this city: {fact['fact']}\n")
