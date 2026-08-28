from pathlib import Path
import json

number = input("What is your favorite number? \n")    
path = Path('favoritenumber.json')
contents = json.dumps(number)
path.write_text(contents)

