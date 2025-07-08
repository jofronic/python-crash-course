cube = []
for value in range(1,11):
    cube.append(value**3)
print(cube)

cube = [value**3 for value in range(1,11)]
print(list(cube))