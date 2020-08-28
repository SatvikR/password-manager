from src import app
from flask import render_template

@app.route('/add_password')
def add_password():
    return render_template('add_password.html')
