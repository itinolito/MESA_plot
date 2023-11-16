import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys


m07 = {
            '07m05c01z03s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/050he/strip02/s02_TPAGB', 
                  'name': 's02_tpagb', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/050he/strip02/s02_WD', 
                  'name': 's02_wd', 'models': [1000, 10476]}, 
                ],
            '07m01c01z00s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.7M01Z/normal/RG', 
                  'name': 's02_tpagb', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.7M01Z/normal/AGB', 
                  'name': 's02_wd', 'models': [1000, 10476]}, 
               ],
            '07m05c01z13s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip02/s02_TPAGB', 
                  'name': 's02_tpagb', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip02/s02_WD', 
                  'name': 's02_wd', 'models': [1000, 10476]}, 
               ],
            '07m01z03s25he': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/s02/s02_TPAGB', 
                  'name': 's02_tpagb', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/s02/s02_WD', 
                  'name': 's02_wd', 'models': [1000, 10476]}, 
                ],
            '07m01z03s75he': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/s02/s02_TPAGB', 
                  'name': 's02_tpagb', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/s02/s02_WD', 
                  'name': 's02_wd', 'models': [1000, 10476]}, 
                ],
            '08m06c01z22s50he': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/3M01Z/strip02/s02_TPAGB', 
                  'name': 's02_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/3M01Z/strip02/s02_WD', 
                    'name': 's02_WD', 'models': [1000, 10476]}],
            }

m10 = {'30m06c01z00s': 
               [
                {'folder_path': '/Volumes/NO NAME/Simulations/3M01Z/normal/RG', 
                 'name': 'RG', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/3M01Z/normal/AGB', 
                 'name': 'AGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/3M01Z/normal/TPAGB', 
                 'name': 'TPAGB', 'models': [1000, 10476]}], 
    '10m05c01z00s': 
               [#{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/preZAMS', 
                # 'name': 'preZAMS', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/MS', 
                # 'name': 'MS', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/normal/RG', 
                 'name': 'RG', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/normal/AGB', 
                 'name': 'AGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/normal/TPAGB', 
                 'name': 'TPAGB', 'models': [1000, 10476]}],
         '10m06c01z20s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/3M01Z/050he/strip04/s04_TPAGB', 
                 'name': 's04_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/3M01Z/050he/strip04/s04_WD', 
                   'name': 's04_WD', 'models': [1000, 10476]}],  
         '09m05c01z11s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/050he/strip04/s04_TPAGB', 
                 'name': 's04_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/050he/strip04/s04_WD', 
                   'name': 's04_WD', 'models': [1000, 10476]}],
         '11m05c01z09s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/050he/strip06/s06_TPAGB', 
                 'name': 's06_TPAGB', 'models': [1000, 10676]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/050he/strip06/s06_WD', 
                   'name': 's06_WD', 'models': [1000, 10476]}],  
}

s1m01z025 = {
            '10m05c01z00s': 
               [#{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/preZAMS', 
                # 'name': 'preZAMS', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/MS', 
                # 'name': 'MS', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/normal/RG', 
                 'name': 'RG', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/normal/AGB', 
                 'name': 'AGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/normal/TPAGB', 
                 'name': 'TPAGB', 'models': [1000, 10476]}], 
            '07m05c01z03s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/s02/s02_TPAGB', 
                  'name': 's02_tpagb', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/s02/s02_WD', 
                  'name': 's02_wd', 'models': [1000, 10476]}, 
                ],}

s1m01z075 = {
            '10m05c01z00s': 
               [#{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/preZAMS', 
                # 'name': 'preZAMS', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/MS', 
                # 'name': 'MS', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/normal/RG', 
                 'name': 'RG', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/normal/AGB', 
                 'name': 'AGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/normal/TPAGB', 
                 'name': 'TPAGB', 'models': [1000, 10476]}], 
            '07m05c01z03s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/s02/s02_TPAGB', 
                  'name': 's02_tpagb', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/s02/s02_WD', 
                  'name': 's02_wd', 'models': [1000, 10476]}, 
                ],}
                   
s2m01z = {
            '20m05c01z00s': 
               [#{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/preZAMS', 
                # 'name': 'preZAMS', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/MS', 
                # 'name': 'MS', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/normal/RG', 
                 'name': 'RG', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/normal/AGB', 
                 'name': 'AGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/normal/TPAGB', 
                 'name': 'TPAGB', 'models': [1000, 10476]}], 
            '07m05c01z13s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip02/s02_TPAGB', 
                  'name': 's02_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip02/s02_WD', 
                    'name': 's02_WD', 'models': [1000, 10476]}],
            '09m05c01z11s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip04/s04_TPAGB', 
                 'name': 's04_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip04/s04_WD', 
                   'name': 's04_WD', 'models': [1000, 10476]}],
            '11m05c01z09s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip06/s06_TPAGB', 
                 'name': 's06_TPAGB', 'models': [1000, 10676]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip06/s06_WD', 
                   'name': 's06_WD', 'models': [1000, 10476]}],
            '13m05c01z07s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip08/s08_TPAGB', 
                 'name': 's08_TPAGB', 'models': [1000, 10876]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip08/s08_WD', 
                   'name': 's08_WD', 'models': [1000, 10476]}],
            '15m05c01z05s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip1/s1_TPAGB', 
                 'name': 's1_TPAGB', 'models': [1000, 10876]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip1/s1_WD', 
                   'name': 's08_WD', 'models': [1000, 10476]}],
            '17m05c01z03s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip1.2/s1.2_TPAGB', 
                 'name': 's1.2_TPAGB', 'models': [1000, 11.276]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip1.2/s1.2_WD', 
                   'name': 's08_WD', 'models': [1000, 10476]}],
            '19m05c01z01s': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip1.4/s1.4_TPAGB', 
                 'name': 's1.4_TPAGB', 'models': [1000, 11.476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/strip1.4/s1.4_WD', 
                   'name': 's08_WD', 'models': [1000, 10476]}],}

s08m01z = {
            '0.8M01Z': 
               [#{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/preZAMS', 
                # 'name': 'preZAMS', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/MS', 
                # 'name': 'MS', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/normal/RG', 
                 'name': 'RG', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/normal/AGB', 
                 'name': 'AGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/normal/TPAGB', 
                 'name': 'TPAGB', 'models': [1000, 10476]}], 
            's0': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/strip0/s0_TPAGB', 
                  'name': 's0_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/strip0/s0_WD', 
                    'name': 's0_WD', 'models': [1000, 10476]}],
            's02': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/strip02/s02_TPAGB', 
                  'name': 's02_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/strip02/s02_WD', 
                    'name': 's02_WD', 'models': [1000, 10476]}],
            's04': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/strip04/s04_TPAGB', 
                 'name': 's04_TPAGB', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.8M01Z/strip04/s04_WD', 
                   'name': 's04_WD', 'models': [1000, 10476]}],}

s08m1z = {
            '0.8M1Z': 
               [#{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/preZAMS', 
                # 'name': 'preZAMS', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/MS', 
                # 'name': 'MS', 'models': [1000, 10476]}, 
                {'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/normal/RG', 
                 'name': 'RG', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/normal/AGB', 
                # 'name': 'AGB', 'models': [1000, 10476]}, 
                #{'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/normal/TPAGB', 
                # 'name': 'TPAGB', 'models': [1000, 10476]}
                ], 
            's0': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/strip0/s0_TPAGB', 
                  'name': 's0_TPAGB', 'models': [1000, 10476]}, 
                ],
            's01': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/strip01/s01_TPAGB', 
                  'name': 's01_TPAGB', 'models': [1000, 10476]}, 
                ],
            's02': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/strip02/s02_TPAGB', 
                  'name': 's02_TPAGB', 'models': [1000, 10476]}, 
                ],
            's03': 
               [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/strip03', 
                  'name': 's03', 'models': [1000, 10476]}, 
                ],
                }

strip_model08m1z = {'strip': [{'folder_path': '/Volumes/NO NAME/Simulations/0.8M1Z/LOGS_stop_at_RG', 
                 'name': 'stop', 'models': [1000, 10476]},]}

strip_model1m01z050 = {'strip': [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/050he/LOGS_stop_at_RG', 
                 'name': 'stop', 'models': [1000, 10476]},]}

strip_model1m01z025 = {'strip': [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/025he/LOGS_stop_at_RG', 
                 'name': 'stop', 'models': [1000, 10476]},]}

strip_model1m01z075 = {'strip': [{'folder_path': '/Volumes/NO NAME/Simulations/1M01Z/075he/LOGS_stop_at_RG', 
                 'name': 'stop', 'models': [1000, 10476]},]}

strip_model2m01z050 = {'strip': [{'folder_path': '/Volumes/NO NAME/Simulations/2M01Z/LOGS_stop_at_RG',
                                                   'name': 'stop', 'models': [1000, 10476]},]}


#mh.all_time_reduced(s1m01z,strip_model1m01z)
#mh.all_time_reduced(s08m1z,strip_model08m1z)
#mh.all_time_reduced(s2m01z,strip_model2m01z050)
#mh.all_time_reduced(s1m01z025,strip_model1m01z025)
mh.all_time_reduced(m10,strip_model1m01z050)

#mh.all_time_reduced(m07,strip_model1m01z050)
#plt.savefig(sim_folder+'merged.png')
plt.show()




