glossary_0 = {'variable' : 'a named container that stores a value in memory.',
              'string' : 'a string is a sequence of characters inside quotes.',
               'list' : 'a collection that can store multiple items in one variable.' ,
               'function' : 'a reusable block of code that performs a specific task.',
              'if_statement' : 'used to make decisions — only runs code if a condition is true.' }

# variable_00 = glossary_0['variable']
# variable_01 = glossary_0['string']
# variable_02 = glossary_0['list']
# variable_03 = glossary_0['function']
# variable_04 = glossary_0['if_statement']



# print(f" A variable is {variable_00}")
# print(f" A string is {variable_01}")
# print(f" A list is {variable_02}")
# print(f" A function is {variable_03}")
# print(f" An if statement is {variable_04}")

# for word, definition in glossary_0.items():
#     if word == 'if_statement':

#         print(f"An '{word}' is a {definition}")

#     else:
#         print(f"A '{word}' is a {definition}")



glossary_0['loop'] = 'repeats a block of code multiple times.'
glossary_0['dictionary'] = 'a collection of key-value pairs.'
glossary_0['tuple'] = 'an ordered, unchangeable sequence of items.'
glossary_0['boolean'] = 'a data type that can be either True or False.'
glossary_0['comment'] = 'a note in code ignored by the interpreter.'



glossary_0['method'] = 'acts on an object. Usually prefixed with a .'
glossary_0['function'] = 'Exists on its own hold methods but can be called to act on its own'
glossary_0['Class'] = 'Can hold data with methods and functions and be called on to act on an object'
glossary_0['object'] = 'a specific instance created from a class. It holds data attributes and can peform actions (methods)'
glossary_0['attribute'] = 'a variable that belongs to an object or class'

for word, definition in glossary_0.items():
    article = "An" if word[0].lower() in "aeiou" else "A"
    print(f"{article} '{word.title()}' is {definition.lower()}")

