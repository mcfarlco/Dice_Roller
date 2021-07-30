import sys
from flask import *
from roller import db
from roller.models import *
from roller.options.forms import *


options = Blueprint("options", __name__)


@options.route("/modifiers", methods=["GET", "POST"])
def modifiers():
    mods = Modifiers.query.first()
    form = ModifierForm()
    form.advantage.data = mods.advantage
    form.disadvantage.data = mods.disadvantage
    form.explode.data = mods.explode
    form.cheater.data = mods.cheater

    if form.validate_on_submit():
        print("Submit Form Received")
        print(form.advantage.data)
        print(form.disadvantage.data)
        print(form.explode.data)
        print(form.cheater.data)
        mods.advantage = form.advantage.data
        mods.disadvantage = form.disadvantage.data
        mods.explode = form.explode.data
        mods.cheater = form.cheater.data
        print("============")
        print(mods)
        print("============")
        db.session.commit()
        
        return redirect(url_for("options.modifiers"))

    return render_template("modifiers.html", title="Modifiers", form=form)


@options.route("/settings", methods=["GET", "POST"])
def settings():
    return render_template("settings.html", title="Settings")

