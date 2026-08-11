from pathlib import Path

content = input("What is your name? ")

path = Path('guest.txt')
path.write_text(content)