car = 'subaru'
print("Is care == 'subaru'? I predict True.")
print (car == 'subaru')
print("Is car == 'audi'? I predict False. ")
print(car == 'audi')

bus = "q17"
print("\nIs bus == q17? I predict True")
print(bus == "q17")
print ("Is bus == q43? I predict False")
print(bus == 'Q43')

train = 'F'
print("\nI predict the train == 'F'.")
print(train == 'F')
print("This train == G? I predict this to be false")
print(train == 'G')

school = 'good'
print("is school == good? I predict True")
print(school == 'good')
print("is school == 'bad'? I predict False")
print(school == 'bad')

age = 46
print("age == 19? I predict false")
print(age == 19)
print('Are they 46? I predict true')
print(age == 46)

gpa = 4
print("is the gpa a 4.0")
print ( gpa >= 4)
print("is the GPA low? I predict false")
print(gpa == 2)

iq = 78
print("\nis the IQ > 120. I predict False")
print(iq > 120)
print("is the Iq lower than 85. I predict True")
print(iq < 85)

teachers = ['Ms.Sally','Ms. Johnson', 'Mr.Roberts']
print(" \nIs Ms. Sally a part of the teachers this year. I predict True")
if 'Ms.Sally' in teachers:
   print('Ms.Sally' in teachers)

print("Is Mr. Roberts teaching this year. I predict True")
if 'Mr.Roberts' in teachers:
    print('Mr.Roberts' in teachers)

print("Ms. Lazou will not be teaching this year. I predict True")
if 'Ms.Lazou' not in teachers:
    print('Ms.Lazou' not in teachers)

age = 21

if age > 18 and age < 31:
    print('You may enter')

print("Bags are a restricted item. I predict, true.")
restricted = ['bags', 'wallets', 'knives']
if 'bags' in restricted:
    print('bags' in restricted)
print("Are guns not in the restricted list. I predict True")
if 'Guns' not in restricted:
    print('Guns' not in restricted)

