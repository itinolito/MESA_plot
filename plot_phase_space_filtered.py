from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import pandas as pd
from plot_phase_space import *
from filter_data_phase_space import *


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/simulations.csv')

comparisons = {
    'prog_comparison' : [X_AXIS, Y_AXIS, X_RANGE, Y_RANGE, 0.05],
    'he_comparison' : [Y_AXIS, Z_AXIS, Y_RANGE, Z_RANGE, 0.098],
    'total_mass_comparison' : [X_AXIS, Z_AXIS, X_RANGE, Z_RANGE, 0.095]
}

#comp = 'total_mass'
#comp = 'prog'
comp = 'he'



#Create csv data
ax_comparison(data, comparisons, comp)

filtered_data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/'+comp+'_comparison.csv')

plot_xyz_data(ax, data)
for i in range(filtered_data['plot number'].max()+1):
    plot_lines(ax, filtered_data[filtered_data['plot number'] == i])

plt.show()