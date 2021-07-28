from flask import *
from roller import db
from roller.models import *
from roller.main.forms import *


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/roll")
def roll():
    return render_template("roll.html", title="Roll")


@main.route("/multi-roll")
def multi_roll():
    return render_template("multi-roll.html", title="Multi-Roll")

