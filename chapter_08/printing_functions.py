# #Start with some designs that need to be printed
unprinted_designs = []
completed_designs = []

def print_models(unprinted_designs, completed_designs):
    print("This is the current design")
    while unprinted_designs:
        current_design = unprinted_designs.pop()        
        print(f"Print Model: {current_design}")
        completed_designs.append(current_design)
    
#Display all models

def show_complete_list(completed_designs):
    print(f"The following models have been completed: ")
    for complete in completed_designs:
        print(complete)

