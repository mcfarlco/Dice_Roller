from flask_wtf import *
from wtforms import *
from wtforms.validators import *


class SingleRollForm(FlaskForm):
    roll = RadioField("roll", choices=[("d4"), ("d6"), ("d8"), ("d10"), ("d12"), ("d20"), ("d100")])
    submit = SubmitField("Roll")


class MultiRollForm(FlaskForm):
    d2 = IntegerField("d2", default=0)
    d3 = IntegerField("d3", default=0)
    d4 = IntegerField("d4", default=0)
    d6 = IntegerField("d6", default=0)
    d8 = IntegerField("d8", default=0)
    d10 = IntegerField("d10", default=0)
    d12 = IntegerField("d12", default=0)
    d20 = IntegerField("d20", default=0)
    d100 = IntegerField("d100", default=0)
    submit = SubmitField("Roll")

class RollHistoryForm(FlaskForm):
    d2 = IntegerField("d2", render_kw={'readonly': True})
    d3 = IntegerField("d3", render_kw={'readonly': True})
    d4 = IntegerField("d4", render_kw={'readonly': True})
    d6 = IntegerField("d6", render_kw={'readonly': True})
    d8 = IntegerField("d8", render_kw={'readonly': True})
    d10 = IntegerField("d10", render_kw={'readonly': True})
    d12 = IntegerField("d12", render_kw={'readonly': True})
    d20 = IntegerField("d20", render_kw={'readonly': True})
    d100 = IntegerField("d100", render_kw={'readonly': True})
    submit = SubmitField("Update")
