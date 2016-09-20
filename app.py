from flask import Flask
import os

from models import db
import config
import views

app = Flask(__name__, static_url_path='')
self_path = os.path.dirname(os.path.abspath(__file__))
app.config.from_object(config.Config(app_root=self_path))
db.init_app(app)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True