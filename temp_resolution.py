import generate_file_models as gfm
import merge_history as mh
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



sim_path = '/Users/nunina/MESA/Simulations/ALL/temp_res/'
specific = ['1M1Z08m1t','1M1Z08m08t','1M1Z06m1t', '1M1Z06m08t']#,'1M1Z1.2','1M1Z1.4','1M1Z1.6','1M1Z1.8','1M1Z2']
#specific = ['1M1Z08','1M1Z1']

paths_list = [ sim_path+i for i in specific ]    
file_models = gfm.generate_multiple_sim(paths_list)
all_data = mh.merge_all_data(file_models)

fig = plt.figure(constrained_layout = True)
fig.suptitle('HR Diagram')
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
ax = fig.add_subplot(spec[:, :])
ax.invert_xaxis()


for folder_name, data in all_data.items():
    mh.resolution_hr(data,folder_name,ax)

ax.legend()

plt.show()

