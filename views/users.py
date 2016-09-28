from flask import Blueprint, render_template
from flask_login import current_user, login_required

from forms import LoginForm
from models import db, User

blueprint = Blueprint("users", __name__, template_folder="templates")

@blueprint.route("/login")
def login():
	login_form = LoginForm()
	if login_form.validate_on_submit():
		return redirect(url_for("base.index"))
	return render_template("users/login.html", login_form=login_form)