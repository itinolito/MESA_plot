import merge_history as mh
import generate_file_models as gfm
import mesa_reader as mr
import os
import pandas as pd
from collections import defaultdict

local_sim = '/Volumes/NO NAME/Simulations/'


#--------------------FUNCTIONS--------------------#

def has_rg_radius(logR):
    return logR > 1.3

def has_large_lum(logL):
    return logL > 1

def particular_age(star_age):
    return star_age > 22755509468.945694

def he_content(he):
    return he > 0.5

#---------FIND MODEL AND DATA FROM MODEL----------#

def find_models_function(function,parameter,sim_folder):
    all_paths = get_paths(sim_folder)
    my_models = gfm.generate_multiple_sim(all_paths)
    for name, simulations in my_models.items():
        for file_model in simulations:
            mesa_param_obj = mr.MesaLogDir(file_model['folder_path'])
            file_model['models'] = mesa_param_obj.select_models(function, parameter).tolist()
    return my_models


#---------FIND DATA ENTRIES FROM HISTORY-------#

def find_data_history(file_models,my_data):
    all_data = mh.merge_all_data(file_models)
    data_to_know = {}
    for sim_name,sim_data in all_data.items():
        print(sim_name)
        data_to_know[sim_name] = sim_data[my_data]
    return data_to_know

def get_paths(sim_folder):
    global_path = local_sim+sim_folder+'/'
    all_paths = []
    for path in os.listdir(global_path):
        if path != '.DS_Store' and path != 'LOGS_stop_at_RG' and path.endswith('.mod')==False:
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

def find_he_data(file_models):
    all_data = mh.merge_all_data(file_models)
    for sim_name,sim_data in all_data.items():
        data_to_know[sim_name] = sim_data[my_data]
    return data_to_know

def find_middle_age(sim_folder,previous_stage,stage):
    ages_wd = find_wd_age(sim_folder)
    stage_lifetime = ages_wd[stage]-ages_wd[previous_stage]
    mid_stage_age = stage_lifetime/2
    return float(ages_wd[previous_stage]+mid_stage_age)

def find_star_mass(sim_folder):
    all_paths = get_paths(sim_folder)
    file_models = gfm.generate_multiple_sim(all_paths)
    masses=find_data_history(file_models,'mass')
    mass_start = {}
    for name,mass in masses.items():
        mass_start[name] = mass[0]
    return mass_start

def find_core_mass(sim_folder):
    all_paths = get_paths(sim_folder)
    file_models = gfm.generate_multiple_sim(all_paths)
    masses=find_data_history(file_models,'he_core_mass')
    mass_core = {}
    for name,mass in masses.items():
        mass_core[name] = mass[0]
    return mass_core


def find_mass_and_age(sim_folder):
    mass = find_star_mass(sim_folder)
    core_mass = find_core_mass(sim_folder)
    age = find_wd_age(sim_folder)
    my_data = defaultdict(list)
    for data in (mass, core_mass, age):
        for key,value in data.items():
            my_data[key].append(value)
    return my_data

def find_he_age(sim_folder):
    all_paths = get_paths(sim_folder)
    file_models = gfm.generate_multiple_sim(all_paths)
    age=find_data_history(file_models,'age')
    he=find_data_history(file_models,'he_core_mass')
    my_data = defaultdict(list)
    for data in (he, age):
        for key,value in data.items():
            my_data[key].append(value)
    return my_data

def total_and_core_mass(masses,core_masses):
    mass_data = {
        name : [] for name in masses.keys()
    }
    for name,mass in masses.items():
        mass_data[name].append(mass[0])
    for name,core_mass in core_masses.items():
        mass_data[name].append(core_mass[0])
    return mass_data

#--------------------DATAFRAME--------------------#
def create_dataframe(dictionary,columns_list):
    dataframe = pd.DataFrame([[key] + val for key, val in dictionary.items()], columns=columns_list)
    return dataframe

