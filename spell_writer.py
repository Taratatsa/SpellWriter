#!/usr/bin/env python
"""
This module allows the writing of spells as described in The Gorilla of Destiny's
Spell Writing System, detailed in his Spell Writing Guide.

Reference : https://www.drivethrurpg.com/product_info.php?products_id=429711
"""

__author__ = 'Jules "Taratatsa" Lelay'
__copyright__ = "None"
__credits__ = ["Gorilla of Destiny"]

__license__ = "None"
__date__ = "2023.03.15"
__version__ = "0.0.1"
__maintainer__ = 'Jules "Taratatsa" Lelay'
__email__ = "jules.lilaille@gmail.com"
__status__ = "Development"

def main():
    """
    Ask for spell and writing details before prompting the written spell

    Returns
    -------
    None.

    """
    name = input("Input your spell's name: ").capitalize()
    input_level = input("Input your spell's level: ")
    input_school = input("Input your spell's school: ").capitalize()
    input_type = input("Input your spell's damage type (\"none\" if irrelevant): ").capitalize()
    input_area = input("Input your spell's area type (\"none\" if irrelevant): ").capitalize()
    input_range = input("Input your spell's range (\"none\" if irrelevant): ").capitalize()

    try:
        level = int(input_level)
    except ValueError:
        print("Format error in level: Please state an integer")
        return

if __name__ == "__main__":
    main()
