# class User:
#     def __init__(self, f_name, l_name, user_age=None, user_location=None, status='Active'):
#         """This class recieves first and last names"""
#         self.first_name = f_name
#         self.last_name = l_name
#         self.age = user_age
#         self.location = user_location
#         self.status = status

#     def describe_user(self):
#         print(f"First name:{self.first_name}")
#         print(f"Last name:{self.last_name}")
#         print(f"This user is currently {self.age} and is located in {self.location}")
#         print(f"Their account is in the {self.status}")

#     def greet_user(self):
#         print(f"Welcome {self.first_name} {self.last_name}")

#     def __str__(self):
#         # 👉 This controls what print(user) shows
#         return f"{self.first_name} {self.last_name}"

from users import User
from privileges import Privileges

class Admin(User):
    def __init__(self, f_name, l_name, user_age=None, user_location=None, status='Active'):
        """This init passes constructers from User Class"""
        super().__init__(f_name, l_name, user_age, user_location, status)
        self.privileges = Privileges()
    
    # def show_privileges(self):
        
    #     for right in self.privileges: 
    #         print(f"This user can perform the following task: {right}")


# rights = Admin('Johan', 'Dominique', 28)
# rights.describe_user()
# rights.show_privileges()