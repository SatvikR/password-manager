from src import app
from src.db import query
from flask import (
    render_template,
    request,
    session,
    redirect,
    url_for
)
from base64 import b64encode

@app.route('/add_password', methods=['GET', 'POST'])
def add_password():
    if request.method == 'POST':
        website = request.form['website']
        password = request.form['password']

        if website[:4] != 'http': # Turn website into a real url
            website = 'http://' + website

        hashed_password = b64encode(password.encode()).decode()

        target_user = query(f"""SELECT id
                        FROM users
                        WHERE username='{session['username']}'""")

        uid, = target_user[0] # Destructuring query

        query(f"""INSERT INTO passwords
                (uid, website, password)
                VALUES ({uid}, '{website}', '{hashed_password}')""")
        
        return redirect(url_for('your_passwords'))
    else:
        if 'username' not in session:
            return redirect(url_for('login'))
        
        return render_template('add_password.html')
