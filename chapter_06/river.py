river = {'nile': 'egypt', 
         'mississpi': 'usa',
         'amazon': 'brazil',}
         

for location, rivers in river.items():
    print(f"The {rivers} river is located in {location}")

for location, rivers in river.items():    
    # for rivers in river.items():
    print(rivers)
    print(location)
