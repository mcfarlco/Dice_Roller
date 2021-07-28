from flask import *
from roller import db
from roller.models import *
from roller.main.forms import *


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    roll_history = Roll_History.query.order_by(Roll_History.roll_id.desc())
    return render_template("home.html", roll_history=roll_history)


@main.route("/roll", methods=["GET", "POST"])
def roll():
    return render_template("roll.html", title="Roll")


@main.route("/multi-roll", methods=["GET", "POST"])
def multi_roll():
    return render_template("multi-roll.html", title="Multi-Roll")

