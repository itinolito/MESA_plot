from lzma import MODE_NORMAL
import mesa_reader as mr
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from astropy import units as u
from astropy import constants as ct

plt.style.use('/Users/nunina/MESA/Simulations/MESA_plot/aesthetic.mplstyle')

history=True

def get_file(file,model):
    if history:
        history_data = file + '/history.data'
        p=mr.MesaData(history_data)
        return p
    else:
        h=mr.MesaLogDir(file)
        p=h.profile_data(model_number=model)
        return p

def get_params(p):
    params = {}
    if history:
    #   Star parameters FOR HISTORY
        params = {
            'log_radius': p.log_R,
            'mass': p.star_mass,
            'age': p.star_age,
            'log_density': p.log_cntr_Rho,
            'pp': p.pp,
            'cno': p.cno,
            'trialpha': p.tri_alpha,
            'he_core_mass': p.he_core_mass,
            'co_core_mass': p.co_core_mass,
            'log_temp_eff': p.log_Teff,
            'log_luminosity': p.log_L,
            'log_center_T': p.log_cntr_T,
            'log_P': p.log_cntr_P,
            'h1': p.center_h1,
            'he4': p.center_he4,
            'c12': p.center_c12,
            'o16': p.center_o16,
            'mass_h': p.total_mass_h1,
            'mass_he': p.total_mass_he4,
            'log_Teff' : p.log_Teff,
            'mass_conv_core' : p.mass_conv_core,
            'conv_mx1_top' : p.conv_mx1_top,
            'conv_mx1_bot' : p.conv_mx1_bot,
            'conv_mx2_top' : p.conv_mx2_top,
            'conv_mx2_bot' : p.conv_mx2_bot,
            'mx1_top' : p.mx1_top,
            'mx1_bot' : p.mx1_bot,
            'mx2_top' : p.mx2_top,
            'mx2_bot' : p.mx2_bot
        }
    else:
    #   Star parameters FOR PARTICULAR PROFILE OR MODEL
        params = {
            'log_radius' : p.logR,
            'mass' : p.mass,
            'age' : p.star_age,
            'log_density' : p.logRho,
            'log_temp' : p.logT,
            #'luminosity' : p.luminosity,
            'hydrogen' : p.x_mass_fraction_H,
            'helium' : p.y_mass_fraction_He,
            'pp' : p.pp,
            'cno' : p.cno,
            'trialpha' : p.tri_alpha,
            #'h1' : p.h1,
            #'he3' : p.he3,
            #'he4' : p.he4,
            #'c12' : p.c12,
            #'n14' : p.n14,
            #'o16' : p.o16,
            #'ne20' : p.ne20,
            #'mg24' : p.mg24,
        }
    #    fe56=p.fe56
    #    ni58=p.ni58 
    
    params['radius'] = 10**params['log_radius']
    params['density'] = 10**params['log_density']
    
    return params

def aggregate_data(stages):

    all_parameters = {}
    if history:
        for stage in stages:
            folder_name = stage['name']
            model = stage['models']
            mesa_param_obj = get_file(stage['folder_path'],model)
            all_parameters[folder_name] = get_params(mesa_param_obj)

    else:    
        for stage in stages:
            folder_name = stage['name']
            print(stage['folder_path'])
            all_parameters[folder_name] = {}
            for model in stage['models']:
                mesa_param_obj = get_file(stage['folder_path'],model)
                all_parameters[folder_name][model] = get_params(mesa_param_obj)

    return all_parameters

def merge_history(data_to_merge):
    merged_data = {}
    for name, folder_data in data_to_merge.items():
        for parameter, value_list in folder_data.items():
            parameter_list = merged_data.get(parameter, [])
            parameter_list.extend(value_list)
            merged_data[parameter] = parameter_list

    return merged_data

def merge_all_data(file_models):
    merged_file_models = {}
    for name, simulations in file_models.items():
        stage_data = aggregate_data(simulations)
        merged_file_models[name] = merge_history(stage_data)

    return merged_file_models


#-------------------------------------------------#
#----------------- HISTORY PLOTS -----------------#
#-------------------------------------------------#

def radius_time(data, name, plt):
    plt.set_yscale("log")
    plt.plot(data['age'],data['radius'], label = "{stage}".format(stage=name), zorder=0)
    plt.fill_between(data['age'],data['radius'], 0, alpha=.1)
    #plt.set_ylabel("$r/R_\odot$")

def beautiful_radius_time(data, name, plt):
    plt.set_yscale("log")
    x = data['age']
    y = data['radius']
    plt.plot(x,y, label = "{stage}".format(stage=name))
    plt.set_ylabel("$r/R_\odot$")
    plt.fill_between(x,y,alpha=.1)


def temp_time(data, name, plt):
    plt.plot(data['age'],data['log_Teff'], label = "{stage}".format(stage=name))
    plt.set_ylabel("$\log_{10} T_{\\textit{eff}}$")

def elements_time(data, name, plt):
#    plt.xscale("log")
    plt.plot(data['age'],data['h1'], label="h1 {stage}".format(stage=name))
    plt.plot(data['age'],data['he4'], label="he4 {stage}".format(stage=name))
    plt.plot(data['age'],data['c12'], label="c12 {stage}".format(stage=name))
    plt.plot(data['age'],data['o16'], label="o16 {stage}".format(stage=name))
    plt.set_ylabel("Abundances")
    
def lum_time(data, name, plt):
    plt.plot(data['age'],data['log_luminosity'], label = "{stage}".format(stage=name))
    plt.set_ylabel("$\log_{\ 10}(L/L_\odot)$ ")

def lum_temp_hr(data, name, plt):
    plt.plot(data['log_Teff'],data['log_luminosity'], label = "{stage}".format(stage=name), lw=0.5, zorder=0)#, marker='.', markevery=indices)
    
    plt.invert_xaxis()

def nuc_time(data, name, plt):
    plt.set_yscale("log")
    plt.plot(data['age'],data['pp'], label="$p-p$ {stage}".format(stage=name))
    plt.plot(data['age'],data['cno'], label="$CNO$ {stage}".format(stage=name))
    plt.plot(data['age'],data['trialpha'], label="$3-alpha$ {stage}".format(stage=name))
    plt.set_ylabel("$\log_{\ 10} (L/L_{\odot})$")
    
def resolution_hr(data, name, plt):
    x = data['log_Teff']
    y = data['log_luminosity']
    plt.plot(x,y, lw=0.5, label = "{stage}".format(stage=name))#, marker='.', markevery=[0])        
    if name == "MS":
        plt.plot(x[0],y[0], 'yo')
    plt.grid(False)
    plt.set_ylabel("$\log_{\ 10}(L/L_\odot)$ ")
    plt.set_xlabel("$\log_{10} T_{\\textit{eff}}$ ")

def beautiful_hr(data, name, plt):
    x = data['log_Teff']
    y = data['log_luminosity']
    f = data['h1']

    # This creates the points as an N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be (numlines) x (points per line) x 2 (for x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)


    # Create a continuous norm to map from data points to colors
    norm = plt.Normalize(f.min(), f.max())
    lc = LineCollection(segments, cmap='viridis', norm=norm)
    # Set the values used for colormapping
    lc.set_array(f)
    lc.set_linewidth(2)
    line = plt.add_collection(lc)
    plt.colorbar(line, ax=plt)

    plt.plot(x,y, lw=0.5, label = "{stage}".format(stage=name))#, marker='.', markevery=[0])        
    if name == "MS":
        plt.plot(x[0],y[0], 'yo')
    plt.grid(False)
    plt.set_ylabel("$\log_{\ 10}(L/L_\odot)$ ")
    plt.set_xlabel("$\log_{10} T_{\\textit{eff}}$ ")

def he_time(data, name, plt):
    plt.plot(data['age'],data['he_core_mass'], label = "{stage}".format(stage=name))#, marker='.', markevery=indices)
    plt.set_ylabel("$he_core$ ")
    plt.set_xlabel("age ")

#-------------------------------------------------#
#----------------- PROFILE PLOTS -----------------#
#-------------------------------------------------#

#--------------- PROFILE / RADIUS ----------------#

def density_radius(data,model,plt):
    plt.set_title("Density profile of a $1M_\odot$ ZAMS red giant")
    plt.xscale("log")
    plt.plot(data['radius'],data['log_density'], label="model {}".format(model))
    plt.set_xlabel("$r/R_\odot$")
    plt.set_ylabel("$\log_{\ 10} \; \left(ρ/ρ_\odot\\right)$")
    
def elements_radius(data,model,plt):
    plt.set_title("Elements for model {}".format(model))
    plt.xscale("log")
    plt.plot(data['radius'],data['h1'], label="h1")
    plt.plot(data['radius'],data['he3'], label="he3")
    plt.plot(data['radius'],data['he4'], label="he4")
    plt.plot(data['radius'],data['c12'], label="c12")
    plt.plot(data['radius'],data['n14'], label="n14")
    plt.plot(data['radius'],data['o16'], label="o16")
    plt.plot(data['radius'],data['ne20'], label="ne20")
    plt.plot(data['radius'],data['mg24'], label="mg24")
#    plt.plot(data['radius'],fe56, label="fe56")
#    plt.plot(data['radius'],ni58, label="ni58")
    plt.set_xlabel("$r/R_\odot$")
    plt.set_ylabel("Abundances")

def tidal_radius_radius(data,model,plt):
    plt.set_title("$\\frac{ r}{M^{1/3}(r)}$ of a $1M_\odot$ ZAMS red giant")
    plt.xscale("log")
    plt.yscale("log")
    y=data['radius']/(data['mass'])**(1/3)
    plt.plot(data['radius'],y, label="model {}".format(model))
    plt.set_xlabel("$r/R_\odot$")
    plt.set_ylabel("$\\frac{ r}{M^{1/3}(r)}$")

def tidal_radius_mass_fraction(data,plt, bh_mass, name):
    #plt.set_xscale("log")
    plt.set_yscale("log")
    total_mass = data["mass"][0]
    x = 1 - data["mass"]/total_mass
    tr_rsun = (data['radius']*(bh_mass/data['mass'])**(1/3))*u.R_sun
    
    mass = (bh_mass*u.M_sun).to('kg')
    
    r_g = ct.G*mass/(ct.c)**2

    y = (tr_rsun.to('m'))/r_g

    
    plt.plot(x,y, label="{}".format(name))
    plt.set_xlim([-0.049,1.049])
    plt.legend(fontsize="x-small", loc="upper right")


#----------------- PROFILE / MASS ----------------#
def radius_mass(data,model,name,plt):
    plt.plot(data['mass'],data['radius'], label=name, lw=0.8)
    plt.set_ylabel("$r/R_\odot$")

def density_mass(data,model,name,plt):
#    plt.set_title("Density profile of a $1M_\odot$ ZAMS red giant")
    plt.plot(data['mass'],data['log_density'], label=name, lw=0.8)
    plt.set_ylabel("$\log_{\ 10} \; \left(\\rho/\\rho_\odot\\right)$")
     
def elements_mass(data,model,name,plt):
#    plt.set_title("Elements for model {}".format(model))
    plt.plot(data['mass'],data['h1'], label="h1 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['he3'], label="he3 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['he4'], label="he4 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['c12'], label="c12 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['n14'], label="n14 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['o16'], label="o16 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['ne20'], label="ne20 model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['mg24'], label="mg24 model {model_num} of {sim}".format(model_num=model, sim=name))
#    plt.plot(radius,fe56, label="fe56")
#    plt.plot(radius,ni58, label="ni58")
    plt.set_ylabel("Abundances")
    plt.legend()
    
def temp_density(data,model,name,plt):
    plt.set_title("Temperature-Density profile")
    plt.xscale("log")
    plt.plot(data['log_density'],data['log_temp'], label="model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_xlabel("$\log_{\ 10} \\rho$")
    plt.set_ylabel("$\log_{\ 10} T$")

def temp_mass(data,model,name,plt):
#    plt.set_title("Temperature-mass profile")
    plt.plot(data['mass'],data['log_temp'], label="model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_ylabel("$\log_{\ 10} T$")
    
def tidal_radius_mass(data,model,name,plt):
#    plt.set_title("$\\frac{ r}{M^{1/3}(r)}$ of a $1M_\odot$ ZAMS red giant")
#    plt.xscale("log")
#    plt.yscale("log")
    y=data['radius']/(data['mass'])**(1/3)
    plt.plot(data['mass'],y, label=name)
    plt.set_ylabel("$r/m^{1/3}$")

def nuc_energy(data,model,name,plt):
    plt.plot(data['mass'],data['pp'], label="pp model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['cno'], label="cno model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.plot(data['mass'],data['trialpha'], label="$\\alpha$ model {model_num} of {sim}".format(model_num=model, sim=name))
    plt.set_ylabel("$\epsilon$")


#-------------------------------------------------#
#-------------PLOT A BUNCH OF STUFF---------------#
#-------------------------------------------------#

def plot_profile_mass(file_models,labeldata):
    fig = plt.figure()
    fig.suptitle('Profiles')
    #spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2, sharex=ax1)

    #ax1 = fig.add_subplot(spec[0, :])
    #ax2 = fig.add_subplot(spec[1, :])
    #ax3 = fig.add_subplot(spec[2,:])

    for name, simulations in file_models.items():
        simulations_data = aggregate_data(simulations)

        for folder_name, models_data in simulations_data.items():
            all_labels = alt_label_parser(folder_name,labeldata)
            my_label = all_labels[0]
            for model,data in models_data.items():
                #import ipdb; ipdb.set_trace()
                density_mass(data,model,my_label,ax1)
                radius_mass(data,model,my_label,ax2)
    handles, labels = ax1.get_legend_handles_labels()
    leg = fig.legend(handles, labels, fontsize="x-small", ncol = 4, loc="lower center", bbox_to_anchor=(0.5,0))
    fig.subplots_adjust(bottom=0.2)
    ax2.set_xlabel('$m/M_\odot$')
    fig.suptitle('Profiles for '+all_labels[1])
    for legobj in leg.legendHandles:
        legobj.set_linewidth(1.5)


def plot_time(file_models):
    fig = plt.figure(constrained_layout = True)
    fig.suptitle('Evolution with time')
    spec = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
    ax1 = fig.add_subplot(spec[0, :])
    ax2 = fig.add_subplot(spec[1, 1:])
    ax3 = fig.add_subplot(spec[1:,0])
    ax3.invert_xaxis()
    ax4 = fig.add_subplot(spec[-1,1:])
#    ax1.set_xlim(1.217e10,1.236e10)
#    ax2.set_xlim(1.217e10,1.236e10)
#    ax4.set_xlim(1.217e10,1.236e10)
    ax1.set_xlim(1.204e10,1.236e10)
    ax2.set_xlim(1.204e10,1.236e10)
    ax4.set_xlim(1.204e10,1.236e10)
    
    all_data = merge_all_data(file_models)

    for folder_name,data in all_data.items():
        radius_time(data,folder_name,ax1)
        lum_time(data,folder_name,ax2)
        #nuc_time(data,folder_name,ax4)
        temp_time(data,folder_name,ax4)
        lum_temp_hr(data,folder_name,ax3)
    ax1.legend(fontsize="x-small")
    ax2.legend(fontsize="x-small")
    ax3.legend(fontsize="x-small")
    ax4.legend(fontsize="x-small")

def all_time(file_models):
    fig = plt.figure(constrained_layout = True)
    fig.suptitle('Evolution with time')
    spec = gridspec.GridSpec(ncols=3, nrows=2, figure=fig)
    ax1 = fig.add_subplot(spec[0, 1:])
    ax2 = fig.add_subplot(spec[1, 1:])
    ax3 = fig.add_subplot(spec[0:,0])
    ax3.invert_xaxis()
    
    all_data = merge_all_data(file_models)

    for folder_name,data in all_data.items():
        radius_time(data,folder_name,ax1)
        temp_time(data,folder_name,ax2)
        lum_temp_hr(data,folder_name,ax3)
    ax1.legend(fontsize="x-small")
    ax2.legend(fontsize="x-small")
    ax3.legend(fontsize="x-small")

    #ax1.set_xlim(1.2e10,1.25e10)
    #ax2.set_xlim(1.2e10,1.25e10)
    #ax4.set_xlim(1.2e10,1.25e10)

def all_time_reduced(file_models, strip_model):
    fig = plt.figure(constrained_layout = True)
    fig.suptitle('Evolution with time')
    spec = gridspec.GridSpec(ncols=3, nrows=2, figure=fig)
    ax1 = fig.add_subplot(spec[0, 1:])
    ax2 = fig.add_subplot(spec[1, 1:])
    ax3 = fig.add_subplot(spec[0:,0])
    ax3.invert_xaxis()
    
    all_data = merge_all_data(file_models)

    for folder_name,data in all_data.items():
        radius_time(data,folder_name,ax1)
        #lum_time(data,folder_name,ax2)
        temp_time(data,folder_name,ax2)
        lum_temp_hr(data,folder_name,ax3)
        
    stripped = merge_all_data(strip_model)    
    data_strip=stripped['strip']
    temp_strip = data_strip['log_Teff'][-1]
    lum_strip = data_strip['log_luminosity'][-1]
    rad_strip = data_strip['radius'][-1]
    time_strip = data_strip['age'][-1]
    ax1.plot(time_strip,rad_strip, 'ro', markersize=3)
    ax2.plot(time_strip,temp_strip, 'ro', markersize=3)
    ax3.plot(temp_strip,lum_strip, 'ro', markersize=3)
    ax1.legend(fontsize="x-small")
    ax2.legend(fontsize="x-small")
    ax3.legend(fontsize="x-small")

    #ax1.set_xlim(1.2e10,1.25e10)
    #ax2.set_xlim(1.2e10,1.25e10)
    #ax4.set_xlim(1.2e10,1.25e10)

def one_profile_plot(file_models, profile):
    # Plot one profile from a dictionary that contains folder_path, name and list of models.
    folder = file_models['folder_path']
    models = file_models['models']
    name = file_models['name']
    fig, ax = plt.subplots(1)
    ax.minorticks_on()
    for model in models:
        p = get_file(folder,model)
        data = get_params(p)
        profile(data,model,name,ax)
#    for title,mass in stripping_mass_1M_10R.items():
#        ax.axvline(mass, ls="--", c="indianred", lw="1", )
#        ax.annotate(title, xy=(mass+0.01,8), rotation=90)
#    ax.axvspan(stripping_mass_1M_10R['Retain 0.2'],stripping_mass_1M_10R['Retain 0.3'], color="indianred", alpha=0.2,lw=0)
    ax.set_xlabel("$m/M_\odot$")
    ax.set_title("Tidal radius profile for a $1M_\odot$ pre-ZAMS RG at time $R=10R_\odot$")

#----

def label_parser(string, data):
    if "normal" in string:
        pieces = string.split("/")
        row_name = pieces[1]+'/050he/normal'
        row_data = data[data["Path"] == row_name]
    else:
        row_data = data[data["Path"] == string]
    #import ipdb; ipdb.set_trace()
    total_mass = float(row_data['Total mass'])
    core_mass = float(row_data['Core mass'])
    progenitor_mass = float(row_data['Progenitor mass'])
    he = float(row_data['%He at stripping'])
    dot_label= "{:.2f}m{:.2f}c{:.1f}p{:.2f}he".format(total_mass,core_mass,progenitor_mass,he)
    label = "".join(dot_label.split("."))
    return label

def alt_label_parser(string, data):
    if "normal" in string:
        pieces = string.split("/")
        row_name = pieces[1]+'/050he/normal'
        row_data = data[data["Path"] == row_name]
    else:
        row_data = data[data["Path"] == string]
    #import ipdb; ipdb.set_trace()
    total_mass = float(row_data['Total mass'])
    core_mass = float(row_data['Core mass'])
    progenitor_mass = float(row_data['Progenitor mass'])
    he = float(row_data['%He at stripping'])
    dot_label= "{:.2f}m{:.2f}c".format(total_mass,core_mass)
    label = "".join(dot_label.split("."))
    common_label = "{:.1f}$M_\odot$ stripped at {:.2f} He fraction".format(progenitor_mass,he)
    return label, common_label