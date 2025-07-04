#establishes the same list
guest_list = ['Alex', 'Red', 'Sabrina','Edy']
new_list = list(guest_list
                )
#this sets a string value to a variable and then using the remove function to remove it from the list. 
not_coming = 'Edy'
guest_list.remove(not_coming)

#This removes the value from the index 0 position and sets it to a new variable
not_coming_1 = guest_list.pop(0)
not_coming_2 = guest_list.pop(0)
not_coming_3 = guest_list.pop(0)

#this displays the variablies retrieved from the pop index. 
print(f'My brother, {not_coming} cant make it. but {not_coming_1.title()}, {not_coming_2.title()}, {not_coming_3.title()} is still coming.')

#adds new guest
new_list.append('sharma')

print(f'{not_coming_1.title()}, {not_coming_2.title()}, {not_coming_3.title()}, is still coming.')
print(f'{not_coming_1.title()}, Thank you for coming. We will see you on the 4th.')
print(f'{not_coming_2.title()}, Thank you for coming. We will see you on the 4th.')
print(f'{not_coming_3.title()}, Thank you for coming. We will see you on the 4th.')

new_list.insert(0,'cecilia') 
new_list.insert(2, 'onyi')
new_list.insert(-1, 'lucien')

# print(guest_list)


# new_guest_1 = guest_list.pop(0)
# new_guest_2 = guest_list.pop(0)
# new_guest_3 = guest_list.pop(0)

# # print(guest_list)

# print(f'{new_guest_1.title()}, Thank you for coming. We will see you on the 4th.')
# print(f'{new_guest_2.title()}, Thank you for coming. We will see you on the 4th.')
# print(f'{new_guest_3.title()}, Thank you for coming. We will see you on the 4th.')

print(f'We can only invite two people for dinner.')
not_coming_1 = new_list.pop(0)
not_coming_2 = new_list.pop(0)
not_coming_3 = new_list.pop(0)
not_coming_4 = new_list.pop(0)
not_coming_5 = new_list.pop(0)
not_coming_6 = new_list.pop(0)

print(f'{not_coming_1.title()}, sorry we wont be able to acoomadate.')
print(f'{not_coming_2.title()}, sorry we wont be able to acoomadate.')
print(f'{not_coming_3.title()}, sorry we wont be able to acoomadate.')
print(f'{not_coming_4.title()}, sorry we wont be able to acoomadate.')
print(f'{not_coming_5.title()}, sorry we wont be able to acoomadate.')
print(f'{not_coming_6.title()}, sorry we wont be able to acoomadate.')

print(f'{new_list[0].title()} I hope you can still make it. We will see you on the fourth')
print(f'{new_list[1].title()} I hope you can still make it. We will see you on the fourth')

del new_list[-1]
del new_list[-1]
print(new_list)