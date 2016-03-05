import os

dirName='Xul'
for item in os.listdir(dirName):
    new = item.replace('Necromancer', '0Necromancer')
    os.rename(dirName + '/' + item, dirName + '/' + new)
