from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.widgets import TextArea

class MessageForm(FlaskForm):
	message = StringField('Message', widget=TextArea())
	send = SubmitField('send')