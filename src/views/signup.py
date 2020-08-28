from src import app
from flask import render_template

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')
