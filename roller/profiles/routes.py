from flask import *
from roller import db
from roller.models import *
from roller.profiles.forms import *


profiles = Blueprint("profiles", __name__)


@profiles.route("/connect", methods=["GET", "POST"])
def connect():
    return render_template("connect.html", title="Connect")


@profiles.route("/customize", methods=["GET", "POST"])
def customize():
    die_dropdown = DieDropdown()
    rgb_profiles = Rgbprofile.query.order_by(Rgbprofile.id.desc()).all()
    profile_forms = []
    for i, profile in enumerate(rgb_profiles):
        form = RGB_Profile(prefix=profile.name)
        form.name.data = profile.name
        form.id.data = profile.id
        profile_forms.append(form)

    for form in profile_forms:
        if form.submit.data and form.validate_on_submit():
            return redirect(url_for("profiles.profile_edit", id=form.id.data, name=form.name.data))

    return render_template("customize.html", title="Customize", profile_forms = profile_forms, dropdown = die_dropdown)


@profiles.route("/profile_edit", methods=["GET", "POST"])
def profile_edit():
    p_id = request.args.get('id')
    name = request.args.get('name')
    profile = Rgbprofile.query.get_or_404(p_id)
    range_profiles = Rangeprofile.query.order_by(Rangeprofile.id.desc()).filter(Rangeprofile.rgb_id == p_id)
    range_forms = []
    for i, profile in enumerate(range_profiles):
        form = RGB_Profile(prefix=profile.name)
        form.name.data = profile.name
        form.id.data = profile.id
        range_forms.append(form)
    
    for form in range_forms:
        if form.submit.data and form.validate_on_submit():
            return redirect(url_for("profiles.range_edit", id=form.id.data, name=form.name.data, rgb_id=p_id))

    return render_template("profile-edit.html", title="Edit Profile", range_forms=range_forms, name=name, p_id=p_id)


@profiles.route("/profile_edit/new", methods=["GET", "POST"])
def profile_new():
    form = NewName()
    if form.validate_on_submit():
        new_profile = Rgbprofile(name=form.name.data)
        db.session.add(new_profile)
        db.session.commit()
        
        return redirect(url_for("profiles.profile_edit", id=new_profile.id, name=new_profile.name))

    return render_template("profile-new.html", title="New Profile", form=form)


@profiles.route("/range_edit", methods=["GET", "POST"])
def range_edit():
    r_name = request.args.get('name')
    r_id = request.args.get('id')
    rgb_id = request.args.get('rgb_id')
    profile = Rangeprofile.query.get_or_404(int(r_id))
    effects = Rgbeffect.query.order_by(Rgbeffect.name).all()

    eff_dropdown = EffectDropdown()
    choices = []
    for effect in effects:
        choices.append(effect.name)
    eff_dropdown.effects.choices = choices

    return render_template("range-edit.html", title="Edit Range", eff_dropdown = eff_dropdown, name=r_name)


@profiles.route("/range_edit/new", methods=["GET", "POST"])
def range_new():
    rgb_id = request.args.get('rgb_id')
    form = NewName()

    if form.validate_on_submit():
        new_range = Rangeprofile(name=form.name.data, rgb_id=rgb_id)
        db.session.add(new_range)
        db.session.commit()

        return redirect(url_for("profiles.range_edit", id=new_range.id, name=new_range.name))

    return render_template("range-new.html", title="New Range", form=form)
