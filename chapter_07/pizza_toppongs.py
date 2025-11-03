prompt = "Tell me all the toppings you would like on your pizza\n (enter quit to end program) "
# message = ""
while True: 
    message2 = input(prompt)

    if message2 == 'quit':
        break
    else:
        print(f"\nWe will get that {message2} on your pizze as soon as possible ")

