from flask_wtf import *
from wtforms import *
from wtforms.validators import *


class ModifierForm(FlaskForm):
    advantage = RadioField("Advantage", choices=[(1, "On"), (0, "Off")])
    disadvantage = RadioField("Disadvantage", choices=[(1, "On"), (0, "Off")])
    explode = RadioField("Explode", choices=[(1, "On"), (0, "Off")])
    cheater = RadioField("Cheater", choices=[(1, "On"), (0, "Off")])
    submit = SubmitField("Update")

