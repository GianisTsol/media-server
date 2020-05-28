import json
import os

#change data format
#add more values for id, type, etc

def openMediaList():
    with open('info.json') as json_file:
        data = json.load(json_file)
        return data

def ContentLocate(id):
    dta = openMediaList()
    for item in dta['content']:
        if item['id']==id:
            return item['location']
            break
        else:
            continue


def ContentPath(id):
    dta = openMediaList()
    for item in dta['content']:
        if item['id']==id:
            return item['path']
            break
        else:
            continue

def ContentType(id):
    dta = openMediaList()
    for item in dta['content']:
        if item['id']==id:
            return item['type']
            break
        else:
            continue

def ContentEpisodes(id):
    myDict = {}
    path="/home/gtsol/"+ContentPath(id)

    dirs=os.listdir(path)
    dirs.sort()
    dirs = [x for x in dirs if "." not in x]
    print(dirs)
    for dir in dirs:
        myDict[dir] = sorted(os.listdir(path+dir))
    return myDict

def ContentSeasons(id):

    path="/home/gtsol/"+ContentPath(id)

    dirs=os.listdir(path)
    dirs.sort()
    dirs = [x for x in dirs if "." not in x]
    return dirs
