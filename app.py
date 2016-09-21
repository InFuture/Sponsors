from flask import Flask, render_template
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

@app.errorhandler(401)
def login(error):
	return render_template("base/login.html")

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True