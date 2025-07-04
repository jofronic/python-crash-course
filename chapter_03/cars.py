cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_copy = cars.copy()
print(cars)

#sorts the list in alphabetical order
cars.sort()
print(cars)

#sorts the list in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

print('\nHere is the Orginal List:')
print(cars_copy)

print('\nHere is the sorted list:')
print(sorted(cars_copy))

print('\nHere Is the orginial list again:')
print(cars_copy)

cars_copy.reverse()
print(cars_copy)
print(len(cars_copy))
