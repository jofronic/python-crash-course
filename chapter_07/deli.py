sandwich_orders  = ['tuna', 'blt', 'chicken', 'pastrami', 'veggie', 'pastrami', 'bacon', 'pastrami']
finished_sandwhiches = []

print(f"\nThe deli has run out of pastrami\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"Your {order.title()} is being made.")
    finished_sandwhiches.append(order)

print(f"The following sandwhiches are ready: ")
for finished in finished_sandwhiches:
    print(finished.title())