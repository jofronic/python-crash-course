ageprompt = "Are you old enough to watch this movie.\n"
ageprompt += "How old are you? "
age = int(input(ageprompt))
if age <=3:
        print("This movie is free")
elif 3 <= age <= 12:
        print ("Ticket price is $10")
else:
        print("Ticket price is $15")
        
    
    