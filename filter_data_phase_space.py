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

data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/simulations.csv')


def filtered_rows(data, axis_row, axis_filtered, row_data, filter_range, eps):
    rows = data[data[axis_row]==row_data]

    data_filtered = rows[rows[axis_filtered].between(filter_range-eps,filter_range+eps)]
    return data_filtered


def ax_comparison(data, comparison_dictionary, name):
    
    axis_row = comparison_dictionary[name+'_comparison'][0]
    axis_filtered = comparison_dictionary[name+'_comparison'][1]
    axis_row_range = comparison_dictionary[name+'_comparison'][2]
    axis_filtered_range = comparison_dictionary[name+'_comparison'][3]
    eps = comparison_dictionary[name+'_comparison'][4]

    counter = 0
    all_filtered_data = pd.DataFrame()
    for ax1 in axis_row_range:
        for ax2 in axis_filtered_range:
            filtered_data = filtered_rows(data, axis_row, axis_filtered, ax1, ax2, eps)
            if filtered_data.shape[0] < 2:
                continue

            filtered_data["plot number"] = counter
            all_filtered_data = pd.concat([all_filtered_data, filtered_data])
            if not filtered_data.empty:
                counter += 1
    
    all_filtered_data.to_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/'+name+'_comparison.csv', mode='w')


