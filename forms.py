from flask_wtf import Form
from wtforms import ValidationError
from wtforms.fields import StringField, PasswordField
from wtforms.validators import InputRequired

from models import User

class LoginForm(Form):
	email = StringField("Email", validators=[InputRequired()])
	password = PasswordField("Password", validators=[InputRequired()])

	def get_user(self, email=None):
		return User.get_user_by_email(email)

	def validate_email(self, field):
		if self.get_user(field.data) is None: raise ValidationError("Invalid email/password.")

	def validate_password(self, field):
		user = self.get_user(field.data)
		if not user: return
		if not user.check_password(field.data): raise ValidationError("Invalid email/password.")