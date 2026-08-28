print("Give me two numbers, and Ill divide them.")
print("Enter 'q' to quit. ")


while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide by 0!")
    else:
        print(answer)


# try:

#     print(5/0)
# except ZeroDivisionError:
#     print('You can not divide by Zero, try again.')