prompt = "Tell me all the toppings you would like on your pizza\n (enter quit to end program) "

while True: 
    message2 = input(prompt)

    if message2 == 'next':
        break
    else:
        print(f"\nWe will get that {message2} on your pizze as soon as possible ")

Active = True
while Active:
    message3 = input('Tell me all the toppings again: ')

    if message3 != "quit":
       print(f"\nWe will get that {message3.title()} on your pizze as soon as possible ") 
    else:
        break
