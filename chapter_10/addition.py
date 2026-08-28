
first_number = input("Please eneter two Numbers: ")
second_number = input("Enter the second number: ")


try:
    first_number = int(first_number)
    second_nubmer = int(second_number)
except ValueError:
    print(f"Please enter a number.")

else:
    print(f"{first_number} , {second_number}")
