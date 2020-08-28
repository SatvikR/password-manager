from flask import Flask
app = Flask(__name__)
app.secret_key = 'SECRET_KEY_HERE'

import src.views
