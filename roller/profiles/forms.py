from flask_wtf import *
from wtforms import *
from wtforms.validators import *

class RGB_ProfileForm(FlaskForm):
    name = StringField("Name", default="Name", render_kw={'readonly': True})
    id = IntegerField('id')
    delete = SubmitField("Delete")
    submit = SubmitField("Edit")


class Range_ProfileForm(FlaskForm):
    name = StringField("Name", default="Name")
    id = IntegerField('ID')
    delete = SubmitField("Delete")
    submit = SubmitField("Edit")


class RGB_EditForm(FlaskForm):
    name = StringField("Name", default="Name")
    id = IntegerField('id')
    submit = SubmitField("Update")


class Range_Profile_EditForm(FlaskForm):
    name = StringField("Name", default="Name")
    id = IntegerField('id')
    min_r = IntegerField('Bottom of range')
    max_r = IntegerField('Top of range')
    effect_id = IntegerField("RGB Effect ID")
    submit = SubmitField("Update")


class Color_EditForm(FlaskForm):
    color_id = IntegerField('Color ID')
    red = IntegerField('Red')
    green = IntegerField('Green')
    blue = IntegerField('Blue')
    effect_id = IntegerField("RGB Effect ID")
    range_id = IntegerField("Range ID")
    submit = SubmitField("✓")


class DieDropdownForm(FlaskForm):
    die = SelectField(
        "Die", choices=[("d4"), ("d6"), ("d8"), ("d10"), ("d12"), ("d20"), ("d100")])


class EffectDropdownForm(FlaskForm):
    effects = SelectField('Effect')
    id = IntegerField('ID')
    submit = SubmitField("Change")

class NewNameForm(FlaskForm):
    name = StringField("Name")
    effect = SelectField('Effect')
    id = IntegerField('id')
    submit = SubmitField("Create")
