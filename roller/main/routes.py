from roller.profiles.forms import RGB_ProfileForm
from typing import SupportsIndex
from flask import *
from roller import db
from roller.models import *
from roller.main.forms import *
from roller.main.roll import *


main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    roll_history = Rollhistory.query.order_by(Rollhistory.roll_id.desc())
    return render_template("home.html", roll_history=roll_history)


@main.route("/roll", methods=["GET", "POST"])
def roll():
    form = SingleRollForm()
    roll_form = RollHistoryForm()
    roll_history = Rollhistory.query.order_by(Rollhistory.roll_id.desc())
    mods = Modifiers.query.first()
    modifiers = [mods.advantage, mods.disadvantage, mods.explode, mods.cheater]
    
    if form.validate_on_submit():
        # Add new roll to roll history
        die = {form.roll.data}
        rolls, results, num_die, total = roll_dice(die, modifiers)
        new_roll = Rollhistory(n_die=num_die, sum_die=total, d2=rolls[0], d3=rolls[1], d4=rolls[2], 
                                d6=rolls[3], d8=rolls[4], d10=rolls[5], 
                                d12=rolls[6], d20=rolls[7], d100=rolls[8])
        
        db.session.add(new_roll)
        db.session.commit()
        new_roll = Rollhistory.query.order_by(Rollhistory.roll_id.desc()).first()

        # Update results tables 
        table_names = [D2_Results, D3_Results, D4_Results, 
                        D6_Results, D8_Results, D10_Results, 
                        D12_Results, D20_Results, D100_Results]

        for i, die in enumerate(results):
            for value in die:
                __tablename__ = table_names[i]
                new_result = __tablename__(result=value, roll_id=new_roll.roll_id)
                db.session.add(new_result)
                db.session.commit()

        # Check row count for display
        rows = db.session.query(Rollhistory).count()

        if rows > 20:
            to_delete = Rollhistory.query.first()
            db.session.delete(to_delete)
            db.session.commit()

        flash(f"Roll accepted for {form.roll.data}", "success")
        return redirect(url_for("main.roll"))
    return render_template("roll.html", title="Roll", form=form, roll_form=roll_form, roll_history=roll_history)


@main.route("/multi-roll", methods=["GET", "POST"])
def multi_roll():
    form = MultiRollForm()
    roll_form = RollHistoryForm()
    roll_history = Rollhistory.query.order_by(Rollhistory.roll_id.desc())
    mods = Modifiers.query.first()
    modifiers = [mods.advantage, mods.disadvantage, mods.explode, mods.cheater]


    if form.validate_on_submit():
        # Add new roll to roll history
        dice = [form.d2.data, form.d3.data, form.d4.data,
                form.d6.data, form.d8.data, form.d10.data,
                form.d12.data, form.d20.data, form.d100.data]

        if sum(dice) == 0:
            flash(f"No dice rolled", "warning")
            return redirect(url_for("main.multi_roll"))

        rolls, results, num_die, total = roll_dice(dice, modifiers)
        new_roll = Rollhistory(n_die=num_die, sum_die=total, d2=rolls[0], d3=rolls[1], d4=rolls[2], 
                                d6=rolls[3], d8=rolls[4], d10=rolls[5], 
                                d12=rolls[6], d20=rolls[7], d100=rolls[8])
        
        db.session.add(new_roll)
        db.session.commit()
        new_roll = Rollhistory.query.order_by(Rollhistory.roll_id.desc()).first()

        # Update results tables 
        table_names = [D2_Results, D3_Results, D4_Results, 
                        D6_Results, D8_Results, D10_Results, 
                        D12_Results, D20_Results, D100_Results]

        for i, die in enumerate(results):
            for value in die:
                __tablename__ = table_names[i]
                new_result = __tablename__(result=value, roll_id=new_roll.roll_id)
                db.session.add(new_result)
                db.session.commit()

        # Check row count for display
        rows = db.session.query(Rollhistory).count()

        if rows > 20:
            to_delete = Rollhistory.query.first()
            db.session.delete(to_delete)
            db.session.commit()

        return redirect(url_for("main.multi_roll"))
    return render_template("multi-roll.html", title="Multi-Roll", form=form, roll_form=roll_form, roll_history=roll_history)

@main.route("/reset")
def reset():
    # Reset database tables
    db.drop_all()
    db.create_all()
    default_mods = Modifiers()
    db.session.add(default_mods)

    # RGB Profiles
    rainbow = Rgbprofile()
    rainbow.name = "Rainbow"
    db.session.add(rainbow)
    swirl = Rgbprofile()
    swirl.name = "Swirl"
    db.session.add(swirl)
    waterfall = Rgbprofile()
    waterfall.name = "Waterfall"
    db.session.add(waterfall)

    # Range Profiles
    d20 = Rangeprofile()
    d20.name = "1 - 20"
    d20.min_r = 1
    d20.max_r = 20
    d20.rgb_id = '1'
    db.session.add(d20)
    d20_2 = Rangeprofile()
    d20_2.name = "1 - 20"
    d20_2.min_r = 1
    d20_2.max_r = 20
    d20_2.rgb_id = '2'
    db.session.add(d20_2)
    d6 = Rangeprofile()
    d6.name = "1 - 6"
    d6.min_r = 1
    d6.max_r = 6
    d6.rgb_id = '3'
    db.session.add(d6)

    # RGB Effects
    flash = Rgbeffect()
    flash.name = "Flash"
    flash.num_colors = 1
    db.session.add(flash)
    spin = Rgbeffect()
    spin.name = "Spin"
    spin.num_colors = 1
    db.session.add(spin)
    cycle = Rgbeffect()
    cycle.name = "Cycle"
    cycle.num_colors = 3
    db.session.add(cycle)

    # RGB Colors
    black = Rgbcolor()
    db.session.add(black)
    white = Rgbcolor()
    white.red = 255
    white.green = 255
    white.blue = 255
    db.session.add(white)
    red = Rgbcolor()
    red.red = 255
    db.session.add(red)
    green = Rgbcolor()
    green.green = 255
    db.session.add(green)
    blue = Rgbcolor()
    blue.blue = 255
    db.session.add(blue)

    db.session.commit()

    # Build profile relationships
    t_flash = db.session.query(Rgbeffect).filter(Rgbeffect.id == '1').all()
    t_spin = db.session.query(Rgbeffect).filter(Rgbeffect.id == '2').all()
    t_cycle = db.session.query(Rgbeffect).filter(Rgbeffect.id == '3').all()
    t_black = db.session.query(Rgbcolor).filter(Rgbcolor.id == '1').all()
    t_white = db.session.query(Rgbcolor).filter(Rgbcolor.id == '2').all()
    t_tri_color = db.session.query(Rgbcolor).filter(Rgbcolor.id.in_(['3', '4', '5'])).all()
    d20.rgb_effect = t_flash
    d20.rgb_colors = t_white
    flash.rgb_colors = t_white
    d20_2.rgb_effect = t_spin
    d20_2.rgb_colors = t_black
    spin.rgb_colors = t_black
    d6.rgb_effect = t_cycle
    d6.rgb_colors = [color for color in t_tri_color]
    cycle.rgb_colors = [color for color in t_tri_color]
    db.session.add_all([d20, d20_2, d6, flash, spin, cycle])
    db.session.commit()
    
    return redirect(url_for("main.home"))
