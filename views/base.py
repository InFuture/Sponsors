from flask import Blueprint, render_template
from flask_login import current_user, login_required
import pdb

blueprint = Blueprint("base", __name__, template_folder="templates")

@blueprint.route("/")
@login_required
def index():
	render_template("base/index.html")