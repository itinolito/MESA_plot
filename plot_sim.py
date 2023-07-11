import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys

def main():
    sim_folder = '/Users/nunina/MESA/Simulations/MS/'
    folder = sim_folder+sys.argv[1]
    to_plot = gfm.generate_file_models(folder)
    mh.all_time(to_plot)
    #plt.savefig(folder+'.png')
    plt.show()

if __name__ == '__main__':
    main()
