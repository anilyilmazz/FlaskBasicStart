from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/need')
def need():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)