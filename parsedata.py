import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares

df = pd.read_csv(os.path.expanduser("PF_All_Yield_Bio_Den_Cov_Ht.csv"))

df_am_2015_bi = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ot_2015_bi = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ro_2015_bi = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='bi')]
df_am_2015_bi_cg = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ot_2015_bi_cg = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ro_2015_bi_cg = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='cg') & (df['compt']=='bi')]


df_am_2016_bi = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='bi')]
df_am_2016_bi_cg = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='cg') & (df['compt']=='bi')]
df_am_2017_bi = df.loc[(df['year']==2017) & (df['climt']=='amb') & (df['spp']=='bi') & (df['compt']=='bi') ]
df_ot_2016_bi = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ot_2016_bi_cg = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ot_2017_bi = df.loc[(df['year']==2017) & (df['climt']=='otc') & (df['spp']=='bi') & (df['compt']=='bi')]
df_ro_2016_bi = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ro_2016_bi_cg = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='cg') & (df['compt']=='bi')]
df_ro_2017_bi = df.loc[(df['year']==2017) & (df['climt']=='ros') & (df['spp']=='bi') & (df['compt']=='bi')]

df_am_2017_bi = df_am_2017_bi[(df_am_2017_bi["bio.wh.g/m2"] != 0) & df_am_2017_bi["bio.cg.g/m2"] != 0]
df_ot_2017_bi = df_ot_2017_bi[(df_ot_2017_bi["bio.wh.g/m2"] != 0) & df_ot_2017_bi["bio.cg.g/m2"] != 0]
df_ro_2017_bi = df_ro_2017_bi[(df_ro_2017_bi["bio.wh.g/m2"] != 0) & df_ro_2017_bi["bio.cg.g/m2"] != 0]

####################################
scale = max(list(df_am_2015_bi["yield.wh.g/m2"]))

cg_am = np.array(list(df_am_2015_bi_cg["bio.cg.g/m2"])+list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi["bio.cg.g/m2"]))
yd_am = np.array(list(df_am_2015_bi["yield.wh.g/m2"])+ list(df_am_2016_bi["yield.wh.g/m2"])+list(df_am_2017_bi["yield.wh.g/m2"]))/scale


def expfit(p,x,y):
    return p[1]*np.exp(p[0]*x) - y


am_p = least_squares(expfit,np.array([-1,1]),args=(cg_am, yd_am))
x = np.arange(0, 1600, 1)
amp = am_p["x"][1]*np.exp(am_p["x"][0]*x)
print("Yield vs cheatgrass biomass")
print("Ambient: {}".format(am_p["x"]))

# am = np.polyfit(cg_am,np.log(yd_am),1)
# x = np.arange(0.0001, 1600, 1)
# amp = np.exp(am[1])*np.exp(am[0]*x)




cg_ot = np.array(list(df_ot_2015_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi["bio.cg.g/m2"]))
yd_ot = np.array(list(df_ot_2015_bi["yield.wh.g/m2"])+list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]))/scale
inds = [i for i,y in enumerate(yd_ot) if np.isnan(y) ]
yd_ot = np.asarray([y for i,y in enumerate(yd_ot) if i not in inds])
cg_ot = np.asarray([y for i,y in enumerate(cg_ot) if i not in inds])

ot_p = least_squares(expfit,np.array([-1,1]),args=(cg_ot, yd_ot))
otp = ot_p["x"][1]*np.exp(ot_p["x"][0]*x)
print("Hot: {}".format(ot_p["x"]))

# ot = np.polyfit(cg_ot,np.log(yd_ot),1)
# otp = np.exp(ot[1])*np.exp(ot[0]*x)

cg_ro = np.array(list(df_ro_2015_bi_cg["bio.cg.g/m2"])+list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi["bio.cg.g/m2"]))
yd_ro = np.array(list(df_ro_2015_bi["yield.wh.g/m2"])+list(df_ro_2016_bi["yield.wh.g/m2"])+list(df_ro_2017_bi["yield.wh.g/m2"]))/scale

ro_p = least_squares(expfit,np.array([-1,1]),args=(cg_ro, yd_ro))
rop = ro_p["x"][1]*np.exp(ro_p["x"][0]*x)
print("Hot/dry: {}".format(ro_p["x"]))

# ro = np.polyfit(cg_ro,np.log(yd_ro),1)
# rop = np.exp(ro[1])*np.exp(ro[0]*x)

####################################

plt.figure()
plt.plot(cg_am,yd_am,linestyle="",marker="o")
plt.plot(x,amp)
plt.title("Ambient 2015-2017")
plt.xlabel("cheatgrass biomass")
plt.ylabel("yield biomass scaled to 2015 ambient max")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.savefig('am_biomass.pdf')
# plt.show()
plt.close()

plt.figure()
plt.plot(cg_ot,yd_ot,linestyle="",marker="o")
plt.plot(x,otp)
plt.title("Hot (ot) 2015-2017")
plt.xlabel("cheatgrass biomass")
plt.ylabel("yield biomass scaled to 2015 ambient max")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.savefig('ot_biomass.pdf')
# plt.show()
plt.close()

plt.figure()
plt.plot(cg_ro,yd_ro,linestyle="",marker="o")
plt.plot(x,rop)
plt.title("Hot/dry (ro) 2015-2017")
plt.xlabel("cheatgrass biomass")
plt.ylabel("yield biomass scaled to 2015 ambient max")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.savefig('ro_biomass.pdf')
# plt.show()
plt.close()


# ###########################################
#
# cg_am_bio = np.array(list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi["bio.cg.g/m2"]))
# cg_am_pts = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi["springdensity.cg.plants/m2"]))
#
#
# def lin(a,x,y):
#     return a[0]*x -y
#
#
# p = least_squares(lin,np.array([1]),args=(cg_am_pts, cg_am_bio))
# x = np.arange(0, 800, 1)
# amp_lin = p["x"][0]*x
# print("Biomass to number plants")
# print("Ambient: {}".format(p["x"]))
#
# amp_exp = am_p["x"][1]*np.exp(am_p["x"][0]*amp_lin)
# am_slope = p["x"][0]
#
#
# plt.figure()
# plt.plot(cg_am_pts,cg_am_bio,linestyle="",marker="o")
# plt.plot(x,amp_lin)
# plt.title("Ambient 2016-2017")
# plt.xlabel("# cheatgrass plants (spring)")
# plt.ylabel("cheatgrass biomass")
# plt.savefig('am_linear.pdf')
# plt.close()
#
# cg_ot_bio = np.array(list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi["bio.cg.g/m2"]))
# cg_ot_pts = np.array(list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi["springdensity.cg.plants/m2"]))
#
# p = least_squares(lin,np.array([1]),args=(cg_ot_pts, cg_ot_bio))
# otp_lin = p["x"][0]*x
# print("Hot: {}".format(p["x"]))
#
# otp_exp = ot_p["x"][1]*np.exp(ot_p["x"][0]*otp_lin)
# ot_slope = p["x"][0]
#
#
# plt.figure()
# plt.plot(cg_ot_pts,cg_ot_bio,linestyle="",marker="o")
# plt.plot(x,otp_lin)
# plt.title("Hot 2016-2017")
# plt.xlabel("# cheatgrass plants (spring)")
# plt.ylabel("cheatgrass biomass")
# plt.savefig('ot_linear.pdf')
# plt.close()
#
# cg_ro_bio = np.array(list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi["bio.cg.g/m2"]))
# cg_ro_pts = np.array(list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi["springdensity.cg.plants/m2"]))
#
# p = least_squares(lin,np.array([1]),args=(cg_ro_pts, cg_ro_bio))
# rop_lin = p["x"][0]*x
# print("Hot/dry: {}".format(p["x"]))
#
# rop_exp = ro_p["x"][1]*np.exp(ro_p["x"][0]*rop_lin)
# ro_slope = p["x"][0]
#
# plt.figure()
# plt.plot(cg_ro_pts,cg_ro_bio,linestyle="",marker="o")
# plt.plot(x,rop_lin)
# plt.title("Hot/dry 2016-2017")
# plt.xlabel("# cheatgrass plants (spring)")
# plt.ylabel("cheatgrass biomass")
# plt.savefig('ro_linear.pdf')
# plt.close()
#
# ######################################################
#
# plt.figure()
# plt.plot(cg_am_pts, yd_am[8:], linestyle="",marker="o")
# plt.plot(x,amp_exp)
# plt.title("Ambient 2016-2017")
# plt.xlabel("# cheatgrass plants (spring)")
# plt.ylabel("yield biomass scaled by ambient 2015")
# plt.savefig('am_numplants.pdf')
# plt.close()
#
# cg_ot_pts = np.array(list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi["springdensity.cg.plants/m2"]))
# yd_ot = np.array(list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]))/scale
#
# plt.figure()
# plt.plot(cg_ot_pts, yd_ot, linestyle="",marker="o")
# plt.plot(x,otp_exp)
# plt.title("Hot 2016-2017")
# plt.xlabel("# cheatgrass plants (spring)")
# plt.ylabel("yield biomass scaled by ambient 2015")
# plt.savefig('ot_numplants.pdf')
# plt.close()
#
# plt.figure()
# plt.plot(cg_ro_pts, yd_ro[8:], linestyle="",marker="o")
# plt.plot(x,rop_exp)
# plt.title("Hot/dry 2016-2017")
# plt.xlabel("# cheatgrass plants (spring)")
# plt.ylabel("yield biomass scaled by ambient 2015")
# plt.savefig('ro_numplants.pdf')
# plt.close()

cg_bio = np.array(list(df_am_2016_bi_cg["bio.cg.g/m2"])+list(df_am_2017_bi["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi["bio.cg.g/m2"])+list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi["bio.cg.g/m2"]))
cg_pts = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi["springdensity.cg.plants/m2"])+list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi["springdensity.cg.plants/m2"])+list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi["springdensity.cg.plants/m2"]))


def satfunc(a,x,y):
    return a[0]*x**a[2]/(a[1]+x**a[2]) -y


x = np.arange(0, 900, 1)

p = least_squares(satfunc,np.array([100,100,5]),args=(cg_pts, cg_bio))
print("Cheatgrass biomass to number plants")
print(p["x"])
sf = p["x"][0]*x**p["x"][2]/(p["x"][1]+x**p["x"][2])

plt.figure()
plt.plot(cg_pts, cg_bio, linestyle="",marker="o")
plt.plot(x,sf)
plt.title("All climates 2016-2017")
plt.xlabel("# cheatgrass plants (spring)")
plt.ylabel("cheatgrass biomass")
plt.savefig('all_numplants.pdf')


##################################################

######################################################
x = np.arange(175, 900, 1)
sf = p["x"][0]*x**p["x"][2]/(p["x"][1]+x**p["x"][2])

amp_exp = am_p["x"][1]*np.exp(am_p["x"][0]*sf)
otp_exp = ot_p["x"][1]*np.exp(ot_p["x"][0]*sf)
rop_exp = ro_p["x"][1]*np.exp(ro_p["x"][0]*sf)

cg_am_pts = np.array(list(df_am_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_am_2017_bi["springdensity.cg.plants/m2"]))
yd_am = np.array(list(df_am_2016_bi["yield.wh.g/m2"])+list(df_am_2017_bi["yield.wh.g/m2"]))/scale

plt.figure()
plt.plot(cg_am_pts, yd_am, linestyle="",marker="o")
plt.plot(x,amp_exp)
plt.title("Ambient 2016-2017")
plt.xlabel("# cheatgrass plants (spring)")
plt.ylabel("yield biomass scaled by ambient max 2015")
plt.savefig('am_numplants.pdf')
plt.close()

cg_ot_pts = np.array(list(df_ot_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ot_2017_bi["springdensity.cg.plants/m2"]))
yd_ot = np.array(list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]))/scale

plt.figure()
plt.plot(cg_ot_pts, yd_ot, linestyle="",marker="o")
plt.plot(x,otp_exp)
plt.title("Hot 2016-2017")
plt.xlabel("# cheatgrass plants (spring)")
plt.ylabel("yield biomass scaled by ambient max 2015")
plt.savefig('ot_numplants.pdf')
plt.close()

cg_ro_pts = np.array(list(df_ro_2016_bi_cg["springdensity.cg.plants/m2"])+list(df_ro_2017_bi["springdensity.cg.plants/m2"]))
yd_ro = np.array(list(df_ro_2016_bi["yield.wh.g/m2"])+list(df_ro_2017_bi["yield.wh.g/m2"]))/scale

plt.figure()
plt.plot(cg_ro_pts, yd_ro, linestyle="",marker="o")
plt.plot(x,rop_exp)
plt.title("Hot/dry 2016-2017")
plt.xlabel("# cheatgrass plants (spring)")
plt.ylabel("yield biomass scaled by ambient max 2015")
plt.savefig('ro_numplants.pdf')
plt.close()


############################################################

x = np.arange(0, 100, 1)
sf = p["x"][0]*x**p["x"][2]/(p["x"][1]+x**p["x"][2])

amp_exp = am_p["x"][1]*np.exp(am_p["x"][0]*sf)
otp_exp = ot_p["x"][1]*np.exp(ot_p["x"][0]*sf)
rop_exp = ro_p["x"][1]*np.exp(ro_p["x"][0]*sf)

scale = am_p["x"][1]


plt.figure()
plt.plot(x,amp_exp,label="ambient")
plt.plot(x,otp_exp,label="hot")
plt.plot(x,rop_exp,label="hot/dry")
plt.title("Extrapolation to low plant numbers")
plt.xlabel("# cheatgrass plants (spring)")
plt.ylabel("yield biomass scaled by ambient max 2015")
plt.legend()
plt.savefig('low_numplants.pdf')
# plt.close()

plt.show()