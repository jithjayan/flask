from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def Home():
    return "welcome"

@app.route('/home1')
def Home1():
    return "welcome1"

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/secpage')
def secpage():
    return render_template('secpage.html')

app.run()