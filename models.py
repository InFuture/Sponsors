from flask_login import current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

import util

db = SQLAlchemy()
login_manager = LoginManager()

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.Unicode(128), unique=True)
	_password = db.Column("password", db.String(length=60))

	def __eq__(self, other):
		if isinstance(other, User):
			return self.id == other.id
		return NotImplemented

	@staticmethod
	@login_manager.user_loader
	def get_user_by_id(id):
		return User.get_by_id(id)

	@classmethod
	def get_user_by_email(cls, email):
		query_results = cls.query.filter(func.lower(User.email) == func.lower(email))
		return query_results.first() if query_results.count() else None

	@hybrid_property
	def password(self):
		return self._password

	@password.setter
	def password(self, password):
		self._password = util.hash_password(password)

	def check_password(self, password):
		return util.verify_password(password, self.password)
	