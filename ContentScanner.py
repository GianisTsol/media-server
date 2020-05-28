import json
from os import walk

mypath = "/home/gtsol/Media/"
f = []
global dirnames

for (dirpath, dirnames, filenames) in walk(mypath):

    f.extend(filenames)
    print(dirnames)
    break
dataa = {}
dataa['content'] = []
for dir in dirnames:
    f2data = ""
    print(dir)
    with open(mypath + dir + '/conf.json', 'r') as f2:
        f2data = json.load(f2)
        dataa['content'].append(f2data['content'])

with open('info.json','w') as f1:
    json.dump(dataa, f1)
