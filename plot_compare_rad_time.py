import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys
import pandas as pd
from find_functions import *



local_folder = '/Volumes/NO NAME/Simulations/'
comp = 'he'

#Read dataframe with the corresponding axis comparison
data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/'+comp+'_comparison.csv')

number_of_plots = data['plot number'].max()+1
number_of_plots = 6
num_columns = 2
rows = number_of_plots // num_columns
if number_of_plots % num_columns != 0:
    rows += 1

position = range(1,number_of_plots+1)

plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['figure.figsize'] = (6,8)



fig = plt.figure()
#Separate dataframes for each simulation into an array called sep_data
for i in range(number_of_plots):
    ax = fig.add_subplot(rows,num_columns,position[i])
    all_paths = []
    #import ipdb; ipdb.set_trace()
    sub_data = data[data['plot number'] == i]
    for path in sub_data['Path']:
        if 'normal' in path:
            split_path = path.split("/")
            mass_folder = split_path[0]
            normal_folder = split_path[-1]
            all_paths.append(local_folder + mass_folder +'/'+ normal_folder)
        else:
            all_paths.append(local_folder + path)
    file_models = gfm.generate_multiple_sim(all_paths)
    all_data = mh.merge_all_data(file_models)
    for folder_name,plot_data in all_data.items():
        print(folder_name)
        label = mh.label_parser(folder_name, data)
        mh.lum_temp_hr(plot_data, label, ax)
    ax.annotate("{}".format(position[i]),xy=(0.962, 0.012), xycoords='axes fraction', fontsize=9, bbox = dict(boxstyle="circle", fc="bisque", ec="orange", lw=0.5, pad=0.2))
    #ax.legend(fontsize=7,loc="lower left", fancybox=True, framealpha=0.5)
    ax.invert_xaxis()

fig.supxlabel("$\log_{10} T_{\\textit{eff}}$ ")
fig.supylabel("$\log_{\ 10}(L/L_\odot)$")
fig.suptitle("HR diagram tracks")
plt.savefig("/Users/nunina/MESA/Simulations/ALL/def/fig/hr_comp_"+comp+".png")
plt.show()
    


