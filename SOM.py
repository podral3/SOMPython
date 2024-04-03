from minisom import MiniSom
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv("D:\PyRepos\SOM data generator\SomDataGrouping.csv")
labels = data['color'].values
data = data.loc[:, ['r', 'g', 'b']].values

train_x, train_y, test_x, test_y = train_test_split(data, labels, test_size=0.20, random_state=42)

# formula for grid dimentions: 5 * sqrt(number of training samples)
#dimentions = 5 * np.sqrt(train_x.shape[0])
#grid_size = np.ceil(np.sqrt(dimentions))

som = MiniSom(3,3,3, sigma=1, learning_rate=0.5)
som.train(train_x, 1000)

for i in test_x.shape[0]:
    som.winner()



