from minisom import MiniSom
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.read_csv('.\SomXYZ.csv')
data = data.values
#moim zdaniem chyba nie potrzeba tutaj normalizować danych, ewentualnie po zmianach wartości x oraz y z jest zawsze -1 do 1
print(data.shape)

x_values = data[:,0]
y_values = data[:,1]
z_values = data[:,2]

#nasz group_array nie ma sensu gdyz dzieli on listę np od recordu 0 do 50, a my poruszamy się w 3d więc musi dzielić np x: 0-5, y: 0-5
#mam na to napisaną metodę w c#
def get_step(data):
  uniq = np.unique(data)
  return abs(uniq[-2] - uniq[-1])
def group_array(data, x_segmentation_range, y_segmentation_range):
    x_segments_count = int((max(data[:,0]) - min(data[:,0])) / get_step(data[:,0])) + 1 #chyba plus jeden, zakres jest od 0 do 99 a pokazuje 99 segmentów
    y_segments_count = int((max(data[:,1]) - min(data[:,1])) / get_step(data[:,1])) + 1
    segmented_points = []
    for x in range(x_segments_count):
       for y in range(y_segments_count):
          points = [point for point in data if point[0] >= x and point[0] < x + x_segmentation_range and point[1] >= y and point[1] < y+y_segmentation_range]
       segmented_points.extend(points)
    return(segmented_points)
    
niggers = group_array(data,10,10)
print(niggers[0])