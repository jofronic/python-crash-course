class User:
    def __init__(self, first_name, last_name, age=None, location=None, status='Active'):
        """This class recieves first and last names"""
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.location = location
        self.status = status

    def describe_user(self):
        print(f"First name:{self.f_name}")
        print(f"Last name:{self.l_name}")
        print(f"This user is currently {self.age} and is located in {self.location}")
        print(f"Their account is in the {self.status}")
    def greet_user(self):
        print(f"Welcome {self.f_name} {self.l_name}")

shout_out = User('Johan', 'Dominique', 40)
shout_out2 = User('Onyi', 'Nwosu', 45, 'Brooklyn')
shout_out3 = User('Cecilia', 'Oryi')
shout_out4 = User('Sharma', 'Pinas')

print(shout_out)
shout_out.describe_user()
shout_out.greet_user()

print(shout_out2)
shout_out2.describe_user()
shout_out2.greet_user()

print(shout_out3)
shout_out3.describe_user()
shout_out3.greet_user()

print(shout_out4)
shout_out4.describe_user()
shout_out4.greet_user()