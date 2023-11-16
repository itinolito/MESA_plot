import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys
import pandas as pd
from find_functions import *


def main():

    local_folder = '/Volumes/NO NAME/Simulations/'
    comp = 'total_mass'

    #Read dataframe with the corresponding axis comparison
    data = pd.read_csv('/Users/nunina/MESA/Simulations/ALL/def/tables/'+comp+'_comparison.csv')
    
 
    #Separate dataframes for each simulation into an array called sep_data
    for i in range(data['plot number'].max()+1):
        all_paths = []
        sub_data = data[data['plot number'] == i]
        for path in sub_data['Path']:
            if 'normal' in path:
                split_path = path.split("/")
                mass_folder = split_path[0]
                normal_folder = split_path[-1]
                all_paths.append(local_folder + mass_folder +'/'+ normal_folder)
            else:
                all_paths.append(local_folder + path)
        file_models = gfm.generate_multiple_sim(all_paths)
        mh.all_time(file_models)
        plt.show()

    

if __name__ == '__main__':
    main()



