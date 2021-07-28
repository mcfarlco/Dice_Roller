from flask import *
from roller import db
from roller.models import *
from roller.profiles.forms import *


profiles = Blueprint("profiles", __name__)


@profiles.route("/connect")
def connect():
    return render_template("connect.html", title="Connect")


@profiles.route("/customize", methods=["GET", "POST"])
def customize():
    return render_template("customize.html", title="Customize")
