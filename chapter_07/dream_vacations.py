visited  = []
stop = 'quit'
while True:
    country = input("If you could visit one place in the world where would you go? (Type 'quit' to stop program) ")
    if country.lower() == stop:
        break      
    
    else:
        visited.append(country)   
        print(f"{country.title()} that sounds nice, lets check the flights!")
        print("Tell me another place you'd like to visit")


if not visited:
       print("Im sorry you dont want to travel.")
  
else:
    print(f"You would like to visit:")
    for places in visited:   
        
        print(places.title())
      

