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

    if form.validate_on_submit():
        mods.advantage = int(form.advantage.data == 'True')
        mods.disadvantage = int(form.disadvantage.data == 'True')
        mods.explode = int(form.explode.data == 'True')
        mods.cheater = int(form.cheater.data == 'True')
        db.session.commit()
        
        return redirect(url_for("options.modifiers"))        

    form.advantage.default = mods.advantage
    form.disadvantage.default = mods.disadvantage
    form.explode.default = mods.explode
    form.cheater.default = mods.cheater
    form.process()

    return render_template("modifiers.html", title="Modifiers", form=form)


@options.route("/settings", methods=["GET", "POST"])
def settings():
    return render_template("settings.html", title="Settings")

