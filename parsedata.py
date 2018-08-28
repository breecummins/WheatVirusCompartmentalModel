import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

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


am = np.polyfit(cg_am,np.log(yd_am),1)
x = np.arange(0.0001, 1600, 10)
amp = np.exp(am[0])*np.exp(am[1]*x)

cg_ot = np.array(list(df_ot_2015_bi_cg["bio.cg.g/m2"])+list(df_ot_2016_bi_cg["bio.cg.g/m2"])+list(df_ot_2017_bi["bio.cg.g/m2"]))
yd_ot = np.array(list(df_ot_2015_bi["yield.wh.g/m2"])+list(df_ot_2016_bi["yield.wh.g/m2"])+list(df_ot_2017_bi["yield.wh.g/m2"]))/scale
inds = [i for i,y in enumerate(yd_ot) if np.isnan(y) ]
yd_ot = np.asarray([y for i,y in enumerate(yd_ot) if i not in inds])
cg_ot = np.asarray([y for i,y in enumerate(cg_ot) if i not in inds])

ot = np.polyfit(cg_ot,np.log(yd_ot),1)
otp = np.exp(ot[0])*np.exp(ot[1]*x)

cg_ro = np.array(list(df_ro_2015_bi_cg["bio.cg.g/m2"])+list(df_ro_2016_bi_cg["bio.cg.g/m2"])+list(df_ro_2017_bi["bio.cg.g/m2"]))
yd_ro = np.array(list(df_ro_2015_bi["yield.wh.g/m2"])+list(df_ro_2016_bi["yield.wh.g/m2"])+list(df_ro_2017_bi["yield.wh.g/m2"]))/scale

ro = np.polyfit(cg_ro,np.log(yd_ro),1)
rop = np.exp(ro[0])*np.exp(ro[1]*x)

####################################

plt.figure()
plt.plot(cg_am,yd_am,linestyle="",marker="o")
plt.plot(x,amp)
plt.title("Ambient")
plt.xlabel("cheatgrass biomass")
plt.ylabel("relative yield biomass")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.show()

plt.figure()
plt.plot(cg_ot,yd_ot,linestyle="",marker="o")
plt.plot(x,otp)
plt.title("Hot (ot)")
plt.xlabel("cheatgrass biomass")
plt.ylabel("relative yield biomass")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.show()

plt.figure()
plt.plot(cg_ro,yd_ro,linestyle="",marker="o")
plt.plot(x,rop)
plt.title("Hot/dry (ro)")
plt.xlabel("cheatgrass biomass")
plt.ylabel("relative yield biomass")
plt.ylim([-0.1,1.15])
plt.xlim([-50,1500])
plt.show()



