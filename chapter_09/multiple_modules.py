from privileges import Admin as A


admin1 = A('Johan', 'Dominique', 34)

print("Show admin1 privileges: ", admin1)
admin1.describe_user()
admin1.privileges.show_privileges()



