import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pandas as pd

data = pd.read_csv('SomXYZ.csv', skiprows=0) #pd dataframe
data = data.values #np array
x = data[:,0]
y = data[:,1]
z = data[:,2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x, y, z, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(x, y, z, c='red')
plt.show()