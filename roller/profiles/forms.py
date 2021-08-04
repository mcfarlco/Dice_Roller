from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class RGB_Profile(FlaskForm):
    name = StringField("Name", default="Name", render_kw={'readonly': True})
    id = IntegerField('id')
    submit = SubmitField("Edit")


class Roll_Profile(FlaskForm):
    name = StringField("Name", default="Name")
    id = IntegerField('id')
    submit = SubmitField("Edit")


class RGB_Edit(FlaskForm):
    name = StringField("Name", default="Name")
    id = IntegerField('id')
    submit = SubmitField("Update")


class Roll_Profile_Edit(FlaskForm):
    name = StringField("Name", default="Name")
    id = IntegerField('id')
    submit = SubmitField("Update")


class DieDropdown(FlaskForm):
    die = SelectField(
        "Die", choices=[("d4"), ("d6"), ("d8"), ("d10"), ("d12"), ("d20"), ("d100")])


class EffectDropdown(FlaskForm):
    effects = SelectField('Effect')

class NewName(FlaskForm):
    name = StringField("Name")
    id = IntegerField('id')
    submit = SubmitField("Create")
