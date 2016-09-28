from flask import Flask, redirect, url_for
import os

from models import db, login_manager
import config
import views

app = Flask(__name__, static_url_path='')
self_path = os.path.dirname(os.path.abspath(__file__))
app.config.from_object(config.Config(app_root=self_path))
db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(views.base.blueprint)
app.register_blueprint(views.users.blueprint)

@app.errorhandler(401)
def login(error):
	return redirect(url_for("users.login"))

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True