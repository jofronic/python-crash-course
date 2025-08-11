user_names = ['cyber', 'director', 'admin', 'audit', 'log' ]
for user in user_names:
    # print(repr(user))
    if user != 'admin': 
        print(f"Hello, {user.title()} thank you for  logging in again.\n")
    else:
        print(f"\tWelcome {user.title()} would you like to see a status report")
    # if user == 'director': 
    #     print(f"Welcome, {user.title()}, so youre in charge, eh.")
    # if 'admin' in user_names: 
    #     print(f"Welcome, {user.title()} what admin task would you like to do today?")
    # if 'audit' in user_names: 
    #     print(f"Welcome, {user.title()}, keeping an eye out.")
    # if 'log' in user_names: 
    #     print(f"Welcome, {user.title()}, going to do some tracking.")   


for user in user_names:
    # print(repr(user))
    if user == 'admin': 
      print(f"\nWelcome {user.title()} what would you like to do")   
    else:
        print(f'Welcome, {user.title()}')                      