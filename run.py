import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_message(username, message):
    """ Add message to the messages list """
    messages.append("{}: {}".format(username, message))


def get_all_messages():
    """ get all messages and separate them with a `br`  """
    return "<br>".join(messages)


@app.route('/')
def index():
    """ Main page with instructions """
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """ Display Chat messages """
    return "<h1>Welcome, {0} </h1> {1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a New message and redirect back to chat page """
    add_message(username, message)
    return redirect("/" + username)
   

app.run(host=os.getenv('IP'),
        port=int(os.getenv('PORT')),
        debug=True)

