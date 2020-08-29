from src import app
from src.db import query
from flask import (
    render_template,
    request,
    session,
    redirect
)

@app.route('/your_passwords')
def your_passwords():
    if 'username' not in session: # User not logged in
        return redirect('login')

    passwords = query(f"""SELECT id, website
                            FROM passwords
                            WHERE uid IN (
                                SELECT id
                                FROM users
                                WHERE username='{session['username']}'
                            )""")
    
    context = {
        'passwords': [list(row) for row in passwords]
    }

    print(context)

    return render_template('your_passwords.html', **context)
        
