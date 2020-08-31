from src import app
from src.db import query
from flask import (
	render_template,
	session,
	redirect,
	url_for
)
from base64 import b64decode

@app.route('/view_password/<int:id>')
def view_password(id):
	if 'username' not in session:
		return redirect(url_for('login'))

	password = query("""SELECT website, password 
						FROM passwords
						WHERE uid IN (
							SELECT id
							FROM users
							WHERE username=?)
						AND id=?""", [session['username'], id])
	
	if not len(password): # Password not found
		return redirect(url_for('your_passwords'))
	
	website, password = password[0] # Destructures tuple

	decoded_password = b64decode(password.encode()).decode()

	context = {'password': decoded_password, 'website': website}

	return render_template('view_password.html', **context)