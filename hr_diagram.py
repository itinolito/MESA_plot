import generate_file_models as gfm
import merge_history as mh
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from astropy import units as u
from astropy import constants as ct

pi = np.pi
sigma = ct.sigma_sb.to('Lsun/(K4 Rsun2)')

sim_path = '/Users/nunina/MESA/Simulations/ALL/spatial_res/'
specific = ['1M1Z2','1M1Z06','1M1Z08']
#specific = ['1M1Z04','1M1Z06','1M1Z08','1M1Z1','1M1Z1.2','1M1Z1.4','1M1Z1.6','1M1Z1.8','1M1Z2']

#specific = ['1M1Z_default', '1M1Z_default_res']#,'1M1Z/normal','1.5M1Z/normal','2M1Z/normal','3M1Z/normal']

paths_list = [ sim_path+i for i in specific ] 
paths_list.append('/Users/nunina/MESA/Simulations/ALL/1M1Z_default_res')
#file_models = gfm.generate_file_models(paths_list[0])   
file_models = gfm.generate_multiple_sim(paths_list)
all_data = mh.merge_all_data(file_models)

fig = plt.figure(constrained_layout = True)
fig.suptitle('HR Diagram')
spec = gridspec.GridSpec(ncols=1, nrows=1, figure=fig)
ax = fig.add_subplot(spec[:, :])
ax.invert_xaxis()

def hr_radius_lines(radius, logT):
    lum_list=[]
    for t in logT:
        temp = 10**t*u.K
        lum=4*pi*sigma*(temp**4)*(radius**2)/u.Lsun
        lum_list.append(np.log10(lum))
    return lum_list

for folder_name, data in all_data.items():
    mh.resolution_hr(data,folder_name,ax)

radius = [0.1*u.Rsun,0.3*u.Rsun,1*u.Rsun,3*u.Rsun,10*u.Rsun,30*u.Rsun,100*u.Rsun]
logT=np.arange(3.3,5.2,0.05)
#ax.plot(data['log_Teff'],data['log_luminosity'], lw=1, label = "{stage}".format(stage=name), marker='.', markevery=[0])        
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
ax.set_ylim(top=4, bottom=-1.2)
ax.set_xlim(right=3.4, left=5.1)

ax.legend()

plt.show()

