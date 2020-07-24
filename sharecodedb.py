#!/usr/bin/env python3

from flask import Flask, request, render_template, \
                  redirect

from model_sqlite import save_doc_as_file, \
                  read_doc_as_file, \
                  get_last_entries_from_files

app = Flask(__name__)

@app.route('/')
def index():
    #d = { 'last_added':[ { 'uid':'testuid', 'code':'testcode' } ] }
    d = { 'last_added':get_last_entries_from_files() }
    print(d)
    return render_template('index.html',**d)

@app.route('/create')
def create():
    listId = save_doc_as_file()
    idCode = listId['idCode']
    return redirect("{}edit/{}".format(request.host_url,idCode))
    
@app.route('/edit/<int:idCode>/')
def edit(idCode):
    info = read_doc_as_file(idCode)
    code = info['code']
    langage = info['langage']
    uid = info['uid']
    idCode = info['idCode']
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code, langage = langage, idCode = idCode,
              url="{}view/{}".format(request.host_url,idCode))
    return render_template('edit.html', **d) 

@app.route('/publish',methods=['POST'])
def publish():
    code = request.form['code']
    uid  = request.form['uid']
    idCode = request.form['idCode']
    langage = request.form['langage']
    save_doc_as_file(uid,code,langage,idCode)
    print('save')
    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     idCode))

@app.route('/view/<int:idCode>/')
def view(idCode):
    info = read_doc_as_file(idCode)
    code = info['code']
    langage = info['langage']
    uid = info['uid']
    idCode = info['idCode']
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code, langage = langage, idCode = idCode,
              url="{}view/{}".format(request.host_url,idCode))
    return render_template('view.html', **d)

@app.route('/admin/')
def admin():
    pass

if __name__ == '__main__':
    app.run()

