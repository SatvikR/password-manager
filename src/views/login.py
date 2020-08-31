from src import app
from src.db import query
from flask import (
    render_template,
    request, 
    session, 
    redirect, 
    url_for, 
    flash
)
from bcrypt import checkpw

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'logout' in request.form: # User logged out
            session.pop('username')
            context = {'logged_in': False}
            return render_template('login.html', **context)

        username = request.form['username']
        password = request.form['password']

        target_user = query("""SELECT username, password 
                                FROM users 
                                WHERE username=?""", [username])
        
        if not len(target_user): # User not found
            flash('Username not found')
            return redirect(url_for('login'))
        
        target_username, target_password = target_user[0]

        if checkpw(password.encode(), target_password.encode()):
            session['username'] = username
            context = {'logged_in': True, 'username': username}
            return render_template('login.html', **context)
        else: # Password incorect
            flash('Password incorrect')
            return redirect(url_for('login'))
    else:
        if 'username' in session: # User is logged in
            context = {'logged_in': True, 'username': session['username']}
            return render_template('login.html', **context)
        else:
            context = {'logged_in': False}
            return render_template('login.html', **context)
