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

def generate_adn_save_xyz_data(filename, x_range, y_range, angle_step):
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

def group_array(data, x_jump, y_jump):
    x_segments_count = int((max(data[:,0]) - min(data[:,0])) / x_jump)
    y_segments_count = int((max(data[:,1]) - min(data[:,1])) / y_jump)
    segmented_points = np.zeros((x_segments_count+1, y_segments_count+1), dtype=object)

    x = min(data[:,0])
    y = min(data[:,1])

    x_iterator = x_segments_count
    while(x_iterator >= 0):
       y_iterator = y_segments_count
       while(y_iterator >= 0):
          points = [point for point in data if point[0] >= x and point[0] < x + x_jump and point[1] >= y and point[1] < y+y_jump]
          x_pos = x_segments_count - x_iterator
          y_pos = y_segments_count - y_iterator
          segmented_points[x_pos,y_pos] = Square(np.array(points), x_pos, y_pos)

          y += y_jump
          y_iterator = y_iterator -1
       x += x_jump
       y = min(data[:,1])
       x_iterator = x_iterator - 1
    return(np.array(segmented_points))

data = read_csv('/home/SOMPython/SOM_XYZ/SomXYZ.csv')
data = data.values
squares2d = group_array(data,10,10)
squares = squares2d.flatten()

def normal_vectors_list(squares2d, x_size, y_size):
    print("dobra nara")
            

generate_adn_save_xyz_data('/SOM_XYZ/SomXYZ.csv', 100, 100, 5 * pi / 180)
#generate_and_save_rgb_data('/SOM_RGB/SomDataGrouping.csv', 1500)  # Generate 150 rows