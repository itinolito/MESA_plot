import merge_history as mh
import generate_file_models as gfm
import mesa_reader as mr
import os
import pandas as pd
from collections import defaultdict


#--------------------FUNCTIONS--------------------#

def has_rg_radius(logR):
    return logR > 1.3

def has_large_lum(logL):
    return logL > 1

#---------FIND MODEL AND DATA FROM MODEL----------#

def find_models_function(function,parameter,file_models):
    my_models = file_models.copy()
    for name, simulations in my_models.items():
        for file_model in simulations:
#            mesa_param_obj = mr.MesaLogDir(file_model['folder_path'])
#            file_model['models'] = mesa_param_obj.select_models(function, parameter).tolist()
            mesa_param_obj = mr.MesaData(file_model['folder_path']+'/history.data')
            file_model['models'] = mesa_param_obj.where(function, parameter).tolist()
    return my_models

def find_data_model(function,parameter,file_models,my_data):
    my_models = find_models_function(function,parameter,file_models)

    my_models_data = {}
    for name,stages in my_models.items():
        stage_data = mh.aggregate_data(stages)
        my_models_data[name] = stage_data

    found_info = {}
    for star_name, stages in my_models_data.items():
        found_info[star_name] = {}
        for folder_name,data in stages.items():
            found_info[star_name] = data[my_data]
    return found_info


#---------FIND DATA ENTRIES FROM HISTORY-------#

def find_data_history(file_models,my_data):
    all_data = mh.merge_all_data(file_models)

    data_to_know = {}
    for sim_name,sim_data in all_data.items():
        data_to_know[sim_name] = sim_data[my_data]
    return data_to_know

def get_paths(sim_folder):
    global_path = local_sim+sim_folder
    all_paths = []
    for path in os.listdir(global_path):
        if path != '.DS_Store':
            all_paths.append(global_path+path)
        else:
            continue
    return all_paths

def find_wd_age(sim_folder):
    all_paths = get_paths(sim_folder)
    file_models = gfm.generate_multiple_sim(all_paths)
    ages=find_data_history(file_models,'age')
    ages_wd = {}
    for name,age in ages.items():
        ages_wd[name] = age[-1]
    return ages_wd

def find_star_mass(sim_folder):
    all_paths = get_paths(sim_folder)
    file_models = gfm.generate_multiple_sim(all_paths)
    masses=find_data_history(file_models,'mass')
    mass_start = {}
    for name,mass in masses.items():
        mass_start[name] = mass[0]
    return mass_start

def find_mass_and_age(sim_folder):
    mass = find_star_mass(sim_folder)
    age = find_wd_age(sim_folder)
    my_data = defaultdict(list)
    for data in (mass, age):
        for key,value in data.items():
            my_data[key].append(value)
    return my_data

#--------------------DATAFRAME--------------------#
def create_dataframe(dictionary,columns_list):
    return pd.DataFrame.from_dict(dictionary,orient='index',columns=columns_list)

#---------------------PROGRAM---------------------#
sim_folders = ['3M1Z/','3M01Z/','2M1Z/','2M01Z/','1.5M1Z/','1.5M01Z/','1M1Z/','1M01Z/','0.8M01Z/']
local_sim = '/Users/nunina/MESA/Simulations/MS/'
columns_list = ['Mass', 'Age at WD']
format_dict = {'Mass' : '{:.2f}','Age at WD' : '{:.3e}'}

for sim_folder in sim_folders:
    name=sim_folder.split('/')[0]
    my_dict=find_mass_and_age(sim_folder)
    df=create_dataframe(my_dict,columns_list)
    normal_age = df.at["normal","Age at WD"]
    df['Diff'] = normal_age - df["Age at WD"]
    df_sorted = df.sort_index()
    df_sorted.head().style.format(format_dict)
    df_sorted.to_csv(local_sim+'tables/{}.csv'.format(name),float_format='%.3e')


#print(find_models_function(has_rg_radius,'log_R',file_models))
#print(find_data_model(has_rg_radius,'log_R',file_models,'age'))

#mesa_param_obj = mr.MesaData(local_sim+sim_folder+'/history.data')
#data = mesa_param_obj.data('log_R')
#for i in data:
#    import ipdb; ipdb.set_trace()
#    if data[i] > 1.0:
#        print(data[i])

