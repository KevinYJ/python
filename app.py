from flask import Flask
from flask import request
from flask import render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', agent=user_agent)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/user/<int:uid>')
def displayuserid(uid):
    return '<h2>user id %s</h2>' % uid


if __name__ == '__main__':
    manager.run()
