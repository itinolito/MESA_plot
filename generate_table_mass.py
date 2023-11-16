import merge_history as mh
import generate_file_models as gfm
import mesa_reader as mr
import os
import pandas as pd
from collections import defaultdict
from find_functions import *


#---------------------PROGRAM---------------------#
#sim_folders = ['3M1Z/','3M01Z/','2M1Z/','2M01Z/','1.5M1Z/','1.5M01Z/','1M1Z/','1M01Z/','0.8M01Z/']
sim_folders = ['1.5M01Z/']

local_sim = '/Users/nunina/MESA/Simulations/ALL/def/'
columns_list = ['Mass', 'Core mass', 'Age at WD']
format_dict = {'Mass' : '{:.2f}','Core mass' : '{:.2f}','Age at WD' : '{:.3e}'}

for sim_folder in sim_folders:
    name=sim_folder.split('/')[0]
    my_dict=find_mass_and_age(sim_folder)
    df=create_dataframe(my_dict,columns_list)
    normal_age = df.at["normal","Age at WD"]
    df['Diff'] = normal_age - df["Age at WD"]
    df_sorted = df.sort_index()
    df_sorted.head().style.format(format_dict)
    df_sorted.to_csv(local_sim+'tables/{}.csv'.format(name),float_format='%.3e')
