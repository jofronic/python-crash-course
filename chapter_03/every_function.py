rapper = ['bigge', 'tupac', 'nas', 'jim jones']

#makes a copy of the list
rapper_new = rapper.copy()

print(f'Which one of these rappers dont belong? {rapper[0].title()}, {rapper[1].title()}, {rapper[2].title()}, {rapper[3].title()} ')

#sorts it by alphabetical order
print(sorted(rapper))

# stores the string value in position 3 
not_here = rapper.pop(3)

#display the variable while capitlizing the first letter
print(f'{not_here.title()} is saying that he belongs?')

#add on Jay Z
rapper.append('Jay-Z')
print(f'This is {rapper[0]}, {rapper[1]}, {rapper[2]} and maybe {rapper[3]}')

#adds a new rappers
rapper.insert(1, '50 Cent')

#displays that new value in the index position
new_rapper = rapper[1]
print(f'We could throw in {new_rapper} to the list.')

#counts the values in the list
list_length = len(rapper)

print(f'We have {list_length} of the greatest rappers of all time here.')

print(f'We have the original list {' , '.join(rapper_new)} but the new list {' , '.join(rapper)} is the real greatest of all time')
