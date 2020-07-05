from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/index')
@app.route('/')
def index():
    user = {
        'username': 'Ayushi',
        'address': 'JEC'
    }

    posts = [
       {
            'author': {'username': 'Jay'},
            'body': 'Aaj mausam bada beimaan hai!'
       },
       {
            'author': {'username': 'Taaniya'},
            'body': 'Kharab mausam hai!'
       }
    ]

    return render_template('index.html', user=user, posts=posts)


@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign in', form=form)
