from merge_history import *

sim_folder = '/home/'

strip_3M_20r = {
    '3M - NS' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_1',
            'name' : 'Core flash',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_2',
            'name' : 'End He burn',
            'models' : [10480,12430],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_3',
            'name' : 'End AGB',
            'models' : [12560,12880],
        },
#        {
#            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS',
#            'name' : 'End WD',
#            'models' : [12900,13312],
#        },
    ],
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
    ],
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
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_6',
#            'name' : 'Stage 6',
#            'models' : [10100],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_7',
#            'name' : 'Stage 7',
#            'models' : [13000],
#        },
#        {
#            'folder_path' : '/home/nuria/Simulations/At_mid_RG/At_5R/1M_strip_retain05/LOGS_8',
#            'name' : 'Stage 8',
#            'models' : [15000],
#        },
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
#        {
#            'folder_path' : '/home/nuria/Simulations/3M/3M_strip_retain1/LOGS',
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


star_4M = {
    '4M' : [
        {
            'folder_path' : '/home/nuria/Simulations/4M_from_7M_testsuite/LOGS',
            'name' : '4M',
            'models' : [300,600],
        },
    ],
}

star_4M_with_test = {
    '4M' : [
        {
            'folder_path' : '/home/nuria/Simulations/12M_pre_ms_to_core_collapse/LOGS',
            'name' : '4M',
            'models' : [300,600],
        },
    ],
}
star_06M = {
    '0.6M' : [
        {
            'folder_path' : '/home/nuria/Simulations/06M_from_tutorial/LOGS',
            'name' : '0.6M',
            'models' : [300,600],
        },
    ],
}

M3_tests = {
    '3M - NS' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_1',
            'name' : 'Core flash',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_2',
            'name' : 'End He burn',
            'models' : [10480,12430],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M/3M_all/LOGS_3',
            'name' : 'End AGB',
            'models' : [12560,12880],
        },
    ],
    '3M_tests' : [
        {
            'folder_path' : '/home/nuria/Simulations/3M_test/LOGS_1',
            'name' : '3M',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M_test/LOGS_2',
            'name' : '3M',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M_test/LOGS_3',
            'name' : '3M',
            'models' : [1000,10476],
        },
        {
            'folder_path' : '/home/nuria/Simulations/3M_test/',
            'name' : '3M',
            'models' : [1000,10476],
        },
    ]
}

all_time(strip_3M_20r)

plt.show()