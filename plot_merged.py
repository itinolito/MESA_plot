import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys

def main():

    sim_folder = '/Users/nunina/MESA/Simulations/ALL/temp_res/'
    folders = []
    for i in range(len(sys.argv)-1):
        folder = sim_folder+sys.argv[i+1]
        folders.append(folder)
    to_plot = gfm.generate_multiple_sim(folders)
    #mh.all_time(to_plot)
    mh.all_time_reduced(to_plot)
    #plt.savefig(sim_folder+'merged.png')
    plt.show()

if __name__ == '__main__':
    main()



