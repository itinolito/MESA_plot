import matplotlib.pyplot as plt
import matplotlib as mpl
import merge_history as mh
import generate_file_models as gfm
import pandas as pd
from find_functions import *
import sys
import numpy as np


local_sim = '/Volumes/NO NAME/Simulations/'
mass_folders = ['0.7M01Z', '1M01Z', '1.5M01Z', '2M01Z', '3M01Z']

plt.rcParams['figure.figsize'] = (5,5)

fig = plt.figure()
fig.suptitle('HR diagram tracks')
ax1 = fig.add_subplot(1,1,1)

i=1
#Iterate over each mass folder
for mass_folder in mass_folders:

   sim_folder = local_sim+mass_folder+'/'
   normal_path = [sim_folder + 'normal']
   
   #Find helium subfolders
   he_folders = [path for path in os.listdir(sim_folder) if path != 'normal']
   stop_folders = []
   if he_folders:
      #Iterate over helium folders to find stop folders if they exist
      for he_folder in he_folders:
         stop_folder = [ sim_folder+he_folder+'/'+stop for stop in os.listdir(sim_folder+he_folder) if stop == 'LOGS_stop_at_RG']
         stop_folders.append(stop_folder[0])

   #normal file models
   normal_models = gfm.generate_multiple_sim(normal_path)

   #different stages
   normal_by_stages = gfm.generate_file_models(normal_path[0])

   all_temp_by_stage = find_data_history(normal_by_stages,'log_Teff')
   all_lum_by_stage = find_data_history(normal_by_stages,'log_luminosity')


   zams_temp = all_temp_by_stage['MS'][0]
   zams_lum = all_lum_by_stage['MS'][0]


   #if he_folders:
   #   #stop file models
   #   stop_models = gfm.generate_multiple_sim(stop_folders)
#
   #   #find data
   #   all_teff = find_data_history(stop_models,'log_Teff')
   #   all_lum = find_data_history(stop_models,'log_luminosity')
#
   #   relevant_teff = []
   #   relevant_lum = []
   #   for name_sim, info in all_teff.items():
   #      strip_age = info[-1]
   #      relevant_teff.append(strip_age)
#
   #   for name_sim, info in all_lum.items():
   #      strip_lum = info[-1]
   #      relevant_lum.append(strip_lum)

   
   all_data = mh.merge_all_data(normal_models)
   for folder_name,data in all_data.items():
      mh.lum_temp_hr(data,folder_name.split("/")[1],ax1)
   
   #if he_folders:
   #   ax1.scatter(relevant_teff,relevant_lum, c="red", zorder=1)
   #   for k,j in enumerate(he_folders):
   #      ax1.annotate('{}'.format(j),xy=(relevant_teff[k],relevant_lum[k]),fontsize=8,xytext=(-20-k*25,-27),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=0.5))

   ax1.scatter(zams_temp,zams_lum,c="red", zorder=1)   

   i+=1
   
leg = fig.legend(fontsize="x-small", ncol = 1, loc = "lower left", bbox_to_anchor=(.14,.13))

for legobj in leg.legendHandles:
    legobj.set_linewidth(2.0)

fig.supylabel("$\log_{\ 10}(L/L_\odot)$")
fig.supxlabel("$\log_{10} T_{\\textit{eff}}$")

plt.show()

