from lzma import MODE_NORMAL
import mesa_reader as mr
import mesaPlot as mp
from astropy import constants as const
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

plt.style.use('aesthetic.mplstyle')

history=True

strip_1M_10r = {
    'Non-stripped RG' : [
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_start_he_core_flash',
            'name' : 'Core flash',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_core_he_burn',
            'name' : 'End He burn',
            'models' : [10480,12430],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_agb',
            'name' : 'End AGB',
            'models' : [12560,12880],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_wd',
            'name' : 'End WD',
            'models' : [12900,13312],
        },
    ],
    'Fully stripped' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_all/LOGS_evolve_stripped',
            'name' : 'Strip',
            'models' : [1000,2000],
        },
    ],
    'Partially stripped - retain 0.2M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain02/LOGS_8',
            'name' : 'Stage 8',
            'models' : [14000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_8',
            'name' : 'Stage 8',
            'models' : [15000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_9',
            'name' : 'Stage 9',
            'models' : [17000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_10',
            'name' : 'Stage 10',
            'models' : [19000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_11',
            'name' : 'Stage 11',
            'models' : [21000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_12',
            'name' : 'Stage 12',
            'models' : [23000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_13',
            'name' : 'Stage 13',
            'models' : [25000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_14',
            'name' : 'Stage 15',
            'models' : [27000],
        },
    ],
    'Partially stripped - retain 0.6M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain03/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_8',
            'name' : 'Stage 8',
            'models' : [15000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_9',
            'name' : 'Stage 9',
            'models' : [17000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_10',
            'name' : 'Stage 10',
            'models' : [19000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_11',
            'name' : 'Stage 11',
            'models' : [21000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_12',
            'name' : 'Stage 12',
            'models' : [23000],
        },
    ]
}

strip_1M_10r_longterm = {
    'Non-stripped RG' : [
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_start_he_core_flash',
            'name' : 'Core flash',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_core_he_burn',
            'name' : 'End He burn',
            'models' : [10480,12430],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_agb',
            'name' : 'End AGB',
            'models' : [12560,12880],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_wd',
            'name' : 'End WD',
            'models' : [12900,13312],
        },
    ],
    'Partially stripped - retain 0.3M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_8',
            'name' : 'Stage 8',
            'models' : [15000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_9',
            'name' : 'Stage 9',
            'models' : [17000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_10',
            'name' : 'Stage 10',
            'models' : [19000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_11',
            'name' : 'Stage 11',
            'models' : [21000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_12',
            'name' : 'Stage 12',
            'models' : [23000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_13',
            'name' : 'Stage 13',
            'models' : [25000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_14',
            'name' : 'Stage 14',
            'models' : [27000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_later_1',
            'name' : 'Later 1',
            'models' : [35000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_later_2',
            'name' : 'Later 2',
            'models' : [42000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_later_3',
            'name' : 'Later 3',
            'models' : [50000],
        },
    ],
    'Partially stripped - retain 0.6M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain03/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain06/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/At_10R/1M_strip_retain06/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_8',
            'name' : 'Stage 8',
            'models' : [15000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_9',
            'name' : 'Stage 9',
            'models' : [17000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_10',
            'name' : 'Stage 10',
            'models' : [19000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_11',
            'name' : 'Stage 11',
            'models' : [21000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_12',
            'name' : 'Stage 12',
            'models' : [23000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS_later_1',
            'name' : 'Later 1',
            'models' : [30000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_strip_retain06/LOGS',
            'name' : 'Later 2',
            'models' : [40000],
        },
    ]
}

rg_at_10r = {
        'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_10R/1M_stop_at_10R/LOGS_to_RG_10R',
        'name' : 'Red giant',
        'models' : [920]
    }

three_solar_mass = {
    'Start' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_start',
            'name' : 'Start',
            'models' : [100],
        }
    ],
    'End H burn' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_to_end_core_h_burn',
            'name' : 'End H burn',
            'models' : [300],
        }
    ],
    'Start He flash' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_to_start_he_core_flash',
            'name' : 'He flash',
            'models' : [400],
        }
    ],
    'End He burn' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_to_end_core_he_burn',
            'name' : 'End He Burn',
            'models' : [600],
        }
    ],
    'Rest' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS',
            'name' : 'End He Burn',
            'models' : [9800],
        }
    ],
}

strip_1M_5r = {
    'Non-stripped RG' : [
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_start_he_core_flash',
            'name' : 'Core flash',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_core_he_burn',
            'name' : 'End He burn',
            'models' : [10480,12430],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_agb',
            'name' : 'End AGB',
            'models' : [12560,12880],
        },
        {
            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_wd',
            'name' : 'End WD',
            'models' : [12900,13312],
        },
    ],
    'Fully stripped' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_all/LOGS_evolve_stripped',
            'name' : 'Strip',
            'models' : [1000,2000],
        },
    ],
    'Partially stripped - retain 0.2M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_8',
            'name' : 'Stage 8',
            'models' : [14000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_9',
            'name' : 'Stage 9',
            'models' : [16000],
        },
    ],
    'Partially stripped - retain 0.3M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_8',
            'name' : 'Stage 8',
            'models' : [15000],
        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_9',
#            'name' : 'Stage 9',
#            'models' : [17000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_10',
#            'name' : 'Stage 10',
#            'models' : [19000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_11',
#            'name' : 'Stage 11',
#            'models' : [21000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_12',
#            'name' : 'Stage 12',
#            'models' : [23000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_13',
#            'name' : 'Stage 13',
#            'models' : [25000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_14',
#            'name' : 'Stage 15',
#            'models' : [27000],
#        },
    ],
    'Partially stripped - retain 0.5M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_7',
            'name' : 'Stage 7',
            'models' : [13000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_8',
            'name' : 'Stage 8',
            'models' : [15000],
        },
    ],    
    'Partially stripped - retain 0.6M' : [
        {
            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_2',
#            'name' : 'Stage 2',
#            'models' : [3000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_3',
#            'name' : 'Stage 3',
#            'models' : [5000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_4',
#            'name' : 'Stage 4',
#            'models' : [7000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_5',
#            'name' : 'Stage 5',
#            'models' : [9000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_6',
#            'name' : 'Stage 6',
#            'models' : [10100],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS',
#            'name' : 'Stage 7',
#            'models' : [13000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_8',
#            'name' : 'Stage 8',
#            'models' : [15000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_9',
#            'name' : 'Stage 9',
#            'models' : [17000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_10',
#            'name' : 'Stage 10',
#            'models' : [19000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_11',
#            'name' : 'Stage 11',
#            'models' : [21000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_12',
#            'name' : 'Stage 12',
#            'models' : [23000],
#        },
    ]
}


strip_3M_20r = {
#    'Non-stripped RG' : [
#        {
#            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_start_he_core_flash',
#            'name' : 'Core flash',
#            'models' : [1000,10476],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_core_he_burn',
#            'name' : 'End He burn',
#            'models' : [10480,12430],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_end_agb',
#            'name' : 'End AGB',
#            'models' : [12560,12880],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/1M/LOGS_to_wd',
#            'name' : 'End WD',
#            'models' : [12900,13312],
#        },
#    ],
    '3M - FS' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_all/LOGS_evolve_stripped',
            'name' : 'Strip',
            'models' : [1000,2000],
        },
    ],
    '3M - retain 0.2M' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain02/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain02/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain02/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain02/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain02/LOGS_5',
            'name' : 'Stage 5',
            'models' : [9000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain02/LOGS_6',
            'name' : 'Stage 6',
            'models' : [10100],
        },
#        {
#            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain02/LOGS',
#            'name' : 'Stage 7',
#            'models' : [13000],
#        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_8',
##            'name' : 'Stage 8',
##            'models' : [14000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain02/LOGS_9',
##            'name' : 'Stage 9',
##            'models' : [16000],
##        },
    ],
##    'Partially stripped - retain 0.5M' : [
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_1',
##            'name' : 'Stage 1',
##            'models' : [940,1300],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_2',
##            'name' : 'Stage 2',
##            'models' : [3000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_3',
##            'name' : 'Stage 3',
##            'models' : [5000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_4',
##            'name' : 'Stage 4',
##            'models' : [7000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_5',
##            'name' : 'Stage 5',
##            'models' : [9000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_6',
##            'name' : 'Stage 6',
##            'models' : [10100],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_7',
##            'name' : 'Stage 7',
##            'models' : [13000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_8',
##            'name' : 'Stage 8',
##            'models' : [15000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_9',
##            'name' : 'Stage 9',
##            'models' : [17000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_10',
##            'name' : 'Stage 10',
##            'models' : [19000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_11',
##            'name' : 'Stage 11',
##            'models' : [21000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_12',
##            'name' : 'Stage 12',
##            'models' : [23000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_13',
##            'name' : 'Stage 13',
##            'models' : [25000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain03/LOGS_14',
##            'name' : 'Stage 15',
##            'models' : [27000],
##        },
##    ],
    '3M - retain 0.7M' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain07/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain07/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain07/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain07/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain07/LOGS',
            'name' : 'Stage 5',
            'models' : [9000],
        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_6',
##            'name' : 'Stage 6',
##            'models' : [10100],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_7',
##            'name' : 'Stage 7',
##            'models' : [13000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_8',
##            'name' : 'Stage 8',
##            'models' : [15000],
##        },
    ],    
    '3M - retain 1M' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain1/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain1/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain1/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain1/LOGS_4',
            'name' : 'Stage 4',
            'models' : [7000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain1/LOGS',
            'name' : 'Stage 5',
            'models' : [9000],
        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_6',
##            'name' : 'Stage 6',
##            'models' : [10100],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS',
##            'name' : 'Stage 7',
##            'models' : [13000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_8',
##            'name' : 'Stage 8',
##            'models' : [15000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_9',
##            'name' : 'Stage 9',
##            'models' : [17000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_10',
##            'name' : 'Stage 10',
##            'models' : [19000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_11',
##            'name' : 'Stage 11',
##            'models' : [21000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_12',
##            'name' : 'Stage 12',
##            'models' : [23000],
##        },
    ],
    '3M - retain 2M' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain2/LOGS_1',
            'name' : 'Stage 1',
            'models' : [940,1300],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain2/LOGS_2',
            'name' : 'Stage 2',
            'models' : [3000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain2/LOGS_3',
            'name' : 'Stage 3',
            'models' : [5000],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain2/LOGS',
            'name' : 'Stage 4',
            'models' : [7000],
        },
##        {
##            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain1/LOGS',
##            'name' : 'Stage 5',
##            'models' : [9000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_6',
##            'name' : 'Stage 6',
##            'models' : [10100],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS',
##            'name' : 'Stage 7',
##            'models' : [13000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_8',
##            'name' : 'Stage 8',
##            'models' : [15000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_9',
##            'name' : 'Stage 9',
##            'models' : [17000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_10',
##            'name' : 'Stage 10',
##            'models' : [19000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_11',
##            'name' : 'Stage 11',
##            'models' : [21000],
##        },
##        {
##            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain06/LOGS_12',
##            'name' : 'Stage 12',
##            'models' : [23000],
##        },
    ]
}


stripping_mass_1M_10R = {
        'Strip all' : 0.249791839625131,
        'Retain 0.2' : 0.444791839625131,
        'Retain 0.3' : 0.544791839625131,
        'Retain 0.6' : 0.844791839625131,
        }

def get_file(file,model):
    if history:
        history_data = file + '/history.data'
        p=mr.MesaData(history_data)
        return p
    else:
        h=mr.MesaLogDir(file)
        p=h.profile_data(model_number=model)
        return p

def get_params(p):
    params = {}
    if history:
    #   Star parameters FOR HISTORY
        params = {
            'log_radius': p.log_R,
            'mass': p.star_mass,
            'age': p.star_age,
            'log_density': p.log_cntr_Rho,
            'pp': p.pp,
            'cno': p.cno,
            'trialpha': p.tri_alpha,
            'he_core_mass': p.he_core_mass,
            'co_core_mass': p.co_core_mass,
            'log_temp_eff': p.log_Teff,
            'log_luminosity': p.log_L,
            'log_center_T': p.log_cntr_T,
            'log_P': p.log_cntr_P,
            'h1': p.center_h1,
            'he4': p.center_he4,
            'c12': p.center_c12,
            'o16': p.center_o16,
            'mass_h': p.total_mass_h1,
            'mass_he': p.total_mass_he4,
            'log_Teff' : p.log_Teff
        }
    else:
    #   Star parameters FOR PARTICULAR PROFILE OR MODEL
        params = {
            'log_radius' : p.logR,
            'mass' : p.mass,
            'age' : p.star_age,
            'log_density' : p.logRho,
            'log_temp' : p.logT,
            'luminosity' : p.luminosity,
            'hydrogen' : p.x_mass_fraction_H,
            'helium' : p.y_mass_fraction_He,
            'pp' : p.pp,
            'cno' : p.cno,
            'trialpha' : p.tri_alpha,
            'h1' : p.h1,
            'he3' : p.he3,
            'he4' : p.he4,
            'c12' : p.c12,
            'n14' : p.n14,
            'o16' : p.o16,
            'ne20' : p.ne20,
            'mg24' : p.mg24,
        }
    #    fe56=p.fe56
    #    ni58=p.ni58 
    
    params['radius'] = 10**params['log_radius']
    params['density'] = 10**params['log_density']
    
    return params

def aggregate_data(stages):

    all_parameters = {}
    if history:
        for stage in stages:
            folder_name = stage['name']
            model = stage['models']
            mesa_param_obj = get_file(stage['folder_path'],model)
            all_parameters[folder_name] = get_params(mesa_param_obj)

    else:    
        for stage in stages:
            folder_name = stage['name']
            all_parameters[folder_name] = {}
            for model in stage['models']:
                mesa_param_obj = get_file(stage['folder_path'],model)
                all_parameters[folder_name][model] = get_params(mesa_param_obj)

    return all_parameters

def merge_history(data_to_merge):
    merged_data = {}
    for name, folder_data in data_to_merge.items():
        for parameter, value_list in folder_data.items():
            parameter_list = merged_data.get(parameter, [])
            parameter_list.extend(value_list)
            merged_data[parameter] = parameter_list

    return merged_data

def merge_all_data(file_models):
    merged_file_models = {}
    for name, simulations in file_models.items():
        stage_data = aggregate_data(simulations)
        merged_file_models[name] = merge_history(stage_data)

    return merged_file_models


#-------------------------------------------------#
#----------------- HISTORY PLOTS -----------------#
#-------------------------------------------------#

def radius_time(data, name, plt):
    plt.set_yscale("log")
    plt.plot(data['age'],data['radius'], label = "for {stage}".format(stage=name))
    plt.set_ylabel("$r/R_\odot$")

def temp_time(data, name, plt):
    plt.plot(data['age'],data['log_Teff'], label = "for {stage}".format(stage=name))
    plt.set_ylabel("$\log_{10} T_{eff}$")

def elements_time(data, name, plt):
#    plt.xscale("log")
    plt.plot(data['age'],data['h1'], label="h1 for {stage}".format(stage=name))
    plt.plot(data['age'],data['he4'], label="he4 for {stage}".format(stage=name))
    plt.plot(data['age'],data['c12'], label="c12 for {stage}".format(stage=name))
    plt.plot(data['age'],data['o16'], label="o16 for {stage}".format(stage=name))
    plt.set_ylabel("Abundances")
    
def lum_time(data, name, plt):
    plt.plot(data['age'],data['log_luminosity'], label = "for {stage}".format(stage=name))
    plt.set_ylabel("$\log_{\ 10}(L/L_\odot)$ ")

def lum_temp_hr(data, name, plt):
    age = data['age']
    num_of_points = len(age)
    indices = list(np.logspace(start=1,stop=12,num=6, base=2, endpoint=True, dtype=np.int32))
    if name == 'Partially stripped - retain 0.2M':
        end_indices = list(range(max(num_of_points-520,0),max(num_of_points-450,0) + 1,3))
    else:
        end_indices = list(range(num_of_points-50,num_of_points+ 1,5))
    indices = end_indices + indices
    indices = [ind for ind in indices if ind < len(age)]
    plt.plot(data['log_Teff'],data['log_luminosity'], label = "for {stage}".format(stage=name), marker='.', markevery=indices)
    for i in indices[::2]:
        plt.text(data['log_Teff'][i],data['log_luminosity'][i],"{:.4}".format(age[i]/1e10))
    plt.set_ylabel("$\log_{\ 10}(L/L_\odot)$ ")
    plt.set_xlabel("$\log_{10} T_{eff}$ ")

def nuc_time(data, name, plt):
    plt.set_yscale("log")
    plt.plot(data['age'],data['pp'], label="$p-p$ for {stage}".format(stage=name))
    plt.plot(data['age'],data['cno'], label="$CNO$ for {stage}".format(stage=name))
    plt.plot(data['age'],data['trialpha'], label="$3-alpha$ for {stage}".format(stage=name))
    plt.set_ylabel("$\log_{\ 10} (L/L_{\odot})$")
    

#-------------------------------------------------#
#----------------- PROFILE PLOTS -----------------#
#-------------------------------------------------#

#--------------- PROFILE / RADIUS ----------------#

def density_radius(data,model,plt):
    plt.set_title("Density profile of a $1M_\odot$ ZAMS red giant")
    plt.xscale("log")
    plt.plot(data['radius'],data['log_density'], label="model {}".format(model))
    plt.set_xlabel("$r/R_\odot$")
    plt.set_ylabel("$\log_{\ 10} \; \left(ρ/ρ_\odot\\right)$")

def radius_mass(data,model,name,plt):
    plt.plot(data['mass'],data['radius'], label="model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_ylabel("$r/R_\odot$")
    
def elements_radius(data,model,plt):
    plt.set_title("Elements for model {}".format(model))
    plt.xscale("log")
    plt.plot(data['radius'],data['h1'], label="h1")
    plt.plot(data['radius'],data['he3'], label="he3")
    plt.plot(data['radius'],data['he4'], label="he4")
    plt.plot(data['radius'],data['c12'], label="c12")
    plt.plot(data['radius'],data['n14'], label="n14")
    plt.plot(data['radius'],data['o16'], label="o16")
    plt.plot(data['radius'],data['ne20'], label="ne20")
    plt.plot(data['radius'],data['mg24'], label="mg24")
#    plt.plot(data['radius'],fe56, label="fe56")
#    plt.plot(data['radius'],ni58, label="ni58")
    plt.set_xlabel("$r/R_\odot$")
    plt.set_ylabel("Abundances")

def tidal_radius_radius(data,model,plt):
    plt.set_title("$\\frac{ r}{M^{1/3}(r)}$ of a $1M_\odot$ ZAMS red giant")
    plt.xscale("log")
    plt.yscale("log")
    y=data['radius']/(data['mass'])**(1/3)
    plt.plot(data['radius'],y, label="model {}".format(model))
    plt.set_xlabel("$r/R_\odot$")
    plt.set_ylabel("$\\frac{ r}{M^{1/3}(r)}$")

#----------------- PROFILE / MASS ----------------#

def density_mass(data,model,name,plt):
#    plt.set_title("Density profile of a $1M_\odot$ ZAMS red giant")
    plt.plot(data['mass'],data['log_density'], label="model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_ylabel("$\log_{\ 10} \; \left(ρ/ρ_\odot\\right)$")
    plt.legend()
     
def elements_mass(data,model,name,plt):
#    plt.set_title("Elements for model {}".format(model))
    plt.plot(data['mass'],data['h1'], label="h1 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['he3'], label="he3 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['he4'], label="he4 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['c12'], label="c12 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['n14'], label="n14 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['o16'], label="o16 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['ne20'], label="ne20 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['mg24'], label="mg24 model {model_num} of {sim}".format(model_num=model, sim=name))
#    plt.plot(radius,fe56, label="fe56")
#    plt.plot(radius,ni58, label="ni58")
    plt.set_ylabel("Abundances")
    plt.legend()
    
def temp_density(data,model,name,plt):
    plt.set_title("Temperature-Density profile")
    plt.xscale("log")
    plt.plot(data['log_density'],data['log_temp'], label="model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_xlabel("$\log_{\ 10} \\rho$")
    plt.set_ylabel("$\log_{\ 10} T$")

def temp_mass(data,model,name,plt):
#    plt.set_title("Temperature-mass profile")
    plt.plot(data['mass'],data['log_temp'], label="model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_ylabel("$\log_{\ 10} T$")
    
def tidal_radius_mass(data,model,name,plt):
#    plt.set_title("$\\frac{ r}{M^{1/3}(r)}$ of a $1M_\odot$ ZAMS red giant")
#    plt.xscale("log")
#    plt.yscale("log")
    y=data['radius']/(data['mass'])**(1/3)
    plt.plot(data['mass'],y, label="model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_ylabel("$r/m^{1/3}$")

def nuc_energy(data,model,name,plt):
    plt.plot(data['mass'],data['pp'], label="pp model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['cno'], label="cno model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['trialpha'], label="$\\alpha$ model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_ylabel("$\epsilon$")


#-------------------------------------------------#
#-------------PLOT A BUNCH OF STUFF---------------#
#-------------------------------------------------#

def plot_profile_mass(file_models):
    fig, ax = plt.subplots(2,2, figsize=(10, 6))    
    fig.suptitle('Profiles')

    for name, simulations in file_models.items():
        simulations_data = aggregate_data(simulations)

        for folder_name, models_data in simulations_data.items():
            for model,data in models_data.items():
                density_mass(data,model,name,ax[0,0])
                #temp_mass(data,model,folder_name,ax[0,1])
                radius_mass(data,model,name,ax[0,1])
                #elements_mass(data,model,folder_name,ax[1,0])
                nuc_energy(data,model,name,ax[1,0])
                tidal_radius_mass(data,model,name,ax[1,1])

    ax[0,0].legend(fontsize="x-small")
    ax[1,0].legend(fontsize="x-small")
    ax[0,1].legend(fontsize="x-small")
    ax[1,1].legend(fontsize="x-small")

def plot_time(file_models):
    fig = plt.figure(constrained_layout = True)
    fig.suptitle('Evolution with time')
    spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
    ax1 = fig.add_subplot(spec[0, :])
    ax2 = fig.add_subplot(spec[1, 1:])
    ax3 = fig.add_subplot(spec[1:,0])
    ax3.invert_xaxis()
    ax4 = fig.add_subplot(spec[-1,1:])
#    ax1.set_xlim(1.217e10,1.236e10)
#    ax2.set_xlim(1.217e10,1.236e10)
#    ax4.set_xlim(1.217e10,1.236e10)
    ax1.set_xlim(1.204e10,1.236e10)
    ax2.set_xlim(1.204e10,1.236e10)
    ax4.set_xlim(1.204e10,1.236e10)
    
    all_data = merge_all_data(file_models)

    for folder_name,data in all_data.items():
        radius_time(data,folder_name,ax1)
        lum_time(data,folder_name,ax2)
        #nuc_time(data,folder_name,ax4)
        temp_time(data,folder_name,ax4)
        lum_temp_hr(data,folder_name,ax3)
    ax1.legend(fontsize="x-small")
    ax2.legend(fontsize="x-small")
    ax3.legend(fontsize="x-small")
    ax4.legend(fontsize="x-small")

def all_time(file_models):
    fig = plt.figure(constrained_layout = True)
    fig.suptitle('Evolution with time')
    spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
    ax1 = fig.add_subplot(spec[0, :])
    ax2 = fig.add_subplot(spec[1, 1:])
    ax3 = fig.add_subplot(spec[1:,0])
    ax3.invert_xaxis()
    ax4 = fig.add_subplot(spec[-1,1:])
    
    all_data = merge_all_data(file_models)

    for folder_name,data in all_data.items():
        radius_time(data,folder_name,ax1)
        lum_time(data,folder_name,ax2)
        #nuc_time(data,folder_name,ax4)
        temp_time(data,folder_name,ax4)
        lum_temp_hr(data,folder_name,ax3)
    ax1.legend(fontsize="x-small")
    ax2.legend(fontsize="x-small")
    ax3.legend(fontsize="x-small")
    ax4.legend(fontsize="x-small")

    #ax1.set_xlim(1.2e10,1.25e10)
    #ax2.set_xlim(1.2e10,1.25e10)
    #ax4.set_xlim(1.2e10,1.25e10)


def one_profile_plot(file_models, profile):
    # Plot one profile from a dictionary that contains folder_path, name and list of models.
    folder = file_models['folder_path']
    models = file_models['models']
    name = file_models['name']
    fig, ax = plt.subplots(1)
    ax.minorticks_on()
    for model in models:
        p = get_file(folder,model)
        data = get_params(p)
        profile(data,model,name,ax)
    for title,mass in stripping_mass_1M_10R.items():
        ax.axvline(mass, ls="--", c="indianred", lw="1", )
        ax.annotate(title, xy=(mass+0.01,8), rotation=90)
    ax.axvspan(stripping_mass_1M_10R['Retain 0.2'],stripping_mass_1M_10R['Retain 0.3'], color="indianred", alpha=0.2,lw=0)
    ax.set_xlabel("$m/M_\odot$")
    ax.set_title("Tidal radius profile for a $1M_\odot$ pre-ZAMS RG at time $R=10R_\odot$")

#-------------------------------------------------#
#--------------FIND PARTICULAR MODEL--------------#
#-------------------------------------------------#

def has_rg_radius(logR):
    return logR > 1.3

def has_large_lum(logL):
    return logL > 1

def find_models_function(function,parameter,file_models):
    my_models = file_models.copy()
    for name, simulations in my_models.items():
        for file_model in simulations:
            mesa_param_obj = mr.MesaLogDir(file_model['folder_path'])
            file_model['models'] = mesa_param_obj.select_models(function, parameter).tolist()
    return my_models

def find_data_model(function,parameter,file_models,my_data):
    my_models = find_models_function(function,parameter,file_models)

    my_models_data = {}
    for name,stages in my_models.items():
        stage_data = aggregate_data(stages)
        my_models_data[name] = stage_data

    found_info = {}
    for star_name, stages in my_models_data.items():
        found_info[star_name] = {}
        for folder_name,data in stages.items():
            found_info[star_name] = data[my_data]
    return found_info



#-------------------------------------------------#
#-----------------ACTUAL PROGRAM------------------#
#-------------------------------------------------#

#plot_profile_mass(file_models)
#plot_time(file_models)
#plot_time(stripping_1M_5r)
#all_time(strip_3M_20r)
#one_profile_plot(rg_at_10r,tidal_radius_mass)
#print(find_models_function(has_rg_radius,'log_R',three_solar_mass))
#print(find_data_model(has_rg_radius,'log_R',three_solar_mass,'age'))

#plt.savefig('test.png')
#print(find_models_function(has_rg_radius,'log_R',file_models))
#print(find_data_model(has_rg_radius,'log_R',file_models,'age'))


#one_file_path = file_models['Main sequence'][0]['folder_path']


#file = get_file(one_file_path,100)
#data = get_params(file)
#fig = plt.figure(constrained_layout = True)
#spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
#ax1 = fig.add_subplot(spec[0, :])
#ax2 = fig.add_subplot(spec[1, 1:])
#ax3 = fig.add_subplot(spec[1:,0])
#ax3.invert_xaxis()
#ax4 = fig.add_subplot(spec[-1,1:])
#
#radius_time(data,"MS",ax1)
#lum_time(data,"MS",ax2)
#nuc_time(data,"MS",ax4)
#lum_temp_hr(data,"MS",ax3)

#stripping_time_filepath = '/home/nuria/Simulations/At_mid_RG/At_10R/1M_stop_at_10R/LOGS_to_RG_10R'
#p = get_file(stripping_time_filepath,920)
#data = get_params(p)
#
#fig = plt.figure()
#spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
#plot = fig.add_subplot(spec[0, 0])
#plot.set_title('Newtonian tidal radius at stripping time')
#plot.set_xlabel('$m/M_\odot$')
#tidal_radius_mass(data,920,'Stripping time',plot)
#plt.show()

#Plot newtonian tidal radius at the stripping point