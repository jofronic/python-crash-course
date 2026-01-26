class User:
    def __init__(self, f_name, l_name, user_age=None, user_location=None, status='Active'):
        """This class recieves first and last names"""
        self.first_name = f_name
        self.last_name = l_name
        self.age = user_age
        self.location = user_location
        self.status = status

    def describe_user(self):
        print(f"First name:{self.first_name}")
        print(f"Last name:{self.last_name}")
        print(f"This user is currently {self.age} and is located in {self.location}")
        print(f"Their account is in the {self.status}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")

    def __str__(self):
        # 👉 This controls what print(user) shows
        return f"{self.first_name} {self.last_name})"

shout_out = User('Johan', 'Dominique', 40)
shout_out2 = User('Onyi', 'Nwosu', 45, 'Brooklyn')
shout_out3 = User('Cecilia', 'Oryi')
shout_out4 = User('Sharma', 'Pinas')

users = [shout_out,shout_out2,shout_out3,shout_out4]
for user in users:
    print(user)
    user.describe_user()
    user.greet_user()
# print(shout_out)
# shout_out.describe_user()
# shout_out.greet_user()

# print(shout_out2)
# shout_out2.describe_user()
# shout_out2.greet_user()

# print(shout_out3)
# shout_out3.describe_user()
# shout_out3.greet_user()

# print(shout_out4)
# shout_out4.describe_user()
# shout_out4.greet_user()