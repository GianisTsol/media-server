from flask import Flask, render_template, request
import sys
import data_handler as dthd


app = Flask(__name__, static_url_path='/static')


Id = 0
ltr = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global ltr
    global Id


    if request.method == 'GET':
        if ltr==1:
            ltr=1
            return render_template('index.html', data=dthd.openMediaList() , **locals())

        elif ltr==0:
            ltr=0
            time = readTime(Id)
            return player(Id, time)

    if request.method == 'POST':
        if request.form['dest'] == '1':
            ltr = 1
            time = request.form['time']
            saveTime(time, Id)
            return render_template('index.html', data=dthd.openMediaList() , **locals())
        elif request.form['dest'] == '0':
            ltr = 0
            print('dest is 0')
            Id = request.form['id']
            time = readTime(Id)
            return player(Id, time)



def player(id, time):
    if dthd.ContentType(id) == "0":
        return render_template('show_player.html', seasons=dthd.ContentSeasons(Id), episodes=dthd.ContentEpisodes(id), video=dthd.ContentLocate(Id),**locals())
    if dthd.ContentType(id) == "1":
        return render_template('player.html', video=dthd.ContentLocate(Id),**locals())
    else:
        return render_template('player.html', video=dthd.ContentLocate(Id),**locals())




def readTime(id):
    with open('/home/gtsol/{}timestamp.txt'.format(dthd.ContentPath(id)), 'r') as f:
        time=f.read()
        if time:
            return time
        else:
            saveTime("1", id)
            return "1"



def saveTime(time, id):
    f = open('/home/gtsol/{}timestamp.txt'.format(dthd.ContentPath(id)), 'w')
    f.write(time)
    f.close()

@app.errorhandler(400)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5024')
