from src import app
from src.db import query
from flask import (
    render_template,
    request,
    session,
    redirect,
    url_for
) 

@app.route('/your_passwords', methods=['GET', 'POST']) 
def your_passwords(): 
    if request.method == 'POST': 
        if 'Delete Password' in request.form.values():
            for key in request.form:
                split_key = key.split('_')
                if split_key[0] == 'delete':
                    id = split_key[1]

            query("""DELETE FROM passwords
                    WHERE id=?""", [id])   
            
            return redirect(url_for('your_passwords'))
        return redirect(url_for('your_passwords'))
    else: 
        if 'username' not in session: # User not logged in
            return redirect(url_for('login'))

        passwords = query("""SELECT id, website
                                FROM passwords
                                WHERE uid IN (
                                    SELECT id
                                    FROM users
                                    WHERE username=?
                                )""", [session['username']])
        
        context = {
            'passwords': [list(row) for row in passwords]
        }

        return render_template('your_passwords.html', **context)
        
