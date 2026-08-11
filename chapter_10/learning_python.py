from pathlib import Path

learnText = Path('/Users/thebrain/Documents/python_work/chapter_10/learning_python.txt')
contents = learnText.read_text()
lines = contents.splitlines()
for line in lines:
    print(line.lstrip())