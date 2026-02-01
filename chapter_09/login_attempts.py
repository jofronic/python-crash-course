class User:
    def __init__(self, f_name, l_name):
        """This class recieves first and last names"""
        self.first_name = f_name
        self.last_name = l_name
        self.age = 0
        self.location = None
        self.status = None
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")

        if self.age > 0:
            print(f"This user is currently {self.age} and is located in {self.location}")
        
        if self.status is not None:
            print(f"Their account is in the {self.status}")
            
        if self.login_attempts > 0:
            print(f'The user has logged in {self.login_attempts} times\n')
        else:
            print(f'User has not logged in yet. Please sign up.\n')

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")

    # def __str__(self):
    #     # 👉 This controls what print(user) shows
    #     return f"{self.first_name} {self.last_name}"
    
    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):
       
        self.login_attempts = 0
      

login_logs= User('Johan', 'dominique')
login_logs.describe_user()
for logs in range(5): 
    login_logs.increment_login_attempts()
    login_logs.describe_user()
login_logs.reset_login_attempts()
login_logs.describe_user()
