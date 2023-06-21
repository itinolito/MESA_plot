import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm

def main():
    folder = input("Folder name: ")
    sim_folder = '/Users/nunina/MESA/Simulations/'

    to_plot = gfm.generate_file_models(sim_folder + folder)
    mh.all_time(to_plot)

    plt.show()

if __name__ == '__main__':
    main()