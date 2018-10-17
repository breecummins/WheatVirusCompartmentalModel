import numpy as np
from read_data import *
from fits_and_plots import *

##############################################################################################
# plot wheat yield vs wheat biomass in years 2015-2017
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

plot_data([wh_bio_15,wh_bio_16,wh_bio_17],[wh_yd_15,wh_yd_16,wh_yd_17],more_than_one_pts=True,legend=["2015","2016","2017"],x=x,curve=curve,xlabel="wheat biomass",ylabel="wheat yield",title="wheat yield vs biomass per m^2, pooled climates",savefile="wh_yieldvsbio_pooled_15-17.pdf",color=["blue","red","black"],show=False)


##############################################################################################
# plot wheat biomass vs number of plants in years 2016-2017 (no plant # data for 2015)
##############################################################################################

wh_pts_mo_16_17 = np.array(list(df_am_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_am_2017_mo_wh["springdensity.wh.plants/m2"])+ list(df_ot_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_ot_2017_mo_wh["springdensity.wh.plants/m2"]) + list(df_ro_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_ro_2017_mo_wh["springdensity.wh.plants/m2"]))/0.75

wh_bio_mo_16_17 = np.array(list(df_am_2016_mo_wh["bio.wh.g/m2"])+list(df_am_2017_mo_wh["bio.wh.g/m2"])+ list(df_ot_2016_mo_wh["bio.wh.g/m2"])+list(df_ot_2017_mo_wh["bio.wh.g/m2"]) + list(df_ro_2016_mo_wh["bio.wh.g/m2"])+list(df_ro_2017_mo_wh["bio.wh.g/m2"]))/0.75

plot_data(wh_pts_mo_16_17,wh_bio_mo_16_17,xlabel="# wheat plants",ylabel="wheat biomass",
          title="wheat biomass vs plants per m^2, monoculture, pooled climates, 2016-17",
          savefile="wh_mo_biovspts_pooled_16-17.pdf",show=False)

###########
wh_pts_bi_16_17 = np.array(list(df_am_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_am_2017_bi_wh["springdensity.wh.plants/m2"])+ list(df_ot_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_ot_2017_bi_wh["springdensity.wh.plants/m2"]) + list(df_ro_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_ro_2017_bi_wh["springdensity.wh.plants/m2"]))/0.75

wh_bio_bi_16_17 = np.array(list(df_am_2016_bi_wh["bio.wh.g/m2"])+list(df_am_2017_bi_wh["bio.wh.g/m2"])+ list(
    df_ot_2016_bi_wh["bio.wh.g/m2"])+list(df_ot_2017_bi_wh["bio.wh.g/m2"]) + list(df_ro_2016_bi_wh["bio.wh.g/m2"])+list(df_ro_2017_bi_wh["bio.wh.g/m2"]))/0.75

plot_data(wh_pts_bi_16_17,wh_bio_bi_16_17,xlabel="# wheat plants",ylabel="wheat biomass",
          title="wheat biomass vs plants per m^2, biculture, pooled climates, 2016-17",
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


plot_data([wh_pts_mo_16_17,wh_pts_bi_16_17],[wh_bio_mo_16_17,wh_bio_bi_16_17],more_than_one_pts=True,legend=["mono","bi"],more_than_one_curve=True,x=[x,x],curve=[curve_mo,curve_bi],xlabel="# wheat plants",ylabel="wheat biomass",title="wheat biomass vs plants per m^2, pooled climates, 2016-17",savefile="wh_bimo_biovspts_pooled_16-17.pdf",color=["blue","red"],show=False)


####################################################################
# plot cheatgrass biomass vs # of cheatgrass plants years 2016-2017
####################################################################

cg_bio = np.array(list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi_cg["bio.cg.g/m2"]) + list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi_cg["bio.cg.g/m2"]))/0.75

cg_pts = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi_cg["springdensity.cg.plants/m2"]) + list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi_cg["springdensity.cg.plants/m2"]) + list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi_cg["springdensity.cg.plants/m2"]))/0.75

x = np.arange(0,1200,1)
IC = np.array([1,-1])
curve = get_curve(cg_pts,cg_bio,lin_curve,IC,x)
slope = fit(cg_pts,cg_bio,lin_curve,IC)[0]
print("Biomass to number plants slope {}".format(slope))

plot_data(cg_pts,cg_bio,x=x,curve=curve,xlabel="# cheatgrass plants",ylabel="cheatgrass biomass",title="cheatgrass biomass vs plants per m^2, biculture, pooled climates, 2016-17",savefile="cg_bi_biovspts_pooled_16-17.pdf",show=False)


##################################################################
# plot wheat yield vs cheatgrass biomass by climate, pooled years
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
curve = get_curve(cg_am,yd_am,exp_curve,IC,x)
p_am = fit(cg_am,yd_am,exp_curve,IC)
print("Cheatgrass biomass to yield exp parameters (ambient) {}".format(p_am))

plot_data(cg_am,yd_am,x=x,curve=curve,xlabel="cheatgrass biomass",ylabel="wheat yield scaled to mean ambient 2015",ylim=ylim,title="wheat yield vs cheatgrass biomass per m^2, biculture, ambient, 2015-17",savefile="yieldvsbio_ambient_15-17.pdf",show=False)

###########
cg_ot = np.array(list(df_ot_2015_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi_cg["bio.cg.g/m2"]))/0.75
yd_ot = np.array(list(df_ot_2015_bi_wh["yield.wh.g/m2"])+ list(df_ot_2016_bi_wh["yield.wh.g/m2"])+list(df_ot_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale

bool_yd = yd_ot > 0
cg_ot=cg_ot[bool_yd]
yd_ot=yd_ot[bool_yd]

x = np.arange(0, 1800, 1)
IC = np.array([1,-1])
curve = get_curve(cg_ot,yd_ot,exp_curve,IC,x)
p_ot = fit(cg_ot,yd_ot,exp_curve,IC)
print("Cheatgrass biomass to yield exp parameters (hot) {}".format(p_ot))

plot_data(cg_ot,yd_ot,x=x,curve=curve,xlabel="cheatgrass biomass",ylabel="wheat yield scaled to mean ambient 2015",ylim=ylim,title="wheat yield vs cheatgrass biomass per m^2, biculture, hot, 2015-17",savefile="yieldvsbio_hot_15-17.pdf",show=False)

############
cg_ro = np.array(list(df_ro_2015_bi_cg["bio.cg.g/m2"])+list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi_cg["bio.cg.g/m2"]))/0.75
yd_ro = np.array(list(df_ro_2015_bi_wh["yield.wh.g/m2"])+ list(df_ro_2016_bi_wh["yield.wh.g/m2"])+list(df_ro_2017_bi_wh["yield.wh.g/m2"]))/0.75/yield_scale

bool_yd = yd_ro > 0
cg_ro=cg_ro[bool_yd]
yd_ro=yd_ro[bool_yd]

x = np.arange(0, 1800, 1)
IC = np.array([1,-1])
curve = get_curve(cg_ro,yd_ro,exp_curve,IC,x)
p_ro = fit(cg_ro,yd_ro,exp_curve,IC)
print("Cheatgrass biomass to yield exp parameters (hot/dry) {}".format(p_ro))

plot_data(cg_ro,yd_ro,x=x,curve=curve,xlabel="cheatgrass biomass",ylabel="wheat yield scaled to mean ambient 2015",ylim=ylim,title="wheat yield vs cheatgrass biomass per m^2, biculture, hot/dry, 2015-17",savefile="yieldvsbio_hotdry_15-17.pdf",show=False)

# FIXME: Now plug in linear fit to exponentials

# #############################################
#
# cg_pts_am = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi["springdensity.cg.plants/m2"]))
# cg_pts_ot = np.array(list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi["springdensity.cg.plants/m2"]))
# cg_pts_ro = np.array(list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi["springdensity.cg.plants/m2"]))
# wh_yield_am = np.array(list(df_am_2016_bi["yield.wh.g/m2"])+list(df_am_2017_bi["yield.wh.g/m2"]))/scale
# wh_yield_ot = np.array(list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]))/scale
# wh_yield_ro = np.array(list(df_ro_2016_bi["yield.wh.g/m2"])+list(df_ro_2017_bi["yield.wh.g/m2"]))/scale
#
# x = np.arange(0, 800, 1)
#
# amp_exp = am_p["x"][1]*np.exp(am_p["x"][0]*slope*x)
# otp_exp = ot_p["x"][1]*np.exp(ot_p["x"][0]*slope*x)
# rop_exp = ro_p["x"][1]*np.exp(ro_p["x"][0]*slope*x)
#
#
# plt.figure()
# plt.plot(cg_pts_am,wh_yield_am,linestyle="",marker="o")
# plt.plot(x,amp_exp)
# plt.title("Ambient 2016-2017")
# plt.xlabel("# cheatgrass plants")
# plt.ylabel("yield biomass scaled to 2015 ambient max")
# plt.ylim([-0.1,1.15])
# plt.xlim([-50,900])
# plt.savefig('am_biomass_with_linear.pdf')
# # plt.show()
# plt.close()
#
# plt.figure()
# plt.plot(cg_pts_ot,wh_yield_ot,linestyle="",marker="o")
# plt.plot(x,otp_exp)
# plt.title("Hot (ot) 2016-2017")
# plt.xlabel("# cheatgrass plants")
# plt.ylabel("yield biomass scaled to 2015 ambient max")
# plt.ylim([-0.1,1.15])
# plt.xlim([-50,900])
# plt.savefig('ot_biomass_with_linear.pdf')
# # plt.show()
# plt.close()
#
# plt.figure()
# plt.plot(cg_pts_ro,wh_yield_ro,linestyle="",marker="o")
# plt.plot(x,rop_exp)
# plt.title("Hot/dry (ro) 2016-2017")
# plt.xlabel("# cheatgrass plants")
# plt.ylabel("yield biomass scaled to 2015 ambient max")
# plt.ylim([-0.1,1.15])
# plt.xlim([-50,900])
# plt.savefig('ro_biomass_with_linear.pdf')
# # plt.show()
# plt.close()
