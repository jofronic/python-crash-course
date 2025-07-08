my_foods = ['pizza','burgers', 'ice cream','falafel']
copy_my_foods = my_foods[:]

print(f'My favorite foods are: \n{list(my_foods)}')

print (f'These are also my favorite foods: \n{copy_my_foods}')

copy_my_foods.append('bread')
my_foods.append('rice')


print(my_foods)
print(copy_my_foods)

# print(f'I added my other favorite food to the list: \n{new_food}')
# print(f'I added this food to my list because i eat every day \n{new_food_b}')

