from privileges import Privileges as P
from users import User as U
from admin import Admin as A

user1 = A('Johan', 'Dominique', 43)
user1.describe_user()
user1.privileges.show_privileges()