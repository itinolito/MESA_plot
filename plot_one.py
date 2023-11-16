import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys


sim_folder = '/Volumes/NO NAME/Simulations/'

file_models = {'1M01Z': [
                {'folder_path': sim_folder+'/1M01Z/010he/LOGS_stop_at_RG', 
                 'name': '010he', 'models': [8359]},
                {'folder_path': sim_folder+'/1M01Z/025he/LOGS_stop_at_RG', 
                 'name': '025he', 'models': [8348]},
                {'folder_path': sim_folder+'/1M01Z/050he/LOGS_stop_at_RG', 
                 'name': '050he', 'models': [8331]},
                {'folder_path': sim_folder+'/1M01Z/075he/LOGS_stop_at_RG', 
                 'name': '075he', 'models': [8312]}],   
}


fig, ax = plt.subplots(1)
ax.minorticks_on()

for mass_folder, data in file_models.items():
    for each in data:
        folder = each['folder_path']
        models = each['models']
        name = each['name']
        
        for model in models:
            p = mh.get_file(folder,model)
            data = mh.get_params(p)
            mh.tidal_radius_mass_fraction(data,ax,10e3,name)


plt.legend()
plt.show()

