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


p = least_squares(expfit,np.array([-1,1]),args=(cg_am, yd_am))
x = np.arange(0, 1600, 1)
amp = p["x"][1]*np.exp(p["x"][0]*x)
print("Ambient: {}".format(p["x"]))

# am = np.polyfit(cg_am,np.log(yd_am),1)
# x = np.arange(0.0001, 1600, 1)
# amp = np.exp(am[1])*np.exp(am[0]*x)




cg_ot = np.array(list(df_ot_2015_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi["bio.cg.g/m2"]))
yd_ot = np.array(list(df_ot_2015_bi["yield.wh.g/m2"])+list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]))/scale
inds = [i for i,y in enumerate(yd_ot) if np.isnan(y) ]
yd_ot = np.asarray([y for i,y in enumerate(yd_ot) if i not in inds])
cg_ot = np.asarray([y for i,y in enumerate(cg_ot) if i not in inds])

p = least_squares(expfit,np.array([-1,1]),args=(cg_ot, yd_ot))
otp = p["x"][1]*np.exp(p["x"][0]*x)
print("Hot: {}".format(p["x"]))

# ot = np.polyfit(cg_ot,np.log(yd_ot),1)
# otp = np.exp(ot[1])*np.exp(ot[0]*x)

cg_ro = np.array(list(df_ro_2015_bi_cg["bio.cg.g/m2"])+list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi["bio.cg.g/m2"]))
yd_ro = np.array(list(df_ro_2015_bi["yield.wh.g/m2"])+list(df_ro_2016_bi["yield.wh.g/m2"])+list(df_ro_2017_bi["yield.wh.g/m2"]))/scale

p = least_squares(expfit,np.array([-1,1]),args=(cg_ro, yd_ro))
rop = p["x"][1]*np.exp(p["x"][0]*x)
print("Hot/dry: {}".format(p["x"]))

# ro = np.polyfit(cg_ro,np.log(yd_ro),1)
# rop = np.exp(ro[1])*np.exp(ro[0]*x)

####################################

plt.figure()
plt.plot(cg_am,yd_am,linestyle="",marker="o")
plt.plot(x,amp)
plt.title("Ambient")
plt.xlabel("cheatgrass biomass")
plt.ylabel("relative yield biomass")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.savefig('am.pdf')
plt.show()

plt.figure()
plt.plot(cg_ot,yd_ot,linestyle="",marker="o")
plt.plot(x,otp)
plt.title("Hot (ot)")
plt.xlabel("cheatgrass biomass")
plt.ylabel("relative yield biomass")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.savefig('ot.pdf')
plt.show()

plt.figure()
plt.plot(cg_ro,yd_ro,linestyle="",marker="o")
plt.plot(x,rop)
plt.title("Hot/dry (ro)")
plt.xlabel("cheatgrass biomass")
plt.ylabel("relative yield biomass")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.savefig('ro.pdf')
plt.show()



