'''
This python script starts a Flask web application and
displays a text on the screen.

function:
    hello(): Displays a text on the screen
        return - Text

    hbnb(): Displays a text on the screen
        return - Text
'''

# Import the class Flask from flask module
from flask import Flask
from markupsafe import escape

# Create an instance of Flask class
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
    A function that returns a text

    return: a text
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    A function that returns a text

    return: a text
    '''
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    '''
    A function that returns a text

    return: a text
    '''
    text = text.replace('_', " ")
    return "C {}".format(escape(text))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
