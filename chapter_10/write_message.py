from pathlib import Path

# path = Path('/Users/thebrain/Documents/python_work/examples/pcc_3e/chapter_10/writing_to_a_file/programming.txt')

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
contents += "I want to add this line because i can.\n"

path = Path('programming2.txt')
path.write_text(contents)

read = path.read_text()

for line in read.splitlines():
    # contents = ''
    print(line)




