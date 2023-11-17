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

plt.rcParams['figure.figsize'] = (5,6)

fig = plt.figure()
fig.suptitle('Radius with time')


i=1
#Iterate over each mass folder
for mass_folder in mass_folders:
   
   ax1 = fig.add_subplot(4,1,i)

   sim_folder = local_sim+mass_folder+'/'
   normal_path = sim_folder + 'normal'
   
   #Find helium subfolders
   he_folders = [path for path in os.listdir(sim_folder) if path != 'normal']
   stop_folders = []

   #Iterate over helium folders to find stop folders if they exist
   for he_folder in he_folders:
      stop_folder = [ sim_folder+he_folder+'/'+stop for stop in os.listdir(sim_folder+he_folder) if stop == 'LOGS_stop_at_RG']
      stop_folders.append(stop_folder[0])

   #normal file models
   normal_models = gfm.generate_file_models(normal_path)

   #stop file models
   stop_models = gfm.generate_multiple_sim(stop_folders)

   #find data
   all_ages = find_data_history(stop_models,'age')
   all_radius = find_data_history(stop_models,'radius')

   relevant_ages = []
   relevant_radius = []
   for name_sim, info in all_ages.items():
      strip_age = info[-1]
      relevant_ages.append(strip_age)

   for name_sim, info in all_radius.items():
      strip_radius = info[-1]
      relevant_radius.append(strip_radius)

   
   all_data = mh.merge_all_data(normal_models)
   for folder_name,data in all_data.items():
      if folder_name == "RG" or folder_name=="AGB" or folder_name=="TPAGB":
         mh.radius_time(data,folder_name,ax1)
         ax1.get_xaxis().get_offset_text().set_visible(False)
         ax_max = max(ax1.get_xticks())
         exponent_axis = np.floor(np.log10(ax_max)).astype(int)
         ax1.annotate(r'$\times 10^{}$'.format(exponent_axis),
          xy=(1.02, .04), xycoords='axes fraction', fontsize=9)
      else:
         continue

   ax1.scatter(relevant_ages,relevant_radius, c="red", zorder=1)
   for k,j in enumerate(he_folders):
      ax1.annotate('{}'.format(j),xy=(relevant_ages[k],relevant_radius[k]),fontsize=8,xytext=(-20-k*25,-27),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=0.5))

   ax1.annotate(mass_folder, xy=(0.15, 0.8),xycoords='axes fraction', fontsize=12, horizontalalignment='center', verticalalignment='top')

   

   i+=1
   
handles, labels = ax1.get_legend_handles_labels()
leg = fig.legend(handles, labels, fontsize="x-small", ncol = 1, loc="right", bbox_to_anchor = (.98,.834))
fig.subplots_adjust(right=0.77)
fig.supylabel("$r/R_\odot$")
fig.supxlabel("$t$ (years)")

        
            

#fig, axs = plt.subplots(2,2, constrained_layout=True)
#
#i=0
#for mass_folder, list_subfolders in mass_file_models.items():
#   column = i % 2
#   row = row_maker(i)
#   
#   axs[row,column].plot(line_xs,line_ys, c="red", ls="dotted", lw = 0.8)
#   axs[row,column].fill_between(line_xs, line_ys, 0, color='red', alpha=.1)
#   for bh_mass in bh_masses:
#      for each in list_subfolders:
#         folder = each['folder_path']
#         models = each['models']
#         name = each['name']
#         if '050he' in name:
#            for model in models:
#               p = mh.get_file(folder,model)
#               data = mh.get_params(p)
#               mh.tidal_radius_mass_fraction(data,axs[row,column],bh_mass,'{:.0e} $M_{}$'.format(bh_mass,'{BH}'))
#               axs[row,column].annotate(name, xy=(0.05, 0.1),xycoords='axes fraction', fontsize=12, horizontalalignment='left', verticalalignment='bottom')
#         else:
#            continue
#   i+=1
#
#plt.grid(False)
#
#fig.supxlabel("$f_s=1-\\frac{M(r)}{M_\star}$")
#fig.supylabel("$\\frac{R_t}{r_g} =  \left(\\frac {M_{BH}}{M(r)}\\right)^{1/3} r \\frac{c^2}{G M_{BH}}$")
#fig.suptitle("Tidal radius as a function of the fraction stripped")
#
plt.show()

