from flask import *
from db import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        userss=allUsers()
    except:
        print("error")
        userss=[]
    return render_template('table.html', users = userss)

@app.route('/new')
def new():
    return render_template('form.html')

@app.route('/delete/<int:id>')
def delete(id=0):
    if id>0:
        delete_user(id)
    return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):
    try:
        user = session.query(User).filter_by(id=id).all()[0]
    except:
        print "error"
        user=''
    if user!= '':
        return render_template('form.html', user=user)

    return redirect('/')


@app.route('/save', methods=['POST'])
def save():
    if request.form.get('id', None) !=None:
        update_user(request.form['id'], request.form['name'], request.form['email'], request.form['tel'])
    else:
        new_user(request.form['name'], request.form['email'], request.form['tel'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
