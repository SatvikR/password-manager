from src import app
import os

# This will run if running without flask cli

if os.getenv('FLASK_ENV') == "development":
    if __name__ == '__main__':
        app.run(port=3000, debug=True)
else:
    if __name__ == '__main__':
        app.run(port=3000, host='0.0.0.0')
