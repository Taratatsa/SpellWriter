#!/usr/bin/env python
"""
This module allows the writing of spells as described in The Gorilla of Destiny's
Spell Writing System, detailed in his Spell Writing Guide.

Reference : https://www.drivethrurpg.com/product_info.php?products_id=429711
"""

from dictionaries_generator import generate_binary_numbers_dictionaries

__author__ = 'Jules "Taratatsa" Lelay'
__copyright__ = "None"
__credits__ = ["Gorilla of Destiny"]

__license__ = "None"
__date__ = "2023.03.15"
__version__ = "0.0.1"
__maintainer__ = 'Jules "Taratatsa" Lelay'
__email__ = "jules.lilaille@gmail.com"
__status__ = "Development"

levels = list(range(10))
schools = ["abjuration",
           "conjuration",
           "divination",
           "enchantment",
           "evocation",
           "illusion",
           "necromancy",
           "transmutation"]
types = ["acid",
         "bludgeoning",
         "cold",
         "damage",
         "extra",
         "fire",
         "force",
         "lightning",
         "necrotic",
         "nonmagical",
         "force",
         "poison",
         "psychic",
         "radiant",
         "slashing",
         "thunder"]
areas = ["circle",
         "cone/sphere",
         "cone",
         "cube",
         "cylinder",
         "line",
         "multiple targets/sphere",
         "multiple targes",
         "single target/cone",
         "single target",
         "sphere/cylinder",
         "sphere",
         "square",
         "wall"]
ranges = ["10 feet radius", "100 feet line", "15 feet cone", "15 feet cube", "15 feet radius",
          "30 feet cone", "30 feet line", "30 feet radius", "5 feet radius", "60 feet cone",
          "60 feet line", "point (150 feet)", "point (30 feet)", "point (300 feet)",
          "point (5 feet)", "point (500 feet)", "point (60 feet)", "point (90 feet)", "self",
          "sight", "special", "touch"]
attributes = [levels, schools, types, areas, ranges]

length = (len(attributes)+1)
none = [0]*length

def get_binary_numbers(level: int, school: str, damage: str, area: str, reach: str):
    """
    Generate the binary numbers required to draw the spell as lists from the spell attributes.

    Parameters
    ----------
    level : int
        Spell level.
    school : str
        Spell school.
    damage : str
        damage type.
    area : str
        Spell area of effect.
    reach : str
        Spell range.

    Returns
    -------
    bin_level : list
        The binary number associated with the spell level as a list.
    bin_school : list
        The binary number associated with the spell school as a list.
    bin_type : list
        The binary number associated with the spell damage type as a list.
    bin_area : list
        The binary number associated with the spell area of effect as a list.
    bin_range : list
        The binary number associated with the spell range as a list.

    """
    binary_numbers_dictionaries = generate_binary_numbers_dictionaries(attributes)

    bin_level = binary_numbers_dictionaries[0][level]
    bin_school = binary_numbers_dictionaries[1][school]
    bin_type = binary_numbers_dictionaries[2][damage]
    bin_area = binary_numbers_dictionaries[3][area]
    bin_range = binary_numbers_dictionaries[4][reach]

    return bin_level, bin_school, bin_type, bin_area, bin_range

def main():
    """
    Ask for spell attributes and writing details before prompting the written spell.

    Returns
    -------
    None.

    """
    name = input("Input your spell's name: ").lower()
    input_level = input("Input your spell's level: ")
    input_school = input("Input your spell's school: ").lower()
    input_damage = input("Input your spell's damage type (\"none\" if irrelevant): ").lower()
    input_area = input("Input your spell's area type (\"none\" if irrelevant): ").lower()
    input_range = input("Input your spell's range (\"none\" if irrelevant): ").lower()

    try:
        level = int(input_level)
    except ValueError:
        print("Format error in level: Please state an integer")
        return
    bins = get_binary_numbers(level, input_school, input_damage, input_area, input_range)


if __name__ == "__main__":
    main()
