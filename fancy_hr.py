import generate_file_models as gfm
import merge_history as mh
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from astropy import units as u
from astropy import constants as ct
from matplotlib.collections import LineCollection
import matplotlib.patheffects as pe

pi = np.pi
sigma = ct.sigma_sb.to('Lsun/(K4 Rsun2)')

#sim_path = ['/Users/nunina/MESA/Simulations/ALL/def/1M1Z_hr']
sim_path = ['/Volumes/NO NAME/Simulations/1M01Z/normal']

stages_separated = gfm.generate_file_models(sim_path[0])
each_stage = {}
for stages,info in stages_separated.items():
    stage_object = mh.get_file(stages_separated[stages][0]['folder_path'],stages_separated[stages][0]['models'])
    stage_data = mh.get_params(stage_object)
    each_stage[stages] = stage_data

file_models = gfm.generate_multiple_sim(sim_path)   
all_data = mh.merge_all_data(file_models)

fig = plt.figure(constrained_layout = True)
fig.suptitle('HR diagram of a $1M_\odot$, $0.1Z_\odot$ star')
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
ax = fig.add_subplot(spec[:, :])
ax.invert_xaxis()
ax.grid(False)


def hr_radius_lines(radius, logT):
    lum_list=[]
    for t in logT:
        temp = 10**t*u.K
        lum=4*pi*sigma*(temp**4)*(radius**2)/u.Lsun
        lum_list.append(np.log10(lum))
    return lum_list

def plot_radius(radius):
    logT=np.arange(3.3,5.2,0.05)
    label_x = min(logT)+0.8
    for r in radius:
        logL=(hr_radius_lines(r,logT))
        ax.plot(logT,logL,lw=0.5,alpha=0.5,color='gray',ls='dashed')
        p1 = ax.transData.transform_point((logT[0], logL[0]))
        p2 = ax.transData.transform_point((logT[1], logL[1]))
        dx = p2[0]-p1[0]
        dy = p2[1]-p1[1]
        angle = np.degrees(np.arctan2(dy, dx))
        label_x -= 0.07  # X-coordinate for the label for each radius
        label_y = np.log10(4*pi*sigma*((10**(label_x)*u.K)**4)*(r**2)/u.Lsun)
        radius_num=r/u.Rsun
        ax.text(label_x, label_y, f'${radius_num}R_\odot$', ha='right', va='bottom', fontsize="x-small", color='gray', alpha=0.5, rotation=-angle+7, rotation_mode='anchor', transform_rotates_text=True)

radius = [0.1*u.Rsun,0.3*u.Rsun,1*u.Rsun,3*u.Rsun,10*u.Rsun,30*u.Rsun,100*u.Rsun]

plot_radius(radius)

for folder_name, data in all_data.items():
    x = data['log_Teff']
    y = data['log_luminosity']
    f = data['h1']
    # This creates the points as an N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be (numlines) x (points per line) x 2 (for x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    # Create a continuous norm to map from data points to colors
    norm = plt.Normalize(min(f), max(f))
    lc = LineCollection(segments, cmap='viridis', norm=norm, linewidth=5)
    # Set the values used for colormapping
    lc.set_array(f)
    lc.set_linewidth(2)
    line = ax.add_collection(lc)
    fig.colorbar(line, ax=ax, label="Center H1")
    ax.plot(x,y, lw=0, label = "{stage}".format(stage=folder_name))#, marker='.', markevery=[0])        

zams=each_stage['MS']
x = zams['log_Teff'][0]
y = zams['log_luminosity'][0]
ax.plot(x,y, 'ro', markersize=3)
ax.annotate("ZAMS",xy=(x,y),xycoords='data',xytext=(-50,-20),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.2"))

rg=each_stage['RG']
x = rg['log_Teff'][0]
y = rg['log_luminosity'][0]
ax.plot(x,y, 'ro', markersize=3)
ax.annotate("RG",xy=(x,y),xycoords='data',xytext=(-50,-10),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.2"))

agb=each_stage['AGB']
x = agb['log_Teff'][0]
y = agb['log_luminosity'][0]
ax.plot(x,y, 'ro', markersize=3)
ax.annotate("AGB",xy=(x,y),xycoords='data',xytext=(-70,-20),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.2"))


tpagb=each_stage['TPAGB']
x = tpagb['log_Teff'][0]
y = tpagb['log_luminosity'][0]
ax.plot(x,y, 'ro', markersize=3)
ax.annotate("TPAGB",xy=(x,y),xycoords='data',xytext=(-70,-10),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.2"))

x = tpagb['log_Teff'][-1]
y = tpagb['log_luminosity'][-1]
ax.plot(x,y, 'ro', markersize=3)
ax.annotate("WDCS",xy=(x,y),xycoords='data',xytext=(30,-20),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.2"))

#
#for stage, data in each_stage.items():
#    x = data['log_Teff'][0]
#    y = data['log_luminosity'][0]
#    ax.plot(x,y, 'ro', markersize=3)
#    ax.annotate("{stage}".format(stage=stage),xy=(x,y),xycoords='data',xytext=(-50,-20),textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=-0.2"))
#
ax.set_ylabel("$\log_{\ 10}(L/L_\odot)$ ")
ax.set_xlabel("$\log_{10} T_{\\textit{eff}}$ ")

ax.set_ylim(top=4, bottom=-1.2)
ax.set_xlim(right=3.4, left=5.1)


#plt.savefig('/Users/nunina/MESA/fig/1M1Z_hr.png')
plt.show()
