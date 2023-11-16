import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys

def main():
    sim_folder = '/Users/nunina/MESA/Simulations/ALL/def/'
    folder=sim_folder+"2M1Z"
    #folder = sim_folder+'1M01Z/025he/normal'#sys.argv[1]
    to_plot = gfm.generate_file_models(folder)
    mh.all_time(to_plot)
    #plt.savefig(folder+'.png')
    plt.show()

if __name__ == '__main__':
    main()
