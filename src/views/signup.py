from src import app
from src.db import query
from flask import (
    render_template,
    session,
    request,
    redirect,
    flash,
    url_for
)
from bcrypt import hashpw, gensalt

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_exists_check = query(f"""SELECT *
                                        FROM users
                                        WHERE username = '{username}'""")
        
        if len(user_exists_check):
            flash('User already exists')
            return redirect('signup')
        
        hashed_password = hashpw(password.encode(), gensalt(14))

        query(f"""INSERT INTO USERS
                (username, password)
                VALUES ('{username}', '{hashed_password.decode()}')""")     
        
        session['username'] = username
        
        return redirect(url_for('login'))
    else:
        if 'username' in session: # User already logged in
            return redirect(url_for('login'))
        else:
            return render_template('signup.html')