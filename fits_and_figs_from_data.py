import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import linregress

#########################################
# data extraction
#########################################


df = pd.read_csv(os.path.expanduser("PF_All_Yield_Bio_Den_Cov_Ht.csv"))

# split out 2015 data
df_am_2015_bi_wh = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ot_2015_bi_wh = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ro_2015_bi_wh = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='bi')]
df_am_2015_bi_cg = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ot_2015_bi_cg = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ro_2015_bi_cg = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='cg') & (df['compt']=='bi')]
df_am_2015_mo_wh = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ot_2015_mo_wh = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ro_2015_mo_wh = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='mo')]
df_am_2015_mo_cg = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='cg') & (df['compt']=='mo')]
df_ot_2015_mo_cg = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='cg') & (df['compt']=='mo')]
df_ro_2015_mo_cg = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='cg') & (df['compt']=='mo')]

# split out 2016 data
df_am_2016_bi_wh = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ot_2016_bi_wh = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ro_2016_bi_wh = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='bi')]
df_am_2016_bi_cg = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ot_2016_bi_cg = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ro_2016_bi_cg = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='cg') & (df['compt']=='bi')]
df_am_2016_mo_wh = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ot_2016_mo_wh = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ro_2016_mo_wh = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='mo')]
df_am_2016_mo_cg = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='cg') & (df['compt']=='mo')]
df_ot_2016_mo_cg = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='cg') & (df['compt']=='mo')]
df_ro_2016_mo_cg = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='cg') & (df['compt']=='mo')]

#split out 2017 data, has slightly different format than previous years
df_am_2017_bi_wh = df.loc[(df['year']==2017) & (df['climt']=='amb') & (df['spp']=='bi') & (df['compt']=='bi') ]
df_ot_2017_bi_wh = df.loc[(df['year']==2017) & (df['climt']=='otc') & (df['spp']=='bi') & (df['compt']=='bi')]
df_ro_2017_bi_wh = df.loc[(df['year']==2017) & (df['climt']=='ros') & (df['spp']=='bi') & (df['compt']=='bi')]
df_am_2017_bi_cg = df_am_2017_bi_wh
df_ot_2017_bi_cg = df_am_2017_bi_wh
df_ro_2017_bi_cg = df_am_2017_bi_wh
df_am_2017_mo_wh = df.loc[(df['year']==2017) & (df['climt']=='amb') & (df['spp']=='wh') & (df['compt']=='mo') ]
df_ot_2017_mo_wh = df.loc[(df['year']==2017) & (df['climt']=='otc') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ro_2017_mo_wh = df.loc[(df['year']==2017) & (df['climt']=='ros') & (df['spp']=='wh') & (df['compt']=='mo')]
df_am_2017_mo_cg = df.loc[(df['year']==2017) & (df['climt']=='amb') & (df['spp']=='cg') & (df['compt']=='mo') ]
df_ot_2017_mo_cg = df.loc[(df['year']==2017) & (df['climt']=='otc') & (df['spp']=='cg') & (df['compt']=='mo')]
df_ro_2017_mo_cg = df.loc[(df['year']==2017) & (df['climt']=='ros') & (df['spp']=='cg') & (df['compt']=='mo')]

################################
# generic plotting function
################################

def plot_data(xpts,ypts,more_than_one_pts=False,legend = False,more_than_one_curve=False,x=None,curve=None,xlabel="",\
                                                                                                            ylabel="",title="",
              savefile="",
              color="blue",show=False):
    plt.figure()
    if more_than_one_pts:
        if isinstance(color,str):
            color = [color]*len(xpts)
        if not legend:
            for (xp, yp, c) in zip(xpts, ypts, color):
                plt.plot(xp, yp, linestyle="", marker="o", color=c)
        else:
            for (xp,yp,c,lab) in zip(xpts,ypts,color,legend):
                plt.plot(xp,yp,linestyle="",marker="o",color=c,label=lab)
            plt.legend()
    else:
        plt.plot(xpts, ypts, linestyle="", marker="o", color=color)
    if more_than_one_curve:
        if isinstance(color,str):
            color = [color]*len(xpts)
        for (xp, yp, c) in zip(x, curve, color):
            plt.plot(xp, yp, color=c)
    elif x and any(curve):
        plt.plot(x,curve)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if savefile:
        plt.savefig(savefile)
    if show:
        plt.show()
    else:
        plt.close()


################################
# data fitting
################################

def lin_curve(p,x):
    # good IC = np.array([1])
    return p[0]*x

def exp_curve(p,x):
    # good IC = np.array([1,-1])
    return p[0]*np.exp(p[1]*x)

def log_curve(p,x):
    # good IC = np.array([1,-1])
    return p[0] * (1 + np.exp(-x))**(p[1])

def fit(xpts,ypts,curve,IC):
    def func(p,x,y):
        return curve(p,x) -y
    p = least_squares(func,IC,args=(xpts, ypts))
    return p["x"]

def get_curve(xpts,ypts,curve,IC,x):
    p = fit(xpts,ypts,curve,IC)
    return curve(p,x)


##############################################################################################
# plot wheat biomass vs number of plants in years 2016-2017 (no plant # data for 2015)
##############################################################################################

wh_pts_mo_16_17 = np.array(list(df_am_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_am_2017_mo_wh["springdensity.wh.plants/m2"])+ list(df_ot_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_ot_2017_mo_wh["springdensity.wh.plants/m2"]) + list(df_ro_2016_mo_wh["springdensity.wh.plants/m2"])+list(df_ro_2017_mo_wh["springdensity.wh.plants/m2"]))

wh_bio_mo_16_17 = np.array(list(df_am_2016_mo_wh["bio.wh.g/m2"])+list(df_am_2017_mo_wh["bio.wh.g/m2"])+ list(df_ot_2016_mo_wh["bio.wh.g/m2"])+list(df_ot_2017_mo_wh["bio.wh.g/m2"]) + list(df_ro_2016_mo_wh["bio.wh.g/m2"])+list(df_ro_2017_mo_wh["bio.wh.g/m2"]))

plot_data(wh_pts_mo_16_17/0.75,wh_bio_mo_16_17/0.75,xlabel="# wheat plants",ylabel="wheat biomass",
          title="wheat biomass vs plants per m^2, monoculture, pooled climates, 2016-17",
          savefile="wh_mo_biovspts_pooled_16-17.pdf",show=False)

wh_pts_bi_16_17 = np.array(list(df_am_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_am_2017_bi_wh["springdensity.wh.plants/m2"])+ list(df_ot_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_ot_2017_bi_wh["springdensity.wh.plants/m2"]) + list(df_ro_2016_bi_wh["springdensity.wh.plants/m2"])+list(df_ro_2017_bi_wh["springdensity.wh.plants/m2"]))

wh_bio_bi_16_17 = np.array(list(df_am_2016_bi_wh["bio.wh.g/m2"])+list(df_am_2017_bi_wh["bio.wh.g/m2"])+ list(
    df_ot_2016_bi_wh["bio.wh.g/m2"])+list(df_ot_2017_bi_wh["bio.wh.g/m2"]) + list(df_ro_2016_bi_wh["bio.wh.g/m2"])+list(df_ro_2017_bi_wh["bio.wh.g/m2"]))

plot_data(wh_pts_bi_16_17/0.75,wh_bio_bi_16_17/0.75,xlabel="# wheat plants",ylabel="wheat biomass",
          title="wheat biomass vs plants per m^2, biculture, pooled climates, 2016-17",
          savefile="wh_bi_biovspts_pooled_16-17.pdf",show=False)

wh_pts_mo = wh_pts_mo_16_17[wh_pts_mo_16_17>0]
wh_pts_bi = wh_pts_bi_16_17[wh_pts_bi_16_17>0]
wh_bio_mo = wh_bio_mo_16_17[wh_pts_mo_16_17>0]
wh_bio_bi = wh_bio_bi_16_17[wh_pts_bi_16_17>0]

x = np.arange(0,350,1)
IC = np.array([1,-1])

curve_mo = get_curve(wh_pts_mo/0.75,wh_bio_mo/0.75,lin_curve,IC,x)
curve_bi = get_curve(wh_pts_bi/0.75,wh_bio_bi/0.75,lin_curve,IC,x)

# curve_mo = get_curve(wh_pts_mo/0.75,wh_bio_mo/0.75,log_curve,IC,x)
# curve_bi = get_curve(wh_pts_bi/0.75,wh_bio_bi/0.75,log_curve,IC,x)


plot_data([wh_pts_mo_16_17/0.75,wh_pts_bi_16_17/0.75],[wh_bio_mo_16_17/0.75,wh_bio_bi_16_17/0.75],more_than_one_pts=True,
          legend=["mono","bi"],more_than_one_curve=True,x=[x,x],curve=[curve_mo,curve_bi],xlabel="# wheat plants",ylabel="wheat biomass",title="wheat biomass vs plants per  m^2, pooled climates, 2016-17",savefile="wh_bimo_biovspts_pooled_16-17.pdf",color=["blue","red"],show=True)







# ##########################################
# wh_bio = np.array(list(df_am_2015_bi["bio.wh.g/m2"])+list(df_am_2016_bi["bio.wh.g/m2"])+list(df_am_2017_bi["bio.wh.g/m2"])+list(df_ot_2015_bi["bio.wh.g/m2"])+list(df_ot_2016_bi["bio.wh.g/m2"])+list(df_ot_2017_bi["bio.wh.g/m2"]) + list(df_ro_2015_bi["bio.wh.g/m2"]) + list(df_ro_2016_bi["bio.wh.g/m2"])+list(df_ro_2017_bi["bio.wh.g/m2"]))
#
# wh_bio_am = np.array(list(df_am_2015_bi["bio.wh.g/m2"])+list(df_am_2016_bi["bio.wh.g/m2"])+list(df_am_2017_bi["bio.wh.g/m2"]))
#
# wh_bio_15 = np.array(list(df_am_2015_bi["bio.wh.g/m2"])+list(df_ot_2015_bi["bio.wh.g/m2"])+list(df_ro_2015_bi["bio.wh.g/m2"]))
#
# wh_pts = np.array(list(df_am_2016_bi["springdensity.wh.plants/m2"])+list(df_am_2017_bi["springdensity.wh.plants/m2"])+ list(df_ot_2016_bi["springdensity.wh.plants/m2"])+list(df_ot_2017_bi["springdensity.wh.plants/m2"]) + list(df_ro_2016_bi["springdensity.wh.plants/m2"])+list(df_ro_2017_bi["springdensity.wh.plants/m2"]))
#
# wh_pts_am = np.array(list(df_am_2015_bi["springdensity.wh.plants/m2"])+list(df_am_2016_bi["springdensity.wh.plants/m2"])+list(df_am_2017_bi["springdensity.wh.plants/m2"]))
#
# wh_yd = np.array(list(df_am_2015_bi["yield.wh.g/m2"])+list(df_am_2016_bi["yield.wh.g/m2"])+list(df_am_2017_bi["yield.wh.g/m2"])+list(df_ot_2015_bi["yield.wh.g/m2"])+list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]) + list(df_ro_2015_bi["yield.wh.g/m2"]) + list(df_ro_2016_bi["yield.wh.g/m2"])+list(df_ro_2017_bi["yield.wh.g/m2"]))
#
# wh_yd_am = np.array(list(df_am_2015_bi["yield.wh.g/m2"])+list(df_am_2016_bi["yield.wh.g/m2"])+list(df_am_2017_bi["yield.wh.g/m2"]))
#
# wh_yd_15 = np.array(list(df_am_2015_bi["yield.wh.g/m2"])+list(df_ot_2015_bi["yield.wh.g/m2"])+list(df_ro_2015_bi["yield.wh.g/m2"]))
#
# plt.figure()
# plt.plot(wh_bio,wh_yd,linestyle="",marker="o")
# plt.plot(wh_bio_15,wh_yd_15,linestyle="",marker="o",color="red")
# plt.title("wheat biomass vs yield, pooled conditions, 2015")
# plt.xlabel("wheat biomass")
# plt.ylabel("wheat yield")
# # plt.savefig('wheat_yield_vs_plants_ambient.pdf')
# # plt.show()
# # plt.close()
#
#
# ###########################################
#
# cg_bio = np.array(list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi["bio.cg.g/m2"]) + list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi["bio.cg.g/m2"]))
# cg_pts = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi["springdensity.cg.plants/m2"]) + list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi["springdensity.cg.plants/m2"]) + list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi["springdensity.cg.plants/m2"]))
#
#
# def lin(a,x,y):
#     return a[0]*x -y
#
#
# p = least_squares(lin,np.array([1]),args=(cg_pts, cg_bio))
# slope = p["x"][0]
# print("Biomass to number plants slope {}".format(slope))
#
# x = np.arange(0, 800, 1)
#
# plt.figure()
# plt.plot(cg_pts,cg_bio,linestyle="",marker="o")
# plt.plot(x,slope*x)
# plt.title("Plant number vs biomass, climate conditions pooled, 2016-2017")
# plt.xlabel("# cheatgrass plants (spring)")
# plt.ylabel("cheatgrass biomass")
# plt.savefig('biomass_linear_fit.pdf')
# # plt.show()
# plt.close()
#
#
# ####################################
# scale = max(list(df_am_2015_bi["yield.wh.g/m2"]))
#
# cg_am = np.array(list(df_am_2015_bi_cg["bio.cg.g/m2"])+list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi["bio.cg.g/m2"]))
# yd_am = np.array(list(df_am_2015_bi["yield.wh.g/m2"])+ list(df_am_2016_bi["yield.wh.g/m2"])+list(df_am_2017_bi["yield.wh.g/m2"]))/scale
#
#
# def expfit(p,x,y):
#     return p[1]*np.exp(p[0]*x) - y
#
# x = np.arange(0, 1600, 1)
#
# am_p = least_squares(expfit,np.array([-1,1]),args=(cg_am, yd_am))
# amp = am_p["x"][1]*np.exp(am_p["x"][0]*x)
# print("Yield vs cheatgrass biomass")
# print("Ambient: {}".format(am_p["x"]))
#
#
#
# cg_ot = np.array(list(df_ot_2015_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi["bio.cg.g/m2"]))
# yd_ot = np.array(list(df_ot_2015_bi["yield.wh.g/m2"])+list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]))/scale
# inds = [i for i,y in enumerate(yd_ot) if np.isnan(y) ]
# yd_ot = np.asarray([y for i,y in enumerate(yd_ot) if i not in inds])
# cg_ot = np.asarray([y for i,y in enumerate(cg_ot) if i not in inds])
#
# ot_p = least_squares(expfit,np.array([-1,1]),args=(cg_ot, yd_ot))
# otp = ot_p["x"][1]*np.exp(ot_p["x"][0]*x)
# print("Hot: {}".format(ot_p["x"]))
#
#
# cg_ro = np.array(list(df_ro_2015_bi_cg["bio.cg.g/m2"])+list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi["bio.cg.g/m2"]))
# yd_ro = np.array(list(df_ro_2015_bi["yield.wh.g/m2"])+list(df_ro_2016_bi["yield.wh.g/m2"])+list(df_ro_2017_bi["yield.wh.g/m2"]))/scale
#
# ro_p = least_squares(expfit,np.array([-1,1]),args=(cg_ro, yd_ro))
# rop = ro_p["x"][1]*np.exp(ro_p["x"][0]*x)
# print("Hot/dry: {}".format(ro_p["x"]))
#
#
#
# ####################################
#
# plt.figure()
# plt.plot(cg_am,yd_am,linestyle="",marker="o")
# plt.plot(x,amp)
# plt.title("Ambient 2015-2017")
# plt.xlabel("cheatgrass biomass")
# plt.ylabel("yield biomass scaled to 2015 ambient max")
# plt.ylim([-0.1,1.15])
# plt.xlim([-50,1500])
# plt.savefig('am_biomass.pdf')
# # plt.show()
# plt.close()
#
# plt.figure()
# plt.plot(cg_ot,yd_ot,linestyle="",marker="o")
# plt.plot(x,otp)
# plt.title("Hot (ot) 2015-2017")
# plt.xlabel("cheatgrass biomass")
# plt.ylabel("yield biomass scaled to 2015 ambient max")
# plt.ylim([-0.1,1.15])
# plt.xlim([-50,1500])
# plt.savefig('ot_biomass.pdf')
# # plt.show()
# plt.close()
#
# plt.figure()
# plt.plot(cg_ro,yd_ro,linestyle="",marker="o")
# plt.plot(x,rop)
# plt.title("Hot/dry (ro) 2015-2017")
# plt.xlabel("cheatgrass biomass")
# plt.ylabel("yield biomass scaled to 2015 ambient max")
# plt.ylim([-0.1,1.15])
# plt.xlim([-50,1500])
# plt.savefig('ro_biomass.pdf')
# # plt.show()
# plt.close()
#
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
