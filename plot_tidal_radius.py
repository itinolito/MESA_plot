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
bh_masses = [1e3,1e4,1e5,1e6]

def row_maker(num):
   if num > 1:
      row = 1
   else:
      row = 0
   return row

line_xs = np.linspace(-0.9,1.1,50)
line_value = 4
line_ys = []
for i in line_xs:
   line_ys.append(line_value)

mass_file_models = {name : [] for name in mass_folders}
#Iterate over each mass folder
for mass_folder in mass_folders:
    sim_folder = local_sim+mass_folder+'/'
    #Find helium subfolders
    he_folders = [path for path in os.listdir(sim_folder) if path != 'normal']
    #Iterate over helium folders to find stop folders if they exist
    for he_folder in he_folders:
        stop_folder = [ sim_folder+he_folder+'/'+stop for stop in os.listdir(sim_folder+he_folder) if stop == 'LOGS_stop_at_RG']
        model_list = []
        if stop_folder:
            #read profiles and take last model
            profiles_info = pd.read_csv(stop_folder[0]+'/profiles.index', delim_whitespace=True, skiprows=1, names=['model', 'priority', 'profile_number'])
            last_model = profiles_info['model'].iloc[-1]
            model_list.append(last_model)
            #add to the file_models the desired model
            mass_file_models[mass_folder].append({'folder_path' : stop_folder[0],
                               'name': mass_folder+he_folder,
                               'models': model_list})
            

fig, axs = plt.subplots(2,2, constrained_layout=True)

i=0
for mass_folder, list_subfolders in mass_file_models.items():
   column = i % 2
   row = row_maker(i)
   
   axs[row,column].plot(line_xs,line_ys, c="red", ls="dotted", lw = 0.8)
   axs[row,column].fill_between(line_xs, line_ys, 0, color='red', alpha=.1)
   for bh_mass in bh_masses:
      for each in list_subfolders:
         folder = each['folder_path']
         models = each['models']
         name = each['name']
         if '050he' in name:
            for model in models:
               p = mh.get_file(folder,model)
               data = mh.get_params(p)
               mh.tidal_radius_mass_fraction(data,axs[row,column],bh_mass,'{:.0e} $M_{}$'.format(bh_mass,'{BH}'))
               axs[row,column].annotate(name, xy=(0.05, 0.1),xycoords='axes fraction', fontsize=12, horizontalalignment='left', verticalalignment='bottom')
         else:
            continue
   i+=1

plt.grid(False)
fig.supxlabel("$f_s=1-\\frac{M(r)}{M_\star}$")
fig.supylabel("$\\frac{R_t}{r_g} =  \left(\\frac {M_{BH}}{M(r)}\\right)^{1/3} r \\frac{c^2}{G M_{BH}}$")
fig.suptitle("Tidal radius as a function of the fraction stripped")

fig, axs = plt.subplots(2,2, constrained_layout=True)

for i in range(4):
   bh_mass = bh_masses[i]
   column = i % 2
   row = row_maker(i)

   axs[row,column].plot(line_xs,line_ys, c="red", ls="dotted", lw = 0.8)
   axs[row,column].fill_between(line_xs, line_ys, 0, color='red', alpha=.1)

   for mass_folder, list_subfolders in mass_file_models.items():
      for each in list_subfolders:
         folder = each['folder_path']
         models = each['models']
         name = each['name']
         if '050he' in name:
            for model in models:
               p = mh.get_file(folder,model)
               data = mh.get_params(p)
               mh.tidal_radius_mass_fraction(data,axs[row,column],bh_mass,name)
               axs[row,column].annotate('{:.0e} $M_{}$'.format(bh_mass, '{BH}'), xy=(0.05, 0.15),xycoords='axes fraction', fontsize=12, horizontalalignment='left', verticalalignment='bottom')
         else:
            continue

fig.supxlabel("$f_s=1-\\frac{M(r)}{M_\star}$")
fig.supylabel("$\\frac{R_t}{r_g} =  \left(\\frac {M_{BH}}{M(r)}\\right)^{1/3} r \\frac{c^2}{G M_{BH}}$")
fig.suptitle("Tidal radius as a function of the fraction stripped")

plt.show()

