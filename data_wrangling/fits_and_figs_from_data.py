import numpy as np
from read_data import *
from fits_and_plots import *

##############################################################################################
# plot winter wheat yield vs winter wheat biomass in years 2015-2017
##############################################################################################

# divide by 0.75 to change into x/m^2

wh_bio_15 = np.array(list(df_am_2015_bi_wh["bio.wh.g/m2"])+list(df_ot_2015_bi_wh["bio.wh.g/m2"])+list(df_ro_2015_bi_wh["bio.wh.g/m2"]))/0.75

wh_bio_16 = np.array(list(df_am_2016_bi_wh["bio.wh.g/m2"])+list(df_ot_2016_bi_wh["bio.wh.g/m2"])+list(df_ro_2016_bi_wh["bio.wh.g/m2"]))/0.75

wh_bio_17 = np.array(list(df_am_2017_bi_wh["bio.wh.g/m2"])+list(df_ot_2017_bi_wh["bio.wh.g/m2"])+list(df_ro_2017_bi_wh["bio.wh.g/m2"]))/0.75

wh_yd_15 = np.array(list(df_am_2015_bi_wh["yield.wh.g/m2"])+list(df_ot_2015_bi_wh["yield.wh.g/m2"])+list(df_ro_2015_bi_wh["yield.wh.g/m2"]))/0.75

wh_yd_16 = np.array(list(df_am_2016_bi_wh["yield.wh.g/m2"])+list(df_ot_2016_bi_wh["yield.wh.g/m2"])+list(df_ro_2016_bi_wh["yield.wh.g/m2"]))/0.75

wh_yd_17 = np.array(list(df_am_2017_bi_wh["yield.wh.g/m2"])+list(df_ot_2017_bi_wh["yield.wh.g/m2"])+list(df_ro_2017_bi_wh["yield.wh.g/m2"]))/0.75

xpts = np.concatenate([wh_bio_15,wh_bio_16,wh_bio_17])
ypts = np.concatenate([wh_yd_15,wh_yd_16,wh_yd_17])
bool_x = xpts > 0
xpts = xpts[bool_x]
ypts = ypts[bool_x]

x = np.arange(0,4000,1)
IC = np.array([1,-1])
curve = get_curve(xpts,ypts,lin_curve,IC,x)

plot_data([wh_bio_15,wh_bio_16,wh_bio_17],[wh_yd_15,wh_yd_16,wh_yd_17],more_than_one_pts=True,legend=["2015","2016","2017"],x=x,curve=curve,xlabel="winter wheat biomass",ylabel="winter wheat yield",title="",savefile="wh_yieldvsbio_pooled_15-17.pdf",color=["blue","red","black"],show=False)


##############################################################################################
# plot winter wheat biomass vs number of plants in years 2016-2017 (no plant # data for 2015)
##############################################################################################

wh_pts_mo_16_17 = np.array(list(df_am_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_am_2017_mo_wh["springdensity.wh.plants/m2"])+ list(df_ot_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_ot_2017_mo_wh["springdensity.wh.plants/m2"]) + list(df_ro_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_ro_2017_mo_wh["springdensity.wh.plants/m2"]))/0.75

wh_bio_mo_16_17 = np.array(list(df_am_2016_mo_wh["bio.wh.g/m2"])+list(df_am_2017_mo_wh["bio.wh.g/m2"])+ list(df_ot_2016_mo_wh["bio.wh.g/m2"])+list(df_ot_2017_mo_wh["bio.wh.g/m2"]) + list(df_ro_2016_mo_wh["bio.wh.g/m2"])+list(df_ro_2017_mo_wh["bio.wh.g/m2"]))/0.75

plot_data(wh_pts_mo_16_17,wh_bio_mo_16_17,xlabel="winter wheat plants per m$^2$",ylabel="winter wheat biomass",
          title="",
          savefile="wh_mo_biovspts_pooled_16-17.pdf",show=False)

###########
wh_pts_bi_16_17 = np.array(list(df_am_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_am_2017_bi_wh["springdensity.wh.plants/m2"])+ list(df_ot_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_ot_2017_bi_wh["springdensity.wh.plants/m2"]) + list(df_ro_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_ro_2017_bi_wh["springdensity.wh.plants/m2"]))/0.75

wh_bio_bi_16_17 = np.array(list(df_am_2016_bi_wh["bio.wh.g/m2"])+list(df_am_2017_bi_wh["bio.wh.g/m2"])+ list(
    df_ot_2016_bi_wh["bio.wh.g/m2"])+list(df_ot_2017_bi_wh["bio.wh.g/m2"]) + list(df_ro_2016_bi_wh["bio.wh.g/m2"])+list(df_ro_2017_bi_wh["bio.wh.g/m2"]))/0.75

plot_data(wh_pts_bi_16_17,wh_bio_bi_16_17,xlabel="winter wheat plants per m$^2$",ylabel="winter wheat biomass",
          title="",
          savefile="wh_bi_biovspts_pooled_16-17.pdf",show=False)

#############
bool_mo = wh_pts_mo_16_17>0
bool_bi = wh_pts_bi_16_17>0
wh_pts_mo = wh_pts_mo_16_17[bool_mo]
wh_pts_bi = wh_pts_bi_16_17[bool_bi]
wh_bio_mo = wh_bio_mo_16_17[bool_mo]
wh_bio_bi = wh_bio_bi_16_17[bool_bi]

x = np.arange(0,350,1)
IC = np.array([1,-1])

curve_mo = get_curve(wh_pts_mo,wh_bio_mo,lin_curve,IC,x)
curve_bi = get_curve(wh_pts_bi,wh_bio_bi,lin_curve,IC,x)

# curve_mo = get_curve(wh_pts_mo/0.75,wh_bio_mo/0.75,log_curve,IC,x)
# curve_bi = get_curve(wh_pts_bi/0.75,wh_bio_bi/0.75,log_curve,IC,x)

# IC = np.array([1,2,1])
# curve_mo = get_curve(wh_pts_mo/0.75,wh_bio_mo/0.75,hill_curve,IC,x)
# curve_bi = get_curve(wh_pts_bi/0.75,wh_bio_bi/0.75,hill_curve,IC,x)


plot_data([wh_pts_mo_16_17,wh_pts_bi_16_17],[wh_bio_mo_16_17,wh_bio_bi_16_17],more_than_one_pts=True,legend=["mono","bi"],more_than_one_curve=True,x=[x,x],curve=[curve_mo,curve_bi],xlabel="winter wheat plants per m$^2$",ylabel="winter wheat biomass",title="",savefile="wh_bimo_biovspts_pooled_16-17.pdf",color=["blue","red"],ylim=[-125,3900],show=False)


####################################################################
# plot B. tectorum biomass vs # of B. tectorum plants years 2016-2017
####################################################################

cg_bio = np.array(list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi_cg["bio.cg.g/m2"]) + list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi_cg["bio.cg.g/m2"]))/0.75

cg_pts = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi_cg["springdensity.cg.plants/m2"]) + list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi_cg["springdensity.cg.plants/m2"]) + list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi_cg["springdensity.cg.plants/m2"]))/0.75

x = np.arange(0,1200,1)
IC = np.array([1,-1])
curve = get_curve(cg_pts,cg_bio,lin_curve,IC,x)
slope = fit(cg_pts,cg_bio,lin_curve,IC)[0]
print("Biomass to number plants slope {}".format(slope))

plot_data(cg_pts,cg_bio,x=x,curve=curve,xlabel="B. tectorum plants per m$^2$",ylabel="B. tectorum biomass",color="red",ylim=[-125,3900],title="",savefile="cg_bi_biovspts_pooled_16-17.pdf",show=False)


##################################################################
# plot winter wheat yield vs B. tectorum biomass by climate, pooled years
##################################################################
yield_scale = np.mean(df_am_2015_bi_wh["yield.wh.g/m2"])
ylim = [0,2.2]

cg_am = np.array(list(df_am_2015_bi_cg["bio.cg.g/m2"])+list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi_cg["bio.cg.g/m2"]))/0.75
yd_am = np.array(list(df_am_2015_bi_wh["yield.wh.g/m2"])+ list(df_am_2016_bi_wh["yield.wh.g/m2"])+list(df_am_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale

bool_yd = yd_am > 0
cg_am=cg_am[bool_yd]
yd_am=yd_am[bool_yd]

x = np.arange(0, 1800, 1)
IC = np.array([1,-1])
curve_am = get_curve(cg_am,yd_am,exp_curve,IC,x)
p_am = fit(cg_am,yd_am,exp_curve,IC)
print("B. tectorum biomass to yield exp parameters (ambient) {}".format(p_am))

plot_data_with_textbox(cg_am,yd_am,p_am,"exp",x=x,curve=curve_am,color="blue",xlabel="B. tectorum biomass",ylabel="winter wheat yield",ylim=ylim,title="",savefile="yieldvsbio_ambient_15-17.pdf",show=False)

###########
cg_ot = np.array(list(df_ot_2015_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi_cg["bio.cg.g/m2"]))/0.75
yd_ot = np.array(list(df_ot_2015_bi_wh["yield.wh.g/m2"])+ list(df_ot_2016_bi_wh["yield.wh.g/m2"])+list(df_ot_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale

bool_yd = yd_ot > 0
cg_ot=cg_ot[bool_yd]
yd_ot=yd_ot[bool_yd]

x = np.arange(0, 1800, 1)
IC = np.array([1,-1])
curve_ot = get_curve(cg_ot,yd_ot,exp_curve,IC,x)
p_ot = fit(cg_ot,yd_ot,exp_curve,IC)
print("B. tectorum biomass to yield exp parameters (hot) {}".format(p_ot))

plot_data_with_textbox(cg_ot,yd_ot,p_ot,"exp",x=x,curve=curve_ot,color="red",xlabel="B. tectorum biomass",ylabel="winter wheat yield",ylim=ylim,title="",savefile="yieldvsbio_hot_15-17.pdf",show=False)

############
cg_ro = np.array(list(df_ro_2015_bi_cg["bio.cg.g/m2"])+list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi_cg["bio.cg.g/m2"]))/0.75
yd_ro = np.array(list(df_ro_2015_bi_wh["yield.wh.g/m2"])+ list(df_ro_2016_bi_wh["yield.wh.g/m2"])+list(df_ro_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale

bool_yd = yd_ro > 0
cg_ro=cg_ro[bool_yd]
yd_ro=yd_ro[bool_yd]

x = np.arange(0, 1800, 1)
IC = np.array([1,-1])
curve_ro = get_curve(cg_ro,yd_ro,exp_curve,IC,x)
p_ro = fit(cg_ro,yd_ro,exp_curve,IC)
print("B. tectorum biomass to yield exp parameters (hot/dry) {}".format(p_ro))

plot_data_with_textbox(cg_ro,yd_ro,p_ro,"exp",x=x,curve=curve_ro,color="black",xlabel="B. tectorum biomass",ylabel="winter wheat yield",ylim=ylim,title="",savefile="yieldvsbio_hotdry_15-17.pdf",show=False)

# ###############
# plot_data([cg_am,cg_ot,cg_ro],[yd_am,yd_ot,yd_ro],more_than_one_pts=True,legend=["ambient","hot","hot/dry"],more_than_one_curve=True,x=[x,x,x],curve=[curve_am,curve_ot,curve_ro],xlabel="B. tectorum biomass",
#           ylabel="winter wheat yield",
#           title="",savefile="yieldvsbio_allclimates_15-17.pdf",
#           color=["blue","red","black"],show=False)

###############
plot_curves_only([x,x,x],[curve_am,curve_ot,curve_ro],xlabel="B. tectorum biomass",
          ylabel="winter wheat yield",legend=["ambient","hot","hot/dry"],more_than_one_curve=True,
          title="",savefile="yieldvsbio_allclimates_15-17.pdf",
          color=["blue","red","black"],show=False)

###################################################
# combined linear and exp fits
###################################################
ylim = [0,1.5]

cg_pts_am_16_17 = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi_cg["springdensity.cg.plants/m2"]))/0.75
cg_pts_ot_16_17 = np.array(list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi_cg[
                                                                                        "springdensity.cg.plants/m2"]))/0.75
cg_pts_ro_16_17 = np.array(list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi_cg[
                                                                                        "springdensity.cg.plants/m2"]))/0.75
yd_am_16_17 = np.array(list(df_am_2016_bi_wh["yield.wh.g/m2"])+list(df_am_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale
yd_ot_16_17 = np.array(list(df_ot_2016_bi_wh["yield.wh.g/m2"])+list(df_ot_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale
yd_ro_16_17 = np.array(list(df_ro_2016_bi_wh["yield.wh.g/m2"])+list(df_ro_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale

x = np.arange(0,1100,1)

curve_am = exp_curve(p_am,slope*x)
curve_ot = exp_curve(p_ot,slope*x)
curve_ro = exp_curve(p_ro,slope*x)

plot_curves_only([x,x,x],[curve_am,curve_ot,curve_ro],legend=["ambient","hot","hot/dry"],more_than_one_curve=True,xlabel="B. tectorum plants per m$^2$",
          ylabel="winter wheat yield",
          title="",savefile="yieldvspts_allclimates_16-17.pdf",
          color=["blue","red","black"],show=False,ylim=ylim,verticals=[10,100])

plot_data_with_textbox(cg_pts_am_16_17,yd_am_16_17,list(p_am)+[slope],"exp_lin",x=x,curve=curve_am,xlabel="B. tectorum plants per m$^2$",
          ylabel="winter wheat yield",
          title="",
          savefile="yieldvspts_ambient_16-17.pdf",
          color="blue",show=False,ylim=ylim)

plot_data_with_textbox(cg_pts_ot_16_17,yd_ot_16_17,list(p_ot)+[slope],"exp_lin",x=x,curve=curve_ot,xlabel="B. tectorum plants per m$^2$",
          ylabel="winter wheat yield",
          title="",
          savefile="yieldvspts_hot_16-17.pdf",
          color="red",show=False,ylim=ylim)

plot_data_with_textbox(cg_pts_ro_16_17,yd_ro_16_17,list(p_ro)+[slope],"exp_lin",x=x,curve=curve_ro,xlabel="B. tectorum plants per m$^2$",
          ylabel="winter wheat yield",
          title="",
          savefile="yieldvspts_hotdry_16-17.pdf",
          color="black",show=False,ylim=ylim)
