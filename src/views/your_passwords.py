from src import app
from flask import render_template

@app.route('/your_passwords')
def your_passwords():
    return render_template('your_passwords.html')
