import generate_file_models as gfm
import merge_history as mh
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



sim_path = '/Users/nunina/MESA/Simulations/ALL/1M1Z_kipp/'
file_models = gfm.generate_file_models(sim_path)
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

