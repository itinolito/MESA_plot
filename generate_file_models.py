import glob
import re

def sorter(string):
    sort_order = {
        'preZAMS' : 1,
        'MS' : 2,
        'RG' : 3,
        'AGB' : 4,
        'TPAGB' : 5,
        'WD' : 6
    }
    max_value = max(sort_order.values())
    #folder_name = string.split('/')[-2]
    folder_name = re.split('/|_',string)[-2]
    return sort_order.get(folder_name, max_value + 1)


def generate_file_models(path):
    find_history_files = glob.glob(path + "/**/history.data", recursive=True)
    sort_history_files = sorted(find_history_files,key=sorter)

    file_names = [
        a.split('/')[-2] for a in sort_history_files
    ]
    folder_paths = [
    '/'.join(name.split('/')[:-1]) for name in sort_history_files
    ]

    models = [1000,10476]

    file_models = {}
    for i in range(len(file_names)):
        file_models[file_names[i]] = [
            {
                'folder_path' : folder_paths[i],
                'name' : file_names[i],
                'models' : models,
            },
        ]
        
    return file_models


def generate_multiple_sim(paths):

    file_models = {}
    for path in paths:
        find_history_files = glob.glob(path + "/**/history.data", recursive=True)
        sort_history_files = sorted(find_history_files, key=sorter)

        file_names = [
            a.split('/')[-2] for a in sort_history_files
        ]
        folder_path = [
        '/'.join(name.split('/')[:-1]) for name in sort_history_files
        ]

        sim_name = path.split('/')[-1]

        models = [1000,10476]
        file_models[sim_name] = []

        for i in range(len(file_names)):
            file_models[sim_name].append({
                    'folder_path' : folder_path[i],
                    'name' : file_names[i],
                    'models' : models,
                },)
    return file_models
