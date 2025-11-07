#Start with some designs that need to be printed
unprinted_designs = ['phone case','robot pendent','dodecahedron']
completed_designs = []

#simulate printing each design, until none are left
#move each design to completed models after designings
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Print Model: {current_design}")
    completed_designs.append(current_design)
#Display all models
print(f"the following models have been completed")
for complete in completed_designs:
    print(complete)