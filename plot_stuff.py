import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm

def main():
    folder = '2M_tests'
    sim_folder = '/Users/nunina/MESA/Simulations/'

    m3_tests = {
        'to ZAMS' : [
            {
                'folder_path' : sim_folder + '3M_tests/LOGS_1',
                'name' : 'to ZAMS',
                'models' : [1000,10476],
            },
        ],
        'to TAMS' : [
            {
                'folder_path' : sim_folder + '3M_tests/LOGS_2',
                'name' : 'to TAMS',
                'models' : [1000,10476],
            },
        ],
        'to TACHeB' : [
            {
                'folder_path' : sim_folder + '3M_tests/LOGS_3',
                'name' : 'to TACHeB',
                'models' : [1000,10476],
            },
        ],
    }
    m3_overshoot_res = {
        #'to ZAMS' : [
        #    {
        #        'folder_path' : sim_folder + '3M_overshoot_res/LOGS_1',
        #        'name' : 'to ZAMS',
        #        'models' : [1000,10476],
        #    },
        #],
        #'to TAMS' : [
        #    {
        #        'folder_path' : sim_folder + '3M_overshoot_res/LOGS_2',
        #        'name' : 'to TAMS',
        #        'models' : [1000,10476],
        #    },
        #],
        #'to TACHeB' : [
        #    {
        #        'folder_path' : sim_folder + '3M_overshoot_res/LOGS_3',
        #        'name' : 'to TACHeB',
        #        'models' : [1000,10476],
        #    },
        #],
        'to AGB_ov_res' : [
            {
                'folder_path' : sim_folder + '3M_overshoot_res/LOGS_4',
                'name' : 'to AGB',
                'models' : [1000,10476],
            },
        ],
        'to AGB_ov' : [
            {
                'folder_path' : sim_folder + '3M_overshoot_res/',
                'name' : 'to AGB',
                'models' : [1000,10476],
            },
        ],
    }

    to_plot = gfm.generate_file_models(sim_folder + folder)
    mh.all_time(to_plot)

    plt.show()

if __name__ == '__main__':
    main()