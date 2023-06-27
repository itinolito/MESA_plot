import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys

def main():
    sim_folder = '/Users/nunina/MESA/Simulations/'
    folder = sim_folder+sys.argv[i+1]
    to_plot = gfm.generate_file_models(sim_folder + folder)
    mh.all_time(to_plot)
    plt.show()

if __name__ == '__main__':
    main()
