users = {
    'aeinstein': {
        'first_name': 'albert',
        'last_name' : 'einstein',
        'location' : 'princeton',
    },

    'mcurie' : {
        'first_name': 'marie',
        'last_name' : 'curie',
        'location' : 'paris',

    },
}

for username, user_info in users.items():
    print(f"\nusername: {username}")
    full_name = f""