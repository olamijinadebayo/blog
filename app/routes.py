from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Miguel'}
    posts = [
        {
            'author':{'username':'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author':{'username':'Debby'},
            'body': 'There is no place like home'
        }
    ]
    return render_template('index.html', title ='Home',user = user,posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title ='Sign in',form = form)