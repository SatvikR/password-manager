from flask import Flask
app = Flask(__name__)
app.secret_key = 'SECRET_KEY_HERE'

# App decleration must be first
import src.views
