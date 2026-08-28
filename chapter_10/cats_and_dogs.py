from pathlib import Path

contents = "tommy\n"
contents += "June\n"
contents += 'Beatrice\n'

path = Path('dogs.txt')
path.write_text(contents)

contents = "Sally\n"
contents += "Alan\n"
contents += "Lyla\n"
path = Path('cats.txt')
path.write_text(contents)

path = Path('dogs1.txt')
found_a_file = False
try:
    read_text = path.read_text()
except FileNotFoundError:
    print(f"{path} was not found\n")
else:
    found_a_file = True
    print(read_text)

path = Path('cats2.txt')
try:
    read_text = path.read_text()
except FileNotFoundError:
    print(f"{path} were not found\n")
else:
    found_a_file = True
    print(read_text)

print(found_a_file)
# if not found_a_file:
#    print("Both Files not found")