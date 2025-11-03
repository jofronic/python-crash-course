numbers = input("Please enter a number, and I will tell you if its a multiple of 10: ")
answer = int(numbers)
if answer % 10 == 0:
    print(f'{answer} is a multiple of 10.')
else: 
    print(f'{answer} number is not a multiple of 10.')