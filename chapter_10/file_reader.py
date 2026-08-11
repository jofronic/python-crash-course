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

print(f"{pi_string[:52]}....")
print(len(pi_string))