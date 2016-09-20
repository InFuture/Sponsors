import os
import pathlib

class Config:
	def __init__(self, app_root=None):
		if app_root is None: self.app_root = pathlib.Path(os.path.dirname(os.path.abspath(__file)))
		else: self.app_root = pathlib.Path(app_root)
		
		self.SECRET_KEY = None
		self._load_secret_key()
		self.SQLALCHEMY_DATABASE_URI = self._get_database_url()
		self.SQLALCHEMY_TRACK_MODIFICATIONS = False
		self.TEMPLATES_AUTO_RELOAD = True

	def _load_secret_key(self):
		if "SECRET_KEY" in os.environ:
			self.SECRET_KEY = os.environ["SECRET_KEY"]
		else:
			secret_path = self.app_root / ".secret_key"
			if not os.path.exists(".secret_key"): open(".secret_key", "w").close()
			with secret_path.open("rb+") as secret_file:
				secret_file.seek(0)
				contents = secret_file.read()
				if not contents and len(contents) == 0:
					key = os.urandom(128)
					secret_file.write(key)
					secret_file.flush()
				else:
					key = contents
			self.SECRET_KEY = key

		return self.SECRET_KEY

	def _get_database_url(self):
		return os.getenv("DATABASE_URL", "")