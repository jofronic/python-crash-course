pizza = ['cheese', 'pepperoni','sausage','anchovies']
for slice in pizza:
    print(f'{slice.title()}')

for slice in pizza:
    print(f'{slice.title()}, is on of my favorite pizzas')

print(f"I like {pizza[0].title()} overall. I can't lie.")
print(f"But {pizza[1].title()} is really good.")
print(f"Im not super excited about {pizza[2].title()}.")
print(f"Yall can have some of my {pizza[3].title()}")

pizza.append('chicken')
friends_pizza = pizza[:]
friends_pizza.append('pineapple')

for slices in pizza:
    print(f'my favorite pizzas are: {slices}')

print('')
for slice in friends_pizza:
    print(f'my favorite pizzas are: {slice}')
