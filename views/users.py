from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user

from forms import LoginForm
from models import db, User

blueprint = Blueprint("users", __name__, template_folder="templates")

@blueprint.route("/login", methods=["GET", "POST"])
def login():
	login_form = LoginForm()
	if login_form.validate_on_submit():
		login_user(login_form.get_user())
		return redirect(url_for("base.index"))
	return render_template("users/login.html", login_form=login_form)