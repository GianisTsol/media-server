#This adds the config file to all movie directories
#Manual editing is needed

import json
from os import walk
import subprocess

mypath = "/home/gtsol/Media/"
f = []
global dirnames

for (dirpath, dirnames, filenames) in walk(mypath):

    f.extend(filenames)
    print(dirnames)
    break

global id
id = 9
f2data= {}
f2data['content'] = []
for dir in dirnames:

    print(mypath + dir + '/conf.json')
    with open(mypath + dir + '/conf.json', 'w') as f2:

        f2data['content'].append({
            'title': 'title',
            'id': id,
            'location': '/Media/'+dir,
            'path': '/Media/'+dir,
            'type': '1'
        })
        json.dump(f2data, f2)
        f2data['content'] = []
        id=id+1
        print(id)
