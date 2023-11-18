from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import pandas as pd
import merge_history as mh

comp = 'he'

color_names = ["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth"]

data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/'+comp+'_comparison.csv')

data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/simulations.csv')


labels = data['Path'].apply(lambda x: mh.label_parser(x, data))

#reordered_columns = [
#    "Path",
#    "Total mass",
#    "Core mass",
#    "plot number",
#    "Progenitor mass",
#    "%He at stripping",
#]

#reordered_data = data[reordered_columns]

#all_colors = []
#number_of_plots = data["plot number"].max() + 1
#
#for i in range(number_of_plots):
#    subset_data = data[data['plot number'] == i]
#    data_size = data[data['plot number'] == i].shape[0]
#
#    for index in range(data_size):
#        color = color_names[index % 9]
#        all_colors.append(color)
#
#
#tikz_list = []
#for i in all_colors:
#    tikz_string = "\\begin{{tikzpicture}}\\draw [line width=3, {color} ] (0,0) -- (1,0) node[right]{{}};\\end{{tikzpicture}}".format(color=i)
#    tikz_list.append(tikz_string)

beautiful_data = pd.DataFrame()
#beautiful_data['Plot \\#'] = data['plot number']+1
#beautiful_data['Color'] = tikz_list
beautiful_data['Label'] = labels
beautiful_data['Total mass'] = data['Total mass']
beautiful_data['Core mass'] = data['Core mass']
beautiful_data['Prog mass'] = data['Progenitor mass']
beautiful_data['He'] = data['%He at stripping']

sorted = beautiful_data.sort_values(by=['Prog mass', 'He', 'Total mass'], ascending=[True, True, False])
sorted.to_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/sim_table.csv', mode='w', sep="&", index=False, line_terminator="\\\\", float_format="%.3f")

#beautiful_data.to_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/'+comp+'_legend.csv', mode='w', sep="&", index=False, line_terminator="\\\\", float_format="%.3f")

