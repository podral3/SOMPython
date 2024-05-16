import csv
import random
import numpy as np
from pandas import read_csv   
from math import sin, pi
from .SOM_XYZ.Square import Square
def generate_and_save_rgb_data(filename, n):

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['r', 'g', 'b', 'color'])  # Write the header row

        for _ in range(n):
            color_choice = random.choice(['red', 'green', 'blue'])
            if color_choice == 'red':
                r = 255
                g = 0  # Limit green for red dominance
                b = 0  # Limit blue for red dominance
                color = "red"
            elif color_choice == 'green':
                r = 0  # Limit red for green dominance
                g = 255
                b = 0  # Limit blue for green dominance
                color = "green"
            else:
                r = 0  # Limit red for blue dominance
                g = 0  # Limit green for blue dominance
                b = 255
                color = "blue"
            writer.writerow([r, g, b, color])

def generate_and_save_xyz_data(filename, x_range, y_range, angle_step):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x','y','z'])

        angle = 0
        for x in range(0,x_range):
            for y in range(0,y_range,):
                z = sin(angle)
                writer.writerow([x,y,z])
                angle += angle_step
            angle = 0        

generate_and_save_xyz_data('/Sample Data/SomXYZ.csv', 100, 100, 5 * pi / 180)