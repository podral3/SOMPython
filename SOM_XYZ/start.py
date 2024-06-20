import numpy as np
import pandas as pd
from Our_MiniSom import *
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use('TkAgg')
from functools import partial
import time


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

def update_plot(iteration, division):
    x_cords = [x * division for x in range(len(errors))]
    line.set_data(x_cords, errors)
    ax.set_xlim(0, iteration)  
    ax.set_ylim(0, max(errors) if errors else 10)   
    # ax.set_ylim(0, 1)  
    fig.canvas.flush_events()

def naszaFunkcja(obiekt, data, iteration, division):
    error = obiekt.quantization_error(data) #wywoływanie tej funkcji podczas treningu potrafi wywalić czasami jakieś NaNy
    errors.append(error)
    update_plot(iteration, division)
    

#Wczytanie danych    
current_dir = os.getcwd()
repo_dir = os.path.dirname(current_dir)
data = pd.read_csv(f'{current_dir}/Sample Data/SomXYZ.csv')
data = data.values

#Przygotowanie danych do treningu
dataSet, normal_vectors_to_train, labels, som_3dim = DataSet.prepare_data(data)
bad_square = dataSet.bad_squares[0]
som_grid_size = 3
label_names = {0: 'Dobre', 1: 'Złe'}

print(len(normal_vectors_to_train))  #9 squerowe wycinki ze wszystkich squerow
label_names={0: 'Dobre', 1: 'Złe'}


# print("data", normal_vectors_to_train[0])
# print("labels", labels[:2])


som = MiniSom(som_grid_size, som_grid_size, som_3dim, sigma=0.3, learning_rate=0.3,random_seed=42)

funkcja_z_parametrami= partial(naszaFunkcja, som, normal_vectors_to_train)
som.train(normal_vectors_to_train, 10000, verbose=False,nasza_funkcja=funkcja_z_parametrami, co_ile_iteracji_nasza= 10)
print("koniec")