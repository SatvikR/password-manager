from src import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html', logged_in=False, username='test_user')
