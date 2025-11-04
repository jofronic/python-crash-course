def describe_city(city, country = 'USA'):
    print(f"{city.title()} is in {country.title()}")
describe_city('new york')
describe_city('san fran')
describe_city('tokyo', country = 'japan')