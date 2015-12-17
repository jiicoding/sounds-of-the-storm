import os

for item in os.listdir('Horseman'):
    if 'VOX' in item:
        idx = item.index('VOX')
        new_item = item[:26] + item[30:]
        os.rename('Horseman/'+item, 'Horseman/'+new_item)
