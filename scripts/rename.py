import os

dirName='Xul'
for item in os.listdir(dirName):
    new = item.replace('Merc_', '')
    os.rename(dirName + '/' + item, dirName + '/' + new)
