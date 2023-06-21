import pandas as pd
import os
import glob

def generate_file_models(path):
    find_history_files = glob.glob(path + "/**/history.data", recursive=True)

    file_names = [
        a.split('/')[-2] for a in find_history_files
    ]
    folder_paths = [
    '/'.join(name.split('/')[:-1]) for name in find_history_files
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
