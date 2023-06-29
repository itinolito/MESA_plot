import merge_history as mh
import generate_file_models as gfm
import mesa_reader as mr


#--------------------FUNCTIONS--------------------#

def has_rg_radius(logR):
    return logR > 1.3

def has_large_lum(logL):
    return logL > 1

#--------------FIND PARTICULAR MODEL--------------#

def find_models_function(function,parameter,file_models):
    my_models = file_models.copy()
    for name, simulations in my_models.items():
        for file_model in simulations:
#            mesa_param_obj = mr.MesaLogDir(file_model['folder_path'])
#            file_model['models'] = mesa_param_obj.select_models(function, parameter).tolist()
            mesa_param_obj = mr.MesaData(file_model['folder_path']+'/history.data')
            file_model['models'] = mesa_param_obj.where(function, parameter).tolist()
    return my_models

def find_data_model(function,parameter,file_models,my_data):
    my_models = find_models_function(function,parameter,file_models)

    my_models_data = {}
    for name,stages in my_models.items():
        stage_data = mh.aggregate_data(stages)
        my_models_data[name] = stage_data

    found_info = {}
    for star_name, stages in my_models_data.items():
        found_info[star_name] = {}
        for folder_name,data in stages.items():
            found_info[star_name] = data[my_data]
    return found_info

#---------------------PROGRAM---------------------#

sim_folder = 'MS/3M1Z/RG'
local_sim = '/Users/nunina/MESA/Simulations/'

#file_models = gfm.generate_file_models(local_sim+sim_folder)

#print(find_models_function(has_rg_radius,'log_R',file_models))
#print(find_data_model(has_rg_radius,'log_R',file_models,'age'))

mesa_param_obj = mr.MesaData(local_sim+sim_folder+'/history.data')
data = mesa_param_obj.data('log_R')
for i in data:
    import ipdb; ipdb.set_trace()
    if data[i] > 1.0:
        print(data[i])
