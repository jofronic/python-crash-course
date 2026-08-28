from pathlib import Path
import json


username = input('what is your name?\n')
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}")
