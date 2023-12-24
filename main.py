from flask import Flask, render_template
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)

@socketio.on('join')
def on_join():
    send('Someone has joined the chat.', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
