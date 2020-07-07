from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
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


@app.route('/login', methods=["GET", "POST"])
def login():
  form = LoginForm()

  if form.validate_on_submit():
    flash('{} attempted to log in..'.format(form.username.data))
    return redirect(url_for('index'))

  return render_template('login.html', title='Sign in', form=form)


