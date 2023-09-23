import mesaPlot as mp


m = mp.MESA()
p=mp.plot()
m.log_fold='/Users/nunina/MESA/Simulations/ALL/1M1Z_kipp/LOGS_2'
m.loadHistory()
#p.plotHistory(m,xaxis='star_age',y1='log_cntr_T',y2='he_core_mass')
p.plotKip2(m,xaxis='star_age',show_mass_loc=True,age_lookback=True,age_log=True)