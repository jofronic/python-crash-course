alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

print(f"The alien is {alien_0['color']}")
alien_0['color']= 'Purple'
print(f"Due to the alien losing life it is now {alien_0['color']}")

#sets the alien position and speed. 
alienspeed_0 = {'x_position': 0,'y_position':25, 'speed':'medium'}
print(f"Original Position:{alienspeed_0['x_position']}")


# Move the alien to the right
#determine how far to move alien based on current speed 
if alienspeed_0['speed'] == 'slow':
    x_increment = 1 
elif alienspeed_0['speed'] == 'medium':
    x_increment = 2
else: 
    #This must be fast alien.
    x_increment = 3

# The new position is the old position plus the increment. 

alienspeed_0['x_position'] = alienspeed_0['x_position'] + x_increment

print(f"New Position: {alienspeed_0['x_position']} ")

alienspeed_0['speed'] = 'fast'

if alienspeed_0['speed'] == 'slow':
    x_increment = 1 
elif alienspeed_0['speed'] == 'medium':
    x_increment = 2
else: 
    #This must be fast alien.
    x_increment = 3

# The new position is the old position plus the increment. 

alienspeed_0['x_position'] = alienspeed_0['x_position'] + x_increment

print(f"New Position: {alienspeed_0['x_position']} ")

alien_0 = {'color': 'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)


