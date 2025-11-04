def describe_city(city, country = 'USA'):
    """This function matches cities and countries in a sentence"""
    print(f"{city.title()} is in {country.title()}")
describe_city('new york')
describe_city('san fran')
describe_city('tokyo', country = 'japan')