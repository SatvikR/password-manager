from src import app

# This will run if running without flask cli
if __name__ == '__main__':
    app.run(port=3000, debug=True)
