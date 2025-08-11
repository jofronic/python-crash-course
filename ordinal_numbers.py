numbers = [1,2,3,4,5,6,7,8,9]

if numbers[0] == 1:
    print(f"this is the {numbers[0]}st")
if numbers[1] == 2:
    print(f"this is the {numbers[1]}st")
if numbers[2] == 3: 
    print(f"this is the {numbers[2]}st")

for numbers in range(4, 10, 1):
    print(f"This is the {numbers}th")


numbers = [1,2,3,4,5,6,7,8,9]

for n in numbers:
    suffix = 'th'
    if n == 1:
        suffix = 'st'
    elif n == 2:
        suffix = 'nd'
    elif n == 3:
        suffix = 'rd'

    print(f"This is {n}{suffix}")