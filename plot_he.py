import matplotlib.pyplot as plt
import merge_history as mh
import generate_file_models as gfm
import sys
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

sim_folder = '/Users/nunina/MESA/Simulations/ALL/def/'
folder=sim_folder+"2M01Z/normal/"
#folder = sim_folder+'1M01Z/025he/normal'#sys.argv[1]
to_plot = gfm.generate_file_models(folder)


fig = plt.figure(constrained_layout = True)
fig.suptitle('He')
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
ax1 = fig.add_subplot(spec[0, 0])


for name, simulations in to_plot.items():
    simulations_data = mh.aggregate_data(simulations)

    for folder_name, models_data in simulations_data.items():
        for model,data in models_data.items():
            mh.he_time(data,name,ax1)

mh.he_time(to_plot)
#plt.savefig(folder+'.png')
plt.show()


