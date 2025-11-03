responses = {}
#Set a flag to indicate that polling is active.
polling_active  = True
while polling_active:
    #Prompt for the person's name and response
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb one day? ")

    # Store the response in the dictionary
    responses[name]  = response

    #find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person? Yes/No ")
    if repeat.lower() == "no":
        polling_active = False

#polling is now complete
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}. ")