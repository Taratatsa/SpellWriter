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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
