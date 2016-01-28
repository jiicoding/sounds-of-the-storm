import os

for item in os.listdir('Nazeebo_Base'):
    new = item.replace('WD_Male', 'NazeeboSpell')
    os.rename('Nazeebo_Base/' + item, 'Nazeebo_Base/' + new)
