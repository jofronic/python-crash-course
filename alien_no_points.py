alien_0 = {'color': 'green', 'speed':'slow'}

# The below code will reult in a traceback error
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

