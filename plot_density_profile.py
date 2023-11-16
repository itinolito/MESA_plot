import matplotlib.pyplot as plt
import matplotlib as mpl
import merge_history as mh
import generate_file_models as gfm
import pandas as pd
from find_functions import *
import sys
import numpy as np


local_sim = '/Volumes/NO NAME/Simulations/'
mass_folders = ['1M01Z', '1.5M01Z', '2M01Z', '3M01Z']
labeldata = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/simulations.csv')

plt.rcParams['figure.figsize'] = (6,5)


def row_maker(num):
   if num > 1:
      row = 1
   else:
      row = 0
   return row


dict_of_file_models = { mass_name : {} for mass_name in mass_folders }

#Iterate over each mass folder
for mass_folder in mass_folders:
   mass_file_models = {}

   sim_folder = local_sim+mass_folder+'/'
   #Find helium subfolders
   he_folders = [path for path in os.listdir(sim_folder) if path != 'normal']
   #Iterate over helium folders to find stop folders if they exist
   for he_folder in he_folders:
      stop_folder = [sim_folder+he_folder+'/'+stop for stop in os.listdir(sim_folder+he_folder) if stop == 'LOGS_stop_at_RG']
      strip_folders = [sim_folder+he_folder+'/'+strip for strip in os.listdir(sim_folder+he_folder) if strip != 'LOGS_stop_at_RG' and '.mod' not in strip]
      model_list = []
      if stop_folder:
         #read profiles and take last model
         profiles_info = pd.read_csv(stop_folder[0]+'/profiles.index', delim_whitespace=True, skiprows=1, names=['model', 'priority', 'profile_number'])
         last_model = profiles_info['model'].iloc[-1]
         model_list.append(last_model)
         #add to the file_models the desired model
         mass_file_models['Before stripping'] = [{'folder_path' : stop_folder[0],
                            'name': 'Simulations/'+mass_folder+'/normal',
                            'models': model_list}]
         
      mass_file_models['After stripping'] = []

      for strip_folder in strip_folders:
         strip = strip_folder.split("/")[-1]
         #parse the subfolder
         subfolder = "/s"+"".join([*strip][5:8])+"_TPAGB"
         model_list = []
         #read profiles and take first model
         profiles_info = pd.read_csv(strip_folder+subfolder+'/profiles.index', delim_whitespace=True, skiprows=1, names=['model', 'priority', 'profile_number'])
         first_model = profiles_info['model'].iloc[0]
         model_list.append(first_model)
         #add to the file_models the desired model
         mass_file_models['After stripping'].append({'folder_path' : strip_folder+subfolder,
                            'name': mass_folder+'/'+he_folder+'/'+strip,
                            'models': model_list})
         
      #mh.plot_profile_mass(mass_file_models,labeldata)
      
   dict_of_file_models[mass_folder] = mass_file_models
           
for name_mass_star, mass_file_models in dict_of_file_models.items():
   mh.plot_profile_mass(mass_file_models,labeldata)
   

plt.show()
