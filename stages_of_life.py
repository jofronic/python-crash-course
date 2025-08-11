person = 18
print(f"if my age is {person}, then:")
if person < 2:
    print("This is a baby")
elif person >= 2 and person < 4:
    print('This person is a toddler')
elif person >= 4 and person < 13:
    print("This person is a kid")
elif person >= 13 and person < 20: 
    print ("This is a teenager")
elif person >= 20 and person < 65:
    print("This person is an adult")
else:
    print("this person is an elder")