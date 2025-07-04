motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#adds a value to the list 
motorcycles.append('ducati')
print(motorcycles)

#creates an array using the append.
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']

#this inserts a value
motorcycles.insert(0, 'ducati')

print(motorcycles)

#this deletes the value based on the index 
del motorcycles[0]
print(motorcycles)
print(f'The answer above should remove ducati')

#Pops out the the last value in the array
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#this shows the popped value with capital letter for the first letter
print(f'The value show is a {popped_motorcycle.title()}')

#this displays the remaining list once the value has been popped
print(f'The remaining list {motorcycles}!')

#this removes the string regardless of the position
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda','yamha','suzuki', 'ducati']
print(motorcycles)

#this assigns a string value to a variable then uses that variable to for the remove method
too_expensive = 'ducati'

#this removes the string value in the variable
motorcycles.remove(too_expensive)

print(motorcycles)
print(f'{too_expensive.title()} is too expensive for me.')
