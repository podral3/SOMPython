import os
from pandas import read_csv
from DataSet import *

def prepare_data(data, x_div_range = 10, y_div_range = 10, plane_method = "svd",
                 search_window_size = 3, randomize_percent = 50,
                 squares_to_randomize = [[4,5]]):
    """
    Returns:
        Processed dataset, Training values, labels for training dataset, 3rd SOM dimetion
    """
    current_dir = os.getcwd()
    repo_dir = os.path.dirname(current_dir)
    data = read_csv(f'{repo_dir}/Sample Data/SomXYZ.csv')
    data = data.values
    #moim zdaniem chyba nie potrzeba tutaj normalizować danych, ewentualnie po zmianach wartości x oraz y z jest zawsze -1 do 1

    dataSet = DataSet(data)
    dataSet.group_points_into_squares(x_div_range, y_div_range, plane_method)
    dataSet.randomize(randomize_percent,squares_to_randomize)
    dataSet.group_normal_vectors(search_window_size)
    som_3dim = len(dataSet.normals_to_train[0]) #ilość wag w neuronie

    normal_vectors_to_train = dataSet.normals_to_train #tworzenie listy składającej się z wektorów gotowych do treningu 
    labels = dataSet.labels

    return dataSet, normal_vectors_to_train, labels, som_3dim