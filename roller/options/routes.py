from flask import *
from roller import db
from roller.models import *
from roller.options.forms import *


options = Blueprint("options", __name__)


@options.route("/modifiers")
def modifiers():
    return render_template("modifiers.html", title="Modifiers")


@options.route("/settings")
def settings():
    return render_template("settings.html", title="Settings")

