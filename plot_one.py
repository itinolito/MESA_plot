import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys


sim_folder = '/Volumes/NO NAME/Simulations/'

file_models_1 = {'1M01Z': [
                {'folder_path': sim_folder+'/1M01Z/normal/MS', 
                 'name': 'Main Sequence', 'models': [284]},
                {'folder_path': sim_folder+'/1M01Z/025he/LOGS_stop_at_RG', 
                 'name': 'RG at 0.25 He fraction', 'models': [8348]},
                {'folder_path': sim_folder+'/1M01Z/050he/LOGS_stop_at_RG', 
                 'name': 'RG at 0.50 He fraction', 'models': [8331]},
                {'folder_path': sim_folder+'/1M01Z/075he/LOGS_stop_at_RG', 
                 'name': 'RG at 0.75 He fraction', 'models': [8312]}],   
}

file_models_2 = {'2M01Z': [
                {'folder_path': sim_folder+'/2M01Z/normal/MS', 
                 'name': 'Main Sequence', 'models': [288]},
                {'folder_path': sim_folder+'/2M01Z/025he/LOGS_stop_at_RG', 
                 'name': 'RG at 0.25 He fraction', 'models': [5139]},
                {'folder_path': sim_folder+'/2M01Z/050he/LOGS_stop_at_RG', 
                 'name': 'RG at 0.50 He fraction', 'models': [5110]},
                {'folder_path': sim_folder+'/2M01Z/075he/LOGS_stop_at_RG', 
                 'name': 'RG at 0.75 He fraction', 'models': [5073]}],   
}

#file_models = {'0.7M01Z': [
#                {'folder_path': sim_folder+'/0.7M01Z/normal/RG', 
#                 'name': '0.7M', 'models': [300,600,1200,3800,5900,6600]},],   
#}

plt.rcParams['figure.figsize'] = (5,6)
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.minorticks_on()

for mass_folder, data in file_models_1.items():
    for each in data:
        folder = each['folder_path']
        models = each['models']
        name = each['name']
        
        for model in models:
            p = mh.get_file(folder,model)
            data = mh.get_params(p)
            mh.density_mass(data,model,name,ax1)
            #mh.tidal_radius_mass_fraction(data,ax,10e3,name)

ax2 = fig.add_subplot(2,1,2)
ax2.minorticks_on()

for mass_folder, data in file_models_2.items():
    for each in data:
        folder = each['folder_path']
        models = each['models']
        name = each['name']
        
        for model in models:
            p = mh.get_file(folder,model)
            data = mh.get_params(p)
            mh.density_mass(data,model,name,ax2)
            #mh.tidal_radius_mass_fraction(data,ax,10e3,name)

ax1.annotate('1M01Z', xy=(0.15, 0.15),xycoords='axes fraction', fontsize=12, horizontalalignment='center', verticalalignment='top')
ax2.annotate('2M01Z', xy=(0.15, 0.15),xycoords='axes fraction', fontsize=12, horizontalalignment='center', verticalalignment='top')

fig.suptitle("Density profiles")
fig.supylabel("$\log_{\ 10} \; \left(\\rho/\\rho_\odot\\right)$")
ax2.set_xlabel("$m/M_\odot$")
handles, labels = ax1.get_legend_handles_labels()
leg = fig.legend(handles, labels, fontsize="x-small", ncol=2,loc="lower center")
fig.subplots_adjust(bottom=.17)
plt.show()

