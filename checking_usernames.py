current_users = ['johan', 'bob','sally', 'tasha','admin', 'globaladmin'] 
new_users = ['Meg', 'Tyshawn', "NatAhlie", 'admin','globaladmin', 'JoHAn', 'sally']

current_users2 = [user.lower() for user in current_users.copy()]
new_users2 = [user.lower() for user in new_users.copy()]


for user in new_users2:
    if user == 'admin' or user == 'globaladmin':
        print(f'You must choose another user name. {user.title()}, is not availalbe')
    elif user in current_users2:
         print(f"Welcome {user.title()}")
    else:
        print(f"{user.title()}, please create an account.")