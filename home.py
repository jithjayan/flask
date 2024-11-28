from flask import Flask,render_template,request
import sqlite3
con=sqlite3.connect('/home/novavi/Documents/jith/flask/dtb.db')
try:
    con.execute("create table std(name text,age int,email email)")
except:
    pass
app=Flask(__name__)

@app.route('/')
def Home():
    return "welcome"

@app.route('/home1')
def Home1():
    return "welcome1"

@app.route('/index',methods=['GET','POST'])
def index():

    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        email=request.form.get('email')
        print(name,age,email)
        con=sqlite3.connect('/home/novavi/Documents/jith/flask/dtb.db')
        con.execute("insert into std(name,age,email)values(?,?,?)",(name,age,email))
        con.commit()
    return render_template('index.html')

@app.route('/secpage')
def secpage():
    return render_template('secpage.html')

app.run()