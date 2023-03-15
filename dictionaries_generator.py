#!/usr/bin/env python
"""
This module generates the necessary sets for the main spell writer module.
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

from copy import deepcopy
import itertools

def generate_binary_numbers_list(length: int):
    """
    Generate a binary numbers list excluding cyclic pairs.

    Parameters
    ----------
    length : int
        length of the desired binary numbers.

    Returns
    -------
    binary_numbers_list : list
        a binary numbers list excluding cyclic pairs as long as desired.
    
    >>> generate_binary_numbers_list(4)
    [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1]]
    >>> len(generate_binary_numbers_list(13))
    632
    """
    binary_numbers_list = [list(i) for i in itertools.product([0, 1], repeat=length)]

    i = 1
    while i < len(binary_numbers_list)-1:
        number = deepcopy(binary_numbers_list[i])
        number.append(number.pop(0))
        while number != binary_numbers_list[i]:
            if number in binary_numbers_list:
                binary_numbers_list.remove(number)
            number.append(number.pop(0))
        i+=1

    return binary_numbers_list

def generate_binary_numbers_dictionaries(attributes: list):
    """
    >>> levels = list(range(10))
    >>> schools = ["abjuration", "conjuration", "divination", "enchantment", "evocation",\
                   "illusion", "necromancy", "transmutation"]
    >>> types = ["acid", "bludgeoning", "cold", "damage", "extra", "fire", "force",\
                 "lightning", "necrotic", "nonmagical", "force", "poison",\
                 "psychic", "radiant", "slashing", "thunder"]
    >>> areas = ["circle", "cone/sphere", "cone", "cube", "cylinder", "line",\
                 "multiple targets/sphere", "multiple targes", "none",\
                 "single target/cone", "single target", "sphere/cylinder", "sphere", \
                 "square", "wall"]
    >>> ranges = ["10 feet radius", "100 feet line", "15 feet cone", "15 feet cube",\
                  "15 feet radius", "30 feet cone", "30 feet line", "30 feet radius",\
                  "5 feet radius", "60 feet cone", "60 feet line", "point (150 feet)",\
                  "point (30 feet)", "point (300 feet)", "point (5 feet)", "point (500 feet)",\
                  "point (60 feet)", "point (90 feet)", "self", "sight", "special", "touch"]
    >>> attributes = [levels, schools, types, areas, ranges]
    >>> binary_numbers_dictionaries = generate_binary_numbers_dictionaries(attributes)
    >>> len(binary_numbers_dictionaries)
    5
    >>> len(binary_numbers_dictionaries[0])
    10
    >>> len(binary_numbers_dictionaries[0][0])
    11
    >>> binary_numbers_dictionaries[1]
    {'abjuration': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 'conjuration': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], 'divination': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 'enchantment': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 'evocation': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 'illusion': [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], 'necromancy': [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], 'transmutation': [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]}
    """
    binary_numbers_list = generate_binary_numbers_list(len(attributes)*2+1)
    binary_numbers_dictionaries = [dict(zip(attribute, binary_numbers_list[1:]))
                                   for attribute in attributes]
    return binary_numbers_dictionaries

if __name__ == "__main__":
    import doctest
    doctest.testmod()
