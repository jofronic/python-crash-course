def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print("\nMaking a pizza with following toppings:")
    for topping in toppings:
        print(f"--{topping}")
