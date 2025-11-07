# #Start with some designs that need to be printed
# unprinted_designs = ['phone case','robot pendent','dodecahedron']
# completed_designs = []

# #simulate printing each design, until none are left
# #move each design to completed models after designings
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Print Model: {current_design}")
#     completed_designs.append(current_design)
# #Display all models
# print(f"The following models have been completed: ")
# for complete in completed_designs:
#     print(complete)




#simulate printing each design, until none are left
#move each design to completed models after designings
def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Print Model: {current_design}")
        completed_designs.append(current_design)
#Display all models

def show_complete_list(comlpeted_designs):
    print(f"The following models have been completed: ")
    for complete in completed_designs:
        print(complete)


unprinted_designs = ['phone case','robot pendent','dodecahedron']
completed_designs = []

print_models(unprinted_designs, completed_designs)
show_complete_list(completed_designs)