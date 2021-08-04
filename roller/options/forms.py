from flask_wtf import *
from wtforms import *
from wtforms.validators import *


class ModifierForm(FlaskForm):
    advantage = RadioField("Advantage", choices=[(True, "On"), (False, "Off")], default=False)
    disadvantage = RadioField("Disadvantage", choices=[(True, "On"), (False, "Off")], default=False)
    explode = RadioField("Explode", choices=[(True, "On"), (False, "Off")], default=False)
    cheater = RadioField("Cheater", choices=[(True, "On"), (False, "Off")], default=False)
    submit = SubmitField("Update")

