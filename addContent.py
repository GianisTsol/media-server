import json


### TODO:
#make script more usable - add user input - detect new content


data = {}
data['shows'] = []
data['movies'] = []

data['movies'].append({
    'title': 'The Matrix 1999',
    'id': '5',
    'location': 'Media/The.Matrix.1999/The.Matrix.1999.720p.BrRip.264.YIFY.mp4',
    'path': 'Media/The.Matrix.1999/'
})

data['movies'].append({
    'title': 'Bad boys 1995',
    'id': '6',
    'location': 'Media/Bad.Boys.1995/BadBoys.mp4',
    'path': 'Media/Bad.Boys.1995/'
})

data['movies'].append({
    'title': 'The Matrix Reloaded',
    'id': '7',
    'location': 'Media/The.Matrix.2/The.Matrix.2.mp4',
    'path': 'Media/The.Matrix.2/'
})

with open('info.json', 'w') as outfile:
    json.dump(data, outfile)
