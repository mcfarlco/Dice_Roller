from flask import *
from roller import db
from roller.models import *
from roller.options.forms import *


options = Blueprint("options", __name__)


@options.route("/modifiers", methods=["GET", "POST"])
def modifiers():
    return render_template("modifiers.html", title="Modifiers")


@options.route("/settings", methods=["GET", "POST"])
def settings():
    return render_template("settings.html", title="Settings")

