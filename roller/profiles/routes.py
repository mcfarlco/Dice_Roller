from flask import *
from roller import db
from roller.models import *
from roller.profiles.forms import *


profiles = Blueprint("profiles", __name__)


@profiles.route("/customize", methods=["GET", "POST"])
def customize():
    die_dropdown = DieDropdownForm()

    # Generate list of all RGB profiles
    rgb_profiles = Rgbprofile.query.order_by(Rgbprofile.id.desc()).all()
    profile_forms = []
    for i, profile in enumerate(rgb_profiles):
        form = RGB_ProfileForm(prefix=profile.name)
        form.name.data = profile.name
        form.id.data = profile.id
        profile_forms.append(form)

    # Check for edit or delete request for each rgb profile
    for form in profile_forms:
        if form.validate_on_submit():
            if form.submit.data:
                return redirect(url_for("profiles.profile_edit", id=form.id.data, name=form.name.data))
            else:
                to_delete = Rgbprofile.query.filter(Rgbprofile.id == form.id.data)
                if to_delete is not None:
                    to_delete.delete()
                    db.session.commit()
                return redirect(url_for("profiles.customize"))
            

    return render_template("customize.html", title="Customize",
                            profile_forms = profile_forms, dropdown = die_dropdown)


@profiles.route("/profile_edit", methods=["GET", "POST"])
def profile_edit():
    p_id = request.args.get('id')
    name = request.args.get('name')
    profile = Rgbprofile.query.get_or_404(p_id)
    range_profiles = Rangeprofile.query.order_by(Rangeprofile.id.desc()).filter(Rangeprofile.rgb_id == p_id)

    # Generate form for each range profile in the RGB profile
    range_forms = []
    for profile in range_profiles:
        form = Range_ProfileForm(prefix=profile.name)
        form.name.data = profile.name
        form.id.data = profile.id
        range_forms.append(form)
    
    # Check for edit or delete request for each range profile
    for form in range_forms:
        if form.validate_on_submit():
            if form.submit.data:
                return redirect(url_for("profiles.range_edit", id=form.id.data, name=form.name.data, rgb_id=p_id))
            else:
                to_delete = Rangeprofile.query.filter(Rangeprofile.id == form.id.data)
                if to_delete is not None:
                    to_delete.delete()
                    db.session.commit()
                return redirect(url_for("profiles.profile_edit", id=p_id, name=name))


    return render_template("profile-edit.html", title="Edit Profile",
     range_forms=range_forms, name=name, p_id=p_id)


@profiles.route("/profile_edit/new", methods=["GET", "POST"])
def profile_new():
    form = NewNameForm()
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
    cur_eff = Rgbeffect.query.filter(Rgbeffect.effect_range.any(id=profile.id)).first()
    range_colors = Rgbcolor.query.filter(Rgbcolor.range_color.any(id=profile.id)).all()

    # Check if profile is new and has no effect
    if cur_eff is None:
        cur_eff = Rgbeffect.query.first()

    # Update form with queried information
    range_edit = Range_Profile_EditForm()
    range_edit.min_r.data = profile.min_r
    range_edit.max_r.data = profile.max_r
    num_colors = cur_eff.num_colors
    animation = Animation.query.filter(Animation.effect_id == cur_eff.id).first()

    # Get dropdown of all RGB Effects
    effects = Rgbeffect.query.order_by(Rgbeffect.name).all()
    eff_dropdown = EffectDropdownForm()
    choices = []
    for effect in effects:
        tup = (effect.id, effect.name)
        choices.append(tup)
    eff_dropdown.effects.choices = choices

    color_forms = []
    for i in range(cur_eff.num_colors):
        # Create color form for each color in RGB effect
        color = range_colors[i]
        form = Color_EditForm(prefix=str(color.id))
        form.red.data = color.red
        form.green.data = color.green
        form.blue.data = color.blue
        form.effect_id.data = cur_eff.id
        form.color_id.data = color.id
        color_forms.append(form)

    if range_edit.validate_on_submit():
        # Update range profile
        profile.min_r = range_edit.min_r.data
        profile.max_r = range_edit.max_r.data
        new_effect = Rgbeffect.query.filter(Rgbeffect.id == eff_dropdown.effects.data).first()
        profile.rgb_effect = new_effect
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for("profiles.range_edit", id=r_id, name=r_name, rgb_id=rgb_id))

    for form in color_forms:
        # Iterate through each color to check for update
        if form.submit.data and form.validate_on_submit():
            color_q = Rgbcolor.query.filter(Rgbcolor.id == form.color_id.data).first()
            color_q.red = form.red.data
            color_q.green = form.green.data
            color_q.blue = form.blue.data
            db.session.add(color_q)
            db.session.commit()
            return redirect(url_for("profiles.range_edit", id=r_id, name=r_name, rgb_id=rgb_id))

    return render_template("range-edit.html", title="Edit Range",
                            eff_dropdown = eff_dropdown, name=r_name, num_colors=num_colors,
                            range_edit=range_edit, color_forms=color_forms, animation=animation)


@profiles.route("/range_edit/new", methods=["GET", "POST"])
def range_new():
    rgb_id = request.args.get('rgb_id')
    form = NewNameForm()

    # Get dropdown list of all RGB effects
    effects = Rgbeffect.query.order_by(Rgbeffect.name).all()
    choices = []
    for effect in effects:
        tup = (effect.id, effect.name)
        choices.append(tup)
    form.effect.choices = choices

    if form.validate_on_submit():
        # Get number of colors for effect and add new colors for the range
        range_effect = db.session.query(Rgbeffect).filter(Rgbeffect.id == form.effect.data).all()
        colors = []
        for i in range(range_effect[0].num_colors):
            colors.append(0)
            colors[i] = Rgbcolor()

        # Add new range
        new_range = Rangeprofile(name=form.name.data, rgb_id=rgb_id)
        db.session.add(new_range)

        # Add range to color relationship
        new_range.rgb_colors = [color for color in colors]
        new_range.rgb_effect = range_effect
        db.session.add(new_range)

        db.session.commit()

        return redirect(url_for("profiles.range_edit", id=new_range.id, name=new_range.name))

    return render_template("range-new.html", title="New Range", form=form)


# TO IMPLEMENT WITH BLUETOOTH CONNECTIVITY
# @profiles.route("/connect", methods=["GET", "POST"])
# def connect():
#     return render_template("connect.html", title="Connect")
