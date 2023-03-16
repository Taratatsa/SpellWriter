#!/usr/bin/env python
"""
This module allows the writing of spells as described in The Gorilla of Destiny's
Spell Writing System, detailed in his Spell Writing Guide.

Reference : https://www.drivethrurpg.com/product_info.php?products_id=429711
"""

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from dictionaries_generator import generate_binary_numbers_dictionaries
from spell_templates import templates

__author__ = 'Jules "Taratatsa" Lelay'
__copyright__ = "None"
__credits__ = ["Gorilla of Destiny"]

__license__ = "None"
__date__ = "2023.03.15"
__version__ = "0.0.1"
__maintainer__ = 'Jules "Taratatsa" Lelay'
__email__ = "jules.lilaille@gmail.com"
__status__ = "Development"

levels = [str(i) for i in range(10)]
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
ranges = ["10 feet radius",
          "100 feet line",
          "15 feet cone",
          "15 feet cube",
          "15 feet radius",
          "30 feet cone",
          "30 feet line", 
          "30 feet radius",
          "5 feet radius",
          "60 feet cone",
          "60 feet line",
          "point (150 feet)",
          "point (30 feet)",
          "point (300 feet)",
          "point (5 feet)",
          "point (500 feet)",
          "point (60 feet)",
          "point (90 feet)",
          "self",
          "sight",
          "special",
          "touch"]
attributes = [["none"]+levels, ["none"]+schools, ["none"]+types, ["none"]+areas, ["none"]+ranges]
length = len(attributes)*2+1

def get_binary_numbers(level: str, school: str, damage: str, area: str, reach: str):
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

    >>> get_binary_numbers("0", "none", "none", "none", "none")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> get_binary_numbers("0", "1", "0", "1", "0")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """
    binary_numbers_dictionaries = generate_binary_numbers_dictionaries(attributes)

    binary_numbers = []
    entries = [level, school, damage, area, reach]
    for attribute in entries:
        try:
            index = entries.index(attribute)
            binary_numbers.append(binary_numbers_dictionaries[index][attribute])
        except KeyError:
            print(attribute + " not recognized, defaulting to none.")
            binary_numbers.append(binary_numbers_dictionaries[index]["none"])

    return binary_numbers

def write_spell(name: str, binary_numbers: list, template: str, mode: str):
    try:
        coordinates, function = templates[template](length)
    except KeyError:
        print("Unknown template")
        return

    fig, axs = plt.subplots(1, 1)
    axs.scatter(*zip(*coordinates), color="white", edgecolors="black")
    k=1
    for binary_number in binary_numbers:
        for i in range(length):
            if binary_number[i] == 1:
                color = "black" if mode=="bw" else list(mcolors.TABLEAU_COLORS.keys())[k-1]
                function(coordinates[i], coordinates[(i+k)%length], color)
        k+=1
    axs.set_aspect('equal', 'box')
    axs.set_title(name, fontsize=14, pad=10)
    plt.axis('off')
    plt.show()

def main():
    """
    Ask for spell attributes and writing details before prompting the written spell.

    Returns
    -------
    None.

    """
    template = input("Input the template you would like to use (custom if irrelevant): ").lower()
    name = input("Input your spell's name: ").capitalize()
    input_level = input("Input your spell's level: ")
    input_school = input("Input your spell's school: ").lower()
    input_damage = input("Input your spell's damage type (\"none\" if irrelevant): ").lower()
    input_area = input("Input your spell's area type (\"none\" if irrelevant): ").lower()
    input_range = input("Input your spell's range (\"none\" if irrelevant): ").lower()
    mode = input("Input your writing mode (\"bw\" or colors): ").lower()

    bins = get_binary_numbers(input_level, input_school, input_damage, input_area, input_range)

    write_spell(name, bins, template, mode)

if __name__ == "__main__":
    main()
