from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

import util

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.Unicode(128), unique=True)
	_password = db.Column("password", db.String(length=60))

	def __eq__(self, other):
		if isinstance(other, User):
			return self.id == other.id
		return NotImplemented

	@hybrid_property
	def password(self):
		return self._password

	@password.setter
	def password(self, password):
		self._password = util.hash_password(password)

	def check_password(self, password):
		return util.verify_password(password, self.password)
	