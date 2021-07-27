# Author: Corey McFarland


import tkinter as tk
from tkinter.ttk import *



class RGBEffect:
    """
    Class to represent movement of RGB colors.
    """

    def __init__(self):
        self._effect_name = "thing"
        self._effect_colors = [
            [0, 0, 0]                          # Red value, Green value, Blue value
        ]
        self._effect_timing = [
            [0, 0, 0, 0]                       # Position 1, Position 2, StartDelay (ms), Frequency (ms)
        ]

    def get_effect_name(self):
        """Method to get the name of the effect."""

        return

    def get_effect_colors(self):
        """Method to get the RGB values of the effect."""

        return

    def get_effect_timing(self):
        """Method to get the timings of the effect."""

        return


class Modifier:
    """
    Class to represent the effects of a modifier.
    """

    def __init__(self):
        self._mod_name = "Mod Name"             #
        self._mod_desc = "Mod Description"      #
        self._mod_mode = 0                      # 0: Disabled - 1: Enabled

    def get_desc(self):
        """Method to get the description of the modifier."""

        return

    def get_mod_name(self):
        """Method to get the name of the modifier."""

        return

    def set_desc(self):
        """Method to change the description of the modifier."""

        return

    def set_mod_name(self):
        """Method to change the name of the modifier."""

        return

    def enable_mod(self):
        """Method to enable the modifier."""

        return

    def disable_mod(self):
        """Method to disable the modifier."""

        return


class RollProfile:
    """
    Class to represent the current roll profile.
    """

    def __init__(self):
        self._roll_dice = [0, 0, 0, 0, 0, 0, 0, 0, 0]     # d2, d3, d4, d6, d8, d10, d12, d20, d100
        self._roll_mods = []

    def get_roll_dice(self):
        """Method to get the die in the current roll profile."""

        return

    def get_roll_mods(self):
        """Method to get the modifiers currently active."""

        return

    def add_die(self):
        """Method to add a die to the current roll profile."""

        return

    def rem_die(self):
        """Method to remove a die from the current roll profile."""

        return

    def clear_die(self):
        """Method to remove all die from the current roll profile."""

        return


class RollHistory:
    """
    Class to represent the roll history of the user.
    """

    def __init__(self):
        self._history_len = 10
        self._history_log = [
            [[], [], [], [], [], [], [], [], []]     # Xd2, Xd3, Xd4, Xd6, Xd8, Xd10, Xd12, Xd20, Xd100
        ]
        self._history_sums = []

    def get_hist_len(self):
        """Method to get the length of the history."""

        return

    def get_hist_log(self):
        """Method to get the roll history log."""

        return

    def get_hist_sum(self):
        """Method to get the log of the sum of each roll in the history."""

        return

    def set_hist_len(self):
        """Method to set the length of the history."""

        return

    def clear_hist(self):
        """Method to clear the history logs."""

        return

    def add_roll(self):
        """Method to add roll to the history."""

        return

    def change_roll_prof(self):
        """Method to update the roll profile to the selected roll."""

        return


class RangeProfile:
    """
    Class to represent a Range profile.
    """

    def __init__(self):
        self._range_num = []
        self._range_effect = "thing"

    def get_range(self):
        """Method to get the range of numbers for the Range profile."""

        return

    def get_range_effect(self):
        """Method to get the effect of the Range profile."""

        return

    def set_range(self):
        """Method to set the range of numbers for the Range profile."""

        return

    def set_range_effect(self):
        """Method to set the effect of the Range profile."""

        return


class RGBProfile:
    """
    Class to represent a Range profile.
    """

    def __init__(self):
        self._rgb_ranges = []
        self._rgb_name = "thing"

    def get_rgb_ranges(self):
        """Method to get the range of numbers for the RGB profile."""

        return

    def get_rgb_name(self):
        """Method to get the effect of the RGB profile."""

        return

    def set_rgb_ranges(self):
        """Method to set the range of numbers for the RGB profile."""

        return

    def set_rgb_name(self):
        """Method to set the effect of the RGB profile."""

        return


class DieProfile:
    """
    Class to represent the profile of a die.
    """

    def __init__(self):
        self._die_name = "thing"
        self._die_type = 2
        self._die_profile = 0

    def get_die_name(self):
        """Method to get the current name of the die."""

        return

    def get_die_type(self):
        """Method to get the current type of the die."""

        return

    def get_die_profile(self):
        """Method to get the current profile of the die."""

        return

    def set_die_name(self):
        """Method to set the name of the die."""

        return

    def set_die_type(self):
        """Method to set the type of the die."""

        return

    def set_die_profile(self):
        """Method to set the profile of the die."""

        return


class Settings:
    """Class to represent the settings of the app."""

    def __init__(self):
        self._var = "Setting"


class Roller:
    """Class to represent the list of all information."""

    def __init__(self):
        self._rgb_e = []
        self._modifiers = []
        self._settings = []
        self._rgb_p = []
        self._dice_p = []
        self._history = []

    def roll(self):

        return


def main():
    print("Roller main function")


if __name__ == "__main__":
    main()


