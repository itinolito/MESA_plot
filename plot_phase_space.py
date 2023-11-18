from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import pandas as pd

X_AXIS = '%He at stripping'
Y_AXIS = 'Progenitor mass'
Z_AXIS = 'Total mass'

X_RANGE = [0.1, 0.25, 0.50, 0.75]
Y_RANGE = [1,1.5,2,3]
Z_RANGE = [0.7, 1,1.2, 1.5,1.8,2]

def plot_xyz_data(ax, data):

    strip_data = data[~data["Path"].str.contains("normal")]
    xdata = strip_data['%He at stripping']
    ydata = strip_data['Progenitor mass']
    zdata = strip_data['Total mass']

    ax.set_xlabel('He fraction at stripping')
    ax.set_ylabel('Progenitor mass')
    ax.set_zlabel('Total mass')

    scatter_plot = ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='viridis')

    normal_data = data[data["Path"].str.contains("normal")]
    normal_xdata = normal_data['%He at stripping']
    normal_ydata = normal_data['Progenitor mass']
    normal_zdata = normal_data['Total mass']
    scatter_plot = ax.scatter3D(normal_xdata, normal_ydata, normal_zdata, c='red')

def plot_lines(ax, data):
    ax.plot(data[X_AXIS],data[Y_AXIS],data[Z_AXIS], c='black', lw=0.5)

