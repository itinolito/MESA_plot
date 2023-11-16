import generate_file_models as gfm
import merge_history as mh
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


sim_path = '/Users/nunina/MESA/Simulations/ALL/temp_res/'
specific = ['1M1Z08m1t','1M1Z08m08t','1M1Z06m1t', '1M1Z06m08t', '1M1Z06m06t']#,'1M1Z1.2','1M1Z1.4','1M1Z1.6','1M1Z1.8','1M1Z2']
#specific = ['1M1Z08','1M1Z1']

paths_list = [ sim_path+i for i in specific ]    
file_models = gfm.generate_multiple_sim(paths_list)
all_data = mh.merge_all_data(file_models)

fig = plt.figure(constrained_layout = True)
fig.suptitle('Resolution tests for a $1M_\odot$, $1Z_\odot$ star')
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
ax = fig.add_subplot(spec[:, :])
ax.invert_xaxis()


axins1 = zoomed_inset_axes(ax, zoom = 2.5, loc=10)
axins1.set(xticks=[],yticks=[])




# SPECIFY THE LIMITS
x1, x2, y1, y2 = 3.62, 3.46, 2.6, 3.67 
axins1.set_xlim(x1, x2)
axins1.set_ylim(y1, y2)

for folder_name, data in all_data.items():
    mh.resolution_hr(data,folder_name,ax)
    mh.resolution_hr(data, folder_name,axins1)

axins1.set_ylabel("")
axins1.set_xlabel("")
mark_inset(ax, axins1, loc1=1, loc2=4, fc="none", ec="0.5")
leg = ax.legend()

for legobj in leg.legendHandles:
    legobj.set_linewidth(2.0)


plt.savefig("/Users/nunina/MESA/fig/res_test.png")
