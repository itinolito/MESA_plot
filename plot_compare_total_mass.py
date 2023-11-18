import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys
import pandas as pd
from find_functions import *
from filter_data_phase_space import *


local_folder = '/Volumes/NO NAME/Simulations/'

data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/simulations.csv')

filtered_data = alt_filtered_rows(data, 'Total mass', 0.6, 0.1)

plt.rcParams['figure.figsize'] = (6,6)

fig = plt.figure()
ax = fig.add_subplot(111)

all_paths = []

for path in filtered_data['Path']:
    if 'normal' in path:
        split_path = path.split("/")
        mass_folder = split_path[0]
        normal_folder = split_path[-1]
        all_paths.append(local_folder + mass_folder +'/'+ normal_folder)
    else:
        all_paths.append(local_folder + path)
all_paths.append(local_folder+'0.7M01Z/normal')
file_models = gfm.generate_multiple_sim(all_paths)
all_data = mh.merge_all_data(file_models)
for folder_name,plot_data in all_data.items():
    print(folder_name)
    label = mh.label_parser(folder_name, data)
    mh.lum_temp_hr(plot_data, label, ax)

ax.legend(fontsize=7,loc="lower left")
ax.invert_xaxis()

fig.supxlabel("$\log_{10} T_{\\textit{eff}}$ ")
fig.supylabel("$\log_{\ 10}(L/L_\odot)$")
fig.suptitle("HR diagram track for 0.7$M_\odot$ stars")

plt.show()
    


