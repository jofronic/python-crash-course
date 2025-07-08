players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[0:4])
print(players[2:])
print(players[-3:])

print(f'Here are the players on my team:')
for player in players[:3]:
    print(player)