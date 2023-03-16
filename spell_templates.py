#!/usr/bin/env python
"""
This module generates the points repartition templates for the main spell writer module.
"""

import matplotlib.pyplot as plt
import numpy as np

__author__ = 'Jules "Taratatsa" Lelay'
__copyright__ = "None"
__credits__ = ["Gorilla of Destiny"]

__license__ = "None"
__date__ = "2023.03.15"
__version__ = "0.0.1"
__maintainer__ = 'Jules "Taratatsa" Lelay'
__email__ = "jules.lilaille@gmail.com"
__status__ = "Development"

def custom_template(length: int):
    coordinates = []
    line = input("Input the " + length + " points you would like to use as template: ")
    while line != "":
        point = (float(f) for f in line.split())
        if len(point) != 2 :
            print("Wrong amount of coordinates. Please input 2 coordinates.")
            for point in coordinates:
                print(point[0],point[1])
            continue
        coordinates.append(point)
        line = input()
    coeff = int(input("Input linearity coefficient (0–100): "))
    function = eval(input("Input drawing function as a lambda (from two points): "))
    return coordinates, coeff, function

def wizard_template(length: int):
    coordinates = [(np.sin(2*np.pi/length*i), np.cos(2*np.pi/length*i)) for i in range(length)]
    function = lambda point1, point2, color: plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color=color)
    return coordinates, function

templates = {"wizard": wizard_template}

if __name__ == "__main__":
    coords = wizard_template(11)[0]
    
    fig, axs = plt.subplots(1, 1)
    axs.scatter(*zip(*coords), color="white", edgecolors="black")
    axs.set_aspect('equal', 'box')
    axs.set_title('WIzard Template', fontsize=14, fontweight="bold", pad=10)
    plt.axis('off')
    plt.plot