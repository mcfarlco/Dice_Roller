import random
from roller import db
from roller.models import *

def r_num(max):
    # Method to generate a random number with a new seed each time
    
    random.seed()
    result = random.randint(1, max)
    return result

def modify(high_num, i, modifiers):
    # Method to apply modifiers to a roll
    if modifiers[0] and modifiers[1]:
        val = r_num(high_num[i])

    elif modifiers[0]:
        val_1 = r_num(high_num[i])
        val_2 = r_num(high_num[i])

        if(val_1 < val_2):
            val = val_2
        
        else:
            val = val_1

    elif modifiers[1]:
        val_1 = r_num(high_num[i])
        val_2 = r_num(high_num[i])

        if(val_1 > val_2):
            val = val_2

        else:
            val = val_1
    
    else:
        val = 0

    return val


def single_dice(arr):
    # Method to return array for single die rolls
    for die in arr:
        if die == "d4":
            arr = [0, 0, 1, 0, 0, 0, 0, 0, 0]

        elif die == "d6":
            arr = [0, 0, 0, 1, 0, 0, 0, 0, 0]

        elif die == "d8":
            arr = [0, 0, 0, 0, 1, 0, 0, 0, 0]

        elif die == "d10":
            arr = [0, 0, 0, 0, 0, 1, 0, 0, 0]

        elif die == "d12":
            arr = [0, 0, 0, 0, 0, 0, 1, 0, 0]

        elif die == "d20":
            arr = [0, 0, 0, 0, 0, 0, 0, 1, 0]

        elif die == "d100":
            arr = [0, 0, 0, 0, 0, 0, 0, 0, 1]

    return arr

def roll_dice(arr, modifiers):
    # Method to roll a number of dice determined from the array and apply the effects of any modifiers.

    # Check for single die rolls
    if len(arr) == 1:
        arr = single_dice(arr)

    # Modifiers [advantage, disadvantage, explode, cheater]
    rolls = [[], [], [], [], [], [], [], [], []]
    high_num = [2, 3, 4, 6, 8, 10, 12, 20, 100]
    sum_val = 0
    n_die = sum(arr)

    # Iterate through dice
    for i, die in enumerate(arr):
        if int(die) > 0:
            for j in range(int(die)):
                # Check for modifiers to affect rolls.
                check = modify(high_num, i, modifiers)

                if modifiers[3]:
                    val = high_num[i]
                    rolls[i].append(val)
                    sum_val += val
                    continue

                elif check > 0:
                    val = check
                
                else:
                    val = r_num(high_num[i])
                
                # Add result to list and increment sum
                rolls[i].append(val)
                sum_val += val

                # Check for any necessary re-rolls
                if modifiers[2]:
                    while(val == high_num[i]):
                        check = modify(high_num, i, modifiers)

                        if check > 0:
                            val = check

                        else:
                            val = r_num(high_num[i])
                        
                        # Add re-rolls to list and increment sum
                        rolls[i].append(val)
                        sum_val += val               

    return arr, rolls, n_die, sum_val


def drop_tables():
    # Reset database tables
    db.drop_all()
    db.create_all()
    default_mods = Modifiers()
    db.session.add(default_mods)


def create_rgb_profiles():
    # RGB Profiles
    rainbow = Rgbprofile()
    rainbow.name = "Rainbow"
    db.session.add(rainbow)
    swirl = Rgbprofile()
    swirl.name = "Swirl"
    db.session.add(swirl)
    waterfall = Rgbprofile()
    waterfall.name = "Waterfall"
    waterfall.die = 6
    db.session.add(waterfall)


def create_range_profiles():
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


def create_rgb_effects():
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


def create_rgb_colors():
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

def create_animations():
    # Animations
    gif_blue = Animation()
    gif_blue.name = "blue.gif"
    db.session.add(gif_blue)
    gif_funnel = Animation()
    gif_funnel.name = "funnel.gif"
    gif_funnel.effect_id = '1'
    db.session.add(gif_funnel)
    gif_green = Animation()
    gif_green.name = "green.gif"
    db.session.add(gif_green)
    gif_orange = Animation()
    gif_orange.name = "orange.gif"
    db.session.add(gif_orange)
    gif_purple = Animation()
    gif_purple.name = "purple.gif"
    db.session.add(gif_purple)
    gif_radar = Animation()
    gif_radar.name = "radar.gif"
    gif_radar.effect_id = '2'
    db.session.add(gif_radar)
    gif_rainbow = Animation()
    gif_rainbow.name = "rainbow.gif"
    gif_rainbow.effect_id = '3'
    db.session.add(gif_rainbow)
    gif_red = Animation()
    gif_red.name = "red.gif"
    db.session.add(gif_red)
    gif_yellow = Animation()
    gif_yellow.name = "yellow.gif"
    db.session.add(gif_yellow)

def create_default_relationships():
    # Build profile relationships
    d20 = db.session.query(Rangeprofile).filter(Rangeprofile.id == '1').first()
    d20_2 = db.session.query(Rangeprofile).filter(Rangeprofile.id == '2').first()
    d6 = db.session.query(Rangeprofile).filter(Rangeprofile.id == '3').first()
    flash = db.session.query(Rgbeffect).filter(Rgbeffect.id == '1').first()
    spin = db.session.query(Rgbeffect).filter(Rgbeffect.id == '2').first()
    cycle = db.session.query(Rgbeffect).filter(Rgbeffect.id == '3').first()
    t_flash = db.session.query(Rgbeffect).filter(Rgbeffect.id == '1').all()
    t_spin = db.session.query(Rgbeffect).filter(Rgbeffect.id == '2').all()
    t_cycle = db.session.query(Rgbeffect).filter(Rgbeffect.id == '3').all()
    t_black = db.session.query(Rgbcolor).filter(Rgbcolor.id == '1').all()
    t_white = db.session.query(Rgbcolor).filter(Rgbcolor.id == '2').all()
    t_tri_color = db.session.query(Rgbcolor).filter(Rgbcolor.id.in_(['3', '4', '5'])).all()
    t_funnel = db.session.query(Animation).filter(Animation.id == '2').all()
    t_radar = db.session.query(Animation).filter(Animation.id == '6').all()
    t_rainbow = db.session.query(Animation).filter(Animation.id == '7').all()
    d20.rgb_effect = t_flash
    d20.rgb_colors = t_white
    flash.animation = t_radar
    d20_2.rgb_effect = t_spin
    d20_2.rgb_colors = t_black
    spin.animation = t_funnel
    d6.rgb_effect = t_cycle
    d6.rgb_colors = [color for color in t_tri_color]
    cycle.animation = t_rainbow
    db.session.add_all([d20, d20_2, d6, flash, spin, cycle])
    db.session.commit()
