message = input("How many people are in your dinner group?")
answer_01 = input(message)
answer_02 = int(message)
if answer_02 >= 8:
    print(f'You will have to wait to wait for a table.')
else:
    print(f"Your table is ready")