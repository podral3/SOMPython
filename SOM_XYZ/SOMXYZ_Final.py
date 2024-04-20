from minisom import MiniSom
import numpy as np
import pandas as pd
from Square import Square, colors

data = pd.read_csv('/home/repos/SOMPython/SOM_XYZ/SomXYZ.csv')
data = data.values
#moim zdaniem chyba nie potrzeba tutaj normalizować danych,
#ewentualnie po zmianach wartości x oraz y z jest zawsze -1 do 1

x_values = data[:,0]
y_values = data[:,1]
z_values = data[:,2]
min_x = min(x_values)
min_y = min(y_values)
max_x = max(x_values)
max_y = max(y_values)

def group_array(data, x_jump, y_jump): #przenieść do pliku ale nie klasy square?
    x_segments_count = int((max(x_values) - min(x_values)) / x_jump)
    y_segments_count = int((max(y_values) - min(y_values)) / y_jump)
    segmented_points = []

    x = min_x
    y = min_y

    x_iterator = x_segments_count
    while(x_iterator >= 0):
       y_iterator = y_segments_count
       while(y_iterator >= 0):
          points = [point for point in data if point[0] >= x and point[0] < x + x_jump and point[1] >= y and point[1] < y+y_jump]
          x_pos = x_segments_count - x_iterator
          y_pos = y_segments_count - y_iterator
          segmented_points.append(Square(np.array(points), x_pos, y_pos))

          y += y_jump
          y_iterator = y_iterator -1
       x += x_jump
       y = min_y
       x_iterator = x_iterator - 1
    return(np.array(segmented_points))
    
squares = group_array(data,10,10)

#zrobić to bardziej ustandaryzowanie
squares[0].randomize_points(10) 
bad_square = squares[0]

som_3dim = squares[0].points_to_train.shape[0] #ilość wag w neuronie
points_to_train = np.array([x.points_to_train for x in squares]) #tworzenie listy składającej się z wektorów gotowych do treningu
som_x, som_y = 2,2
som = MiniSom(som_x, som_y, som_3dim, random_seed=42)
som.train(points_to_train, 100000) 

#tworzenie mapy kolorów 
#mądrze umieścić gdzieś w funkcji
som_colors = np.empty((som_x, som_y), dtype='object')
color_idx = 0
for i in range(som_x):
    for j in range (som_y):
        som_colors[i,j] = colors[color_idx]
        color_idx+= 1

#kolorowanie punktów sinusoidy
#mądrze umieścić w funkcji
for square in squares:
    winner_pos = som.winner(bad_square.points_to_train)
    col = som_colors[winner_pos[0], winner_pos[1]]
    square.color_my_points(col)

#zapisywanie pokolorowanych pkt do pliku csv
import csv
def print_out_squares(squares): #zmien nazwe
    formatted_numbers = []
    with open('numbers.csv', 'w', newline='') as csvfile:
        for suqare in squares:
            points_to_print = suqare.colored_points
            writer = csv.writer(csvfile)
            for point in points_to_print:
                for num in point:
                    formatted_numbers.append("{}".format(num))
                writer.writerow(formatted_numbers)
                formatted_numbers = []
print_out_squares(squares)