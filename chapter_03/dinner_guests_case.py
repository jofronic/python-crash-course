guest_list = ['Alex', 'Red', 'Sabrina','Edy']

#this sets a string value to a variable and then using the remove function to remove it from the list. 
not_coming = 'Edy'
guest_list.remove(not_coming)


#thi displays the variablies retrieved from the pop index. 
print(f'My brother, {not_coming} cant make it. but {guest_list[0]}, {guest_list[1]}, {guest_list[2]} is still coming.')

#adds new guest
guest_list.append('sharma')


#This removes the value from the index 0 position and sets it to a new variable
not_coming_1 = guest_list.pop(0)
not_coming_2 = guest_list.pop(0)
not_coming_3 = guest_list.pop(0)

print(f'{not_coming_1.title()}, {not_coming_2.title()}, {not_coming_3.title()}, is still coming.')
print(f'{not_coming_1.title()}, Thank you for coming. We will see you on the 4th.')
print(f'{not_coming_2.title()}, Thank you for coming. We will see you on the 4th.')
print(f'{not_coming_3.title()}, Thank you for coming. We will see you on the 4th.')

# print(guest_list)

guest_list.insert(0,'cecilia') 
guest_list.insert(2, 'onyi')
guest_list.insert(-1, 'lucien')

# print(guest_list)

# new_guest_1 = guest_list.pop(0)
# new_guest_2 = guest_list.pop(0)
# new_guest_3 = guest_list.pop(0)

print(f'{guest_list[0].title()}, Thank you for coming. We will see you on the 4th.')
print(f'{guest_list[1].title()},, Thank you for coming. We will see you on the 4th.')
print(f'{guest_list[2].title()}, Thank you for coming. We will see you on the 4th.')

guest_count = len(guest_list)
print(f'We have {guest_count} coming to dinner')