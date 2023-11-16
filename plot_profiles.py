import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys


file_models = {
            'Before stripping': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/0.8M1Z/LOGS_stop_at_RG/', 
                 'name': 'RG', 'models': [508]},], 
            #'s0': 
            #   [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/0.8M1Z/strip0/s0_TPAGB/', 
            #     'name': 's0', 'models': [578]}, ],
            's01': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/0.8M1Z/strip01/s01_TPAGB/', 
                 'name': 's01', 'models': [600]}, ],
            's02': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/0.8M1Z/strip02/s02_TPAGB/', 
                  'name': 's02', 'models': [600]}, ],
                }


s2m01z = {
            'Before stripping': 
               [#{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/1M01Z/preZAMS', 
                # 'name': 'preZAMS', 'models': [1000, 10476]}, 
                #{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/1M01Z/MS', 
                # 'name': 'MS', 'models': [1000, 10476]}, 
                {'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/LOGS_stop_at_RG', 
                 'name': 'RG', 'models': [5110]}], 
            '07m05c01z02s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/strip02/s02_TPAGB', 
                  'name': 's02_TPAGB', 'models': [5200]}, 
                ],
            '09m05c01z04s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/strip04/s04_TPAGB', 
                 'name': 's04_TPAGB', 'models': [5200]}, 
                ],
            '11m05c01z06s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/strip06/s06_TPAGB', 
                 'name': 's06_TPAGB', 'models': [5200]}, 
                ],
            '13m05c01z08s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/strip08/s08_TPAGB', 
                 'name': 's08_TPAGB', 'models': [5200]}, 
                ],
            '15m05c01z10s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/strip1/s1_TPAGB', 
                 'name': 's1_TPAGB', 'models': [5200]}, 
                ],
            '17m05c01z12s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/strip1.2/s1.2_TPAGB', 
                 'name': 's1.2_TPAGB', 'models': [5200]}, 
                ],
            '19m05c01z14s': 
               [{'folder_path': '/Users/nunina/MESA/Simulations/ALL/def/2M01Z/050he/strip1.4/s1.4_TPAGB', 
                 'name': 's1.4_TPAGB', 'models': [5200]}, 
                ],}
mh.plot_profile_mass(s2m01z)
plt.show()