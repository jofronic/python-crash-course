from pathlib import Path
import json

path= Path('favoritenumber.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number, it is {number}")
else:
    pass

