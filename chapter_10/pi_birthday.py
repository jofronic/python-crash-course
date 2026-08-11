from pathlib import Path

# path = Path('chapter_10/pi_digits.txt')
path = Path('/Users/thebrain/Documents/python_work/chapter_10/pi_million_digits.txt')
# contents = path.read_text().rstrip()
contents = path.read_text()
# contents = contents.rstrip()

lines = contents.splitlines()
pi_string = ''

for line in lines:

    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi! ")
else: 
    print("Your birthday does not appear in the first million digits of pi! ")