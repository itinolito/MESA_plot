import merge_history as mh
import generate_file_models as gfm
import mesa_reader as mr
import os
import pandas as pd
from collections import defaultdict
from find_functions import *
import generate_file_models as gfm
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#---------------------PROGRAM---------------------#
local_sim = '/Users/nunina/MESA/Simulations/ALL/def/'
sim_folder = '0.7M01Z/normal/'

columns_list = ['He', 'Age']
format_dict = {'He' : '{:.2f}', 'Age' : '{:.3e}'}

#for sim_folder in sim_folders:
#    name=sim_folder.split('/')[0]
#    my_dict=find_he_age(sim_folder)
#    print(my_dict)
    #df=create_dataframe(my_dict,columns_list)
    #df_sorted = df.sort_index()
    #df_sorted.head().style.format(format_dict)
    #df_sorted.to_csv(local_sim+'tables/{}.csv'.format(name),float_format='%.3e')

#file_models = gfm.generate_file_models(local_sim+sim_folder)
#results = find_models_function(is_middle_rg,'star_age',file_models)
#print(results)

if mh.history == True:
    # This finds the age of the star at half the RG lifetime
    mid_rg = find_middle_age(sim_folder,'MS','RG')

    # This finds the first model of the star that has that age
    results = find_models_function(particular_age,'star_age',sim_folder)
    for stage, sim in results.items():
        if sim[0]['models'] == []:
            continue
        else:
            model=sim[0]['models'][0]
            break

# Now we want to know the core mass of that model

file_models = {'07m01c01z00s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/0.7M01Z/normal/RG', 
                 'name': '07m_rg', 'models': [400,2300,6693]}],
               '07m05c01z02s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/1M01Z/050he/strip02/s02_TPAGB', 
                  'name': 's02_tpagb', 'models': [8400]},
                ],}

fig = plt.figure(constrained_layout = True)
fig.suptitle('Profiles')
spec = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
ax1 = fig.add_subplot(spec[0, :])
ax2 = fig.add_subplot(spec[1, :])


for name, simulations in file_models.items():
    simulations_data = mh.aggregate_data(simulations)

    for folder_name, models_data in simulations_data.items():
        for model,data in models_data.items():
            mh.density_mass(data,model,name,ax1)
            mh.radius_mass(data,model,name,ax2)

plt.show()
