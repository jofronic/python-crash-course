print("Give me two numbers, and ill divide them")
print("enter 'q' to quit.")


while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    
    try: 

        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide by Zero")
    else:
        print(answer)

    # try:
    #     print(5/0)
    # except ZeroDivisionError:
    #     print("you cant divide by zero")