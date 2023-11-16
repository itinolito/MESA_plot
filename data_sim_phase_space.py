import merge_history as mh
import generate_file_models as gfm
import mesa_reader as mr
import os
import pandas as pd
from collections import defaultdict
from find_functions import *


#---------------------PROGRAM---------------------#

local_sim = '/Volumes/NO NAME/Simulations/'
mass_folders = ['1M01Z', '1.5M01Z', '2M01Z', '3M01Z']

data_to_plot = {}
normal_data = {}
#Iterate over each mass folder
for mass_folder in mass_folders:
    #Find helium subfolders
    he_folders = [path for path in os.listdir(local_sim+mass_folder+'/') if path != 'normal']
    #Iterate over helium folders
    for he_folder in he_folders:
        sim_folder = mass_folder+'/'+he_folder
        stop_folder = [ local_sim+sim_folder+'/'+stop for stop in os.listdir(local_sim+sim_folder) if stop == 'LOGS_stop_at_RG']
        #Get the list of all paths inside he folders (strip cases)
        all_paths = get_paths(sim_folder)
        #Get a dictionary organized by simulation with all the paths
        file_models = gfm.generate_multiple_sim(all_paths)
        
        #Find data from each simulation
        #import ipdb; ipdb.set_trace()
        masses=find_data_history(file_models,'mass')
        core_masses=find_data_history(file_models,'he_core_mass')

        #Generate dictionary with key simulation and mass, core for the start of each one
        inner_data = total_and_core_mass(masses,core_masses)
        folder = sim_folder.split("/")[-2]
        sub_folder = sim_folder.split("/")[-1]
        split_subfolder = [*sub_folder]
        he1 = ".".join(split_subfolder[0:2])
        progenitor_mass = folder.split('M')[0]
        he = he1+split_subfolder[2]


        all_sim_data = {name : [] for name in file_models.keys() if name != "LOGS_stop_at_RG"}
        for name in all_sim_data:
            all_sim_data[name].append(inner_data[name][0])
            all_sim_data[name].append(inner_data[name][1])
            all_sim_data[name].append(float(progenitor_mass))
            all_sim_data[name].append(float(he))
        data_to_plot[sim_folder] = all_sim_data
        if stop_folder:
            #normal simulation
            normal_fm = gfm.generate_file_models(stop_folder[0])
            normal_mass = find_data_history(normal_fm,'mass')['LOGS_stop_at_RG'][-1]
            normal_core_mass = find_data_history(normal_fm,'he_core_mass')['LOGS_stop_at_RG'][-1]
            normal_data[mass_folder+'/'+he_folder] = [normal_mass,normal_core_mass,float(progenitor_mass),float(he)]

data_for_dataframe = {}
for name, another_dict in data_to_plot.items():
    for strip, data in another_dict.items():
        if strip != 'normal':
            #folder_mass = name.split("/")[0]
            data_for_dataframe[strip] = data

for name, data in normal_data.items():
    data_for_dataframe[name+'/normal'] = data

columns_list = ['Path', 'Total mass', 'Core mass', 'Progenitor mass', '%He at stripping']

df=create_dataframe(data_for_dataframe, columns_list)
#normal_df = create_dataframe(normal_data,columns_list)

df_sorted = df.sort_values('Progenitor mass')
df_sorted.to_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/simulations.csv',float_format='%.3e')
#normal_df.to_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/simulations_normal.csv',float_format='%.3e')

