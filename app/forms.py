from flask.ext.wtf import Form
from wtforms import BooleanField, validators
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

class LoginForm(Form):
	openid = StringFiled('openid', validators=[InputRequired()])
	remember_me = BooleanField('remember_me', default=False)
