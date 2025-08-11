requested_toppings = ['cheese', 'pepperoni', 'pineapple' ]
if 'cheese' in requested_toppings:
    print("adding cheese")
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')
if 'pineapple' in requested_toppings:
    print('adding pineapple')
print("Making your Pizza")

if 'cheese' in requested_toppings:
    print("adding cheese")
elif 'pepperoni' in requested_toppings:
    print('adding pepperoni')
elif 'pineapple' in requested_toppings:
    print('adding pineapple')
elif 'pepperoni' in requested_toppings:
    print('adding pepperoni')
print("Making your Pizza")

avalible_toppings = ['cheese','pineapple']

for requested_topping in requested_toppings: 
    if requested_topping in avalible_toppings:
        print(f"Adding {requested_topping} to your pizza")
    else:
        print(f"sorry we dont have {requested_topping}")