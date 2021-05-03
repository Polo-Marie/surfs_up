from flask import Flask

# Create ab app, being sure to pass__name__
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

export FLASK_APP=app.py
    flask run

#if __name__ == "__main__":
    #app.run()
