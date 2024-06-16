from minisom import MiniSom
import numpy as np
import pandas as pd
from Data_Structures import DataSet, Square
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use('TkAgg')
from functools import partial


# Inicjalizacja listy do przechowywania wyników
errors = []

# Inicjalizacja wykresu
plt.ion()  
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
ax.set_xlim(0, 10)  
ax.set_ylim(0, 0.5)   
ax.set_title('Quantization Error over Time')
ax.set_xlabel('Iteration')
ax.set_ylabel('Quantization Error')

def update_plot():
    line.set_data(range(len(errors)), errors)
    ax.set_xlim(0, max(10, len(errors)))  
    ax.set_ylim(0, max(errors) if errors else 10)  
    # ax.set_ylim(0, 1)  
    fig.canvas.flush_events()

def naszaFunkcja(obiekt, data):
    error = obiekt.quantization_error(data)
    errors.append(error)
    update_plot()
    
#WASZE

current_dir = os.getcwd()
repo_dir = os.path.dirname(current_dir)
data = pd.read_csv(f'/Users/arturjanowski/Projekty/SOMAGAIN/2/Sample/SomXYZ2.csv')
data = data.values
#moim zdaniem chyba nie potrzeba tutaj normalizować danych, ewentualnie po zmianach wartości x oraz y z jest zawsze -1 do 1

dataSet = DataSet(data)
dataSet.group_points_into_squares(5,5, "squares")
dataSet.randomize(90,[[4,5]])
dataSet.group_normal_vectors(7)
bad_square = dataSet.bad_squares[0]  #0 wskazuje na piereszy element badsquare, mamy teraz tylko jeden
som_3dim = len(dataSet.normals_to_train[0]) #ilość wag w neuronie
som_grid_size = 4

normal_vectors_to_train = dataSet.normals_to_train #tworzenie listy składającej się z wektorów gotowych do treningu 
labels = dataSet.labels



print(len(normal_vectors_to_train))  #9 squerowe wycinki ze wszystkich squerow
label_names={0: 'Dobre', 1: 'Złe'}


print("data", normal_vectors_to_train[0])
print("labels", labels[:2])


som = MiniSom(som_grid_size, som_grid_size, som_3dim, sigma=0.3, learning_rate=0.3,random_seed=42)

funkcja_z_parametrami= partial(naszaFunkcja, som, normal_vectors_to_train)
som.train(normal_vectors_to_train, 1000000, verbose=False,funkcja_po_kazdej_iteracji=funkcja_z_parametrami )