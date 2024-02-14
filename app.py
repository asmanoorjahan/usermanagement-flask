import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
app= Flask(__name__)
app.config['SECRET_KEY']='your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute("select * from users where id = " + str(user_id)).fetchone()
    conn.close()
    return user 


@app.route('/')
def index():
    conn = get_db_connection()
    userlist = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=userlist)

@app.route('/<int:user_id>')
def user(user_id):
    user = get_user(user_id)
    return render_template('view.html', user=user)

@app.route('/create', methods=('GET','POST'))
def create():
    print("I am here .........")
    print(request)
    if request.method =='POST':
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        dob = request.form['dob']
        password = request.form['pass']

        if not username or not firstname or not lastname:
            flash('Username/Firstname/Lastname all are mandatory.')
        else:
            conn=get_db_connection()
            conn.execute('INSERT INTO users(username, firstname, lastname, dob, email, password, created) VALUES(?,?,?,?,?,?,date())',
                         (username,firstname, lastname, dob, email, password))
            conn.commit()
            conn.close()
        return redirect(url_for('index'))        
    return render_template('create.html')  



@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    currentuser = get_user(id)

    if request.method == 'POST':
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        dob = request.form['dob']
        pas = request.form['pass']

        if not username:
            flash('userName is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE users SET username = ?, firstname = ?, lastname = ?, email = ?, dob = ?, password = ? WHERE id = ?',
                         (username, firstname, lastname, email, dob, pas, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', user=currentuser) 


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    user = get_user(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(user['username']))
    return redirect(url_for('index'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          