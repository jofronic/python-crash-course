from pathlib import Path
import json

def get_stored_username(path):
    """Get stored user name"""
    if path.exists():
            contents = path.read_text()
            username = json.loads(contents)
            return username
    else:
         return None

def get_new_username(path):
    """prompt for a new username"""
    username = input("What is your name? \n")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def great_user():
    """Greet the user by name"""    
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back {username}")
    else:
        username = get_new_username(path)
        print(f"We will remember you next time, {username}")


great_user()