from pathlib import Path

learnText = Path('/Users/thebrain/Documents/python_work/chapter_10/learning_python.txt')
contents = learnText.read_text()
new_content = contents.replace('Python','C')
lines = new_content.splitlines()
for line in lines:
    print(line.lstrip())

