from flask import Flask, render_template, request, session
from functools import wraps
from models import Session,Users

app = Flask(__name__)

def loginControl(function):
    @wraps(function)
    def wrapper():
        if session.get('username'):
            return function()
        else:
            return render_template('index.html')
    return wrapper

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
@loginControl
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return render_template('index.html')
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #session['username'] = request.form['username']
        newUser = Users(username=request.form['email'],
                        password=request.form['password'],
                        email=request.form['email'])
        print(newUser)
        return render_template('index.html')
    if request.method == 'GET':
        return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)