#!/usr/bin/python3
from flask import Flask, redirect, make_response, url_for, request, render_template
from flask import session
app = Flask(__name__)
app.secret_key = 'any random string'
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/student')
def student():
    return render_template("form.html")

@app.route('/table')
def sfgg():
    return render_template("form.html")

@app.route('/hello/<name>')
def Hello_world(name):
    return f'Flask {name.capitalize()}!'

@app.route('/welcome/<name>')
def welcome(name):
    return f'Welcome {name.capitalize()}!'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for("welcome", name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for("welcome", name=user))
    
@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == "POST":
        result = request.form
        print(result)
        return render_template("table.html", result=result)

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method =="POST":
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    if name:
        return '<h1>welcome '+ name +'</h1>'
    else:
        return '<h1>Cookie not set. Please set cookie first.</h2>'

@app.route('/cookie')
def cookie():
    return render_template("setcookie.html")

@app.route('/session')
def session():
    if 'username' in session:
        username = session['username']
        return'Logged in as ' + username + '<br>'+ \
            "<b><a href='/logout'>click here to logout</a></b>"
    return "You are not logged in <br><a href='/login'> </b>"

if __name__ == "__main__":
    app.run(debug=True)
