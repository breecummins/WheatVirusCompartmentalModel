import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(os.path.expanduser("PF_All_Yield_Bio_Den_Cov_Ht.csv"))
df_am_2015_bi = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='bi')]
df_am_2015_mo = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ot_2015_bi = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ot_2015_mo = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ro_2015_bi = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ro_2015_mo = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='mo')]

# for z in zip(df_am_2015["yield.wh.g/m2"],df_am_2015["pcntcov.wh"],df_am_2015["bio.wh.g/m2"]):
#     print(z)

# plt.scatter(df_am_2015_bi["bio.wh.g/m2"],df_am_2015_bi["yield.wh.g/m2"], color="blue", label="biculture")
# plt.hold('on')
# plt.scatter(df_am_2015_mo["bio.wh.g/m2"],df_am_2015_mo["yield.wh.g/m2"], color="red", label="monoculture")
# plt.legend()
# plt.show()

# fig = plt.figure()
# plt.title("2015")
# plt.ylim([0,0.5])
# plt.plot([1]*len(df_am_2015_bi["yield.wh.g/m2"]),df_am_2015_bi["yield.wh.g/m2"]/df_am_2015_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="blue", label="am bi")
# plt.hold('on')
# plt.plot([2]*len(df_am_2015_mo["yield.wh.g/m2"]),df_am_2015_mo["yield.wh.g/m2"]/df_am_2015_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="red", label="am mono")
# plt.plot([3]*len(df_ot_2015_bi["yield.wh.g/m2"]),df_ot_2015_bi["yield.wh.g/m2"]/df_ot_2015_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="green", label="ot bi")
# plt.hold('on')
# plt.plot([4]*len(df_ot_2015_mo["yield.wh.g/m2"]),df_ot_2015_mo["yield.wh.g/m2"]/df_ot_2015_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="black", label="ot mono")
# plt.plot([5]*len(df_ro_2015_bi["yield.wh.g/m2"]),df_ro_2015_bi["yield.wh.g/m2"]/df_ro_2015_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="cyan", label="ro bi")
# plt.hold('on')
# plt.plot([6]*len(df_ro_2015_mo["yield.wh.g/m2"]),df_ro_2015_mo["yield.wh.g/m2"]/df_ro_2015_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="magenta", label="ro mono")
# lgd = plt.legend(bbox_to_anchor=(1.0, 1.0))
# fig.savefig('PF2015.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')

df_am_2016_bi = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='bi')]
df_am_2016_mo = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='wh') & (df['compt']=='mo')]
df_am_2017_bi = df.loc[(df['year']==2017) & (df['climt']=='amb') & (df['spp']=='bi') & (df['compt']=='bi') ]
df_am_2017_mo = df.loc[(df['year']==2017) & (df['climt']=='amb') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ot_2016_bi = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ot_2016_mo = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ot_2017_bi = df.loc[(df['year']==2017) & (df['climt']=='otc') & (df['spp']=='bi') & (df['compt']=='bi')]
df_ot_2017_mo = df.loc[(df['year']==2017) & (df['climt']=='otc') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ro_2016_bi = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='bi')]
df_ro_2016_mo = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='wh') & (df['compt']=='mo')]
df_ro_2017_bi = df.loc[(df['year']==2017) & (df['climt']=='ros') & (df['spp']=='bi') & (df['compt']=='bi')]
df_ro_2017_mo = df.loc[(df['year']==2017) & (df['climt']=='ros') & (df['spp']=='wh') & (df['compt']=='mo')]

df_am_2017_bi = df_am_2017_bi[(df_am_2017_bi["bio.wh.g/m2"] != 0) & df_am_2017_bi["bio.cg.g/m2"] != 0]
df_ot_2017_bi = df_ot_2017_bi[(df_ot_2017_bi["bio.wh.g/m2"] != 0) & df_ot_2017_bi["bio.cg.g/m2"] != 0]
df_ro_2017_bi = df_ro_2017_bi[(df_ro_2017_bi["bio.wh.g/m2"] != 0) & df_ro_2017_bi["bio.cg.g/m2"] != 0]

# fig = plt.figure()
# plt.title("2016")
# plt.ylim([0,0.5])
# plt.plot([1]*len(df_am_2016_bi["yield.wh.g/m2"]),df_am_2016_bi["yield.wh.g/m2"]/df_am_2016_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="blue", label="am bi")
# plt.hold('on')
# plt.plot([2]*len(df_am_2016_mo["yield.wh.g/m2"]),df_am_2016_mo["yield.wh.g/m2"]/df_am_2016_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="red", label="am mono")
# plt.plot([3]*len(df_ot_2016_bi["yield.wh.g/m2"]),df_ot_2016_bi["yield.wh.g/m2"]/df_ot_2016_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="green", label="ot bi")
# plt.hold('on')
# plt.plot([4]*len(df_ot_2016_mo["yield.wh.g/m2"]),df_ot_2016_mo["yield.wh.g/m2"]/df_ot_2016_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="black", label="ot mono")
# plt.plot([5]*len(df_ro_2016_bi["yield.wh.g/m2"]),df_ro_2016_bi["yield.wh.g/m2"]/df_ro_2016_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="cyan", label="ro bi")
# plt.hold('on')
# plt.plot([6]*len(df_ro_2016_mo["yield.wh.g/m2"]),df_ro_2016_mo["yield.wh.g/m2"]/df_ro_2016_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="magenta", label="ro mono")
# lgd = plt.legend(bbox_to_anchor=(1.0, 1.0))
# fig.savefig('PF2016.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')

# fig = plt.figure()
# plt.title("2017")
# plt.ylim([0,0.5])
# plt.plot([1]*len(df_am_2017_bi["yield.wh.g/m2"]),df_am_2017_bi["yield.wh.g/m2"]/df_am_2017_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="blue", label="am bi")
# plt.hold('on')
# plt.plot([2]*len(df_am_2017_mo["yield.wh.g/m2"]),df_am_2017_mo["yield.wh.g/m2"]/df_am_2017_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="red", label="am mono")
# plt.plot([3]*len(df_ot_2017_bi["yield.wh.g/m2"]),df_ot_2017_bi["yield.wh.g/m2"]/df_ot_2017_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="green", label="ot bi")
# plt.hold('on')
# plt.plot([4]*len(df_ot_2017_mo["yield.wh.g/m2"]),df_ot_2017_mo["yield.wh.g/m2"]/df_ot_2017_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="black", label="ot mono")
# plt.plot([5]*len(df_ro_2017_bi["yield.wh.g/m2"]),df_ro_2017_bi["yield.wh.g/m2"]/df_ro_2017_bi["bio.wh.g/m2"], linestyle="None",marker="o",color="cyan", label="ro bi")
# plt.hold('on')
# plt.plot([6]*len(df_ro_2017_mo["yield.wh.g/m2"]),df_ro_2017_mo["yield.wh.g/m2"]/df_ro_2017_mo["bio.wh.g/m2"], linestyle="None",marker="o",color="magenta", label="ro mono")
# lgd = plt.legend(bbox_to_anchor=(1.0, 1.0))
# fig.savefig('PF2017.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')

# plt.figure()
# plt.hold('on')
# plt.title('2015')
# plt.scatter(range(len(df_am_2015)),df_am_2015["yield.wh.g/m2"], color="red",label="am")
# plt.scatt# plt.figure()
# plt.hold('on')
# plt.title('2015')
# plt.scatter(range(len(df_am_2015)),df_am_2015["yield.wh.g/m2"], color="red",label="am")
# plt.scatter(range(len(df_am_2015)),df_ot_2015["yield.wh.g/m2"], color="blue",label="ot")
# plt.scatter(range(len(df_am_2015)),df_ro_2015["yield.wh.g/m2"], color="black",label="ro")
# plt.legend()
# plt.show()
#
# plt.figure()
# plt.hold('on')
# plt.title('2016')
# plt.scatter(range(len(df_am_2016)),df_am_2016["yield.wh.g/m2"], color="red",label="am")
# plt.scatter(range(len(df_am_2016)),df_ot_2016["yield.wh.g/m2"], color="blue",label="ot")
# plt.scatter(range(len(df_am_2016)),df_ro_2016["yield.wh.g/m2"], color="black",label="ro")
# plt.legend()
# plt.show()

# plt.figure()
# plt.hold('on')
# plt.title('2017')
# plt.scatter(df_amb_2017["bio.wh.g/m2"],df_amb_2017["yield.wh.g/m2"], color="red",label="am")
# plt.scatter(df_otc_2017["bio.wh.g/m2"],df_otc_2017["yield.wh.g/m2"], color="blue",label="ot")
# plt.scatter(df_ros_2017["bio.wh.g/m2"],df_ros_2017["yield.wh.g/m2"], color="black",label="ro")
# plt.legend()
# plt.show()


print("Average relative cheatgrass in biculture under ambient conditions in 2017: ")
print(sum(df_am_2017_bi["bio.cg.g/m2"]/df_am_2017_bi["bio.wh.g/m2"])/len(df_am_2017_bi["bio.cg.g/m2"]))

print("Average relative yield in biculture under ambient conditions in 2017: ")
print(sum(df_am_2017_bi["yield.wh.g/m2"]/df_am_2017_bi["bio.wh.g/m2"])/len(df_am_2017_bi["yield.wh.g/m2"]))

print("Average relative yield in monoculture under ambient conditions in 2017: ")
print(sum(df_am_2017_mo["yield.wh.g/m2"]/df_am_2017_mo["bio.wh.g/m2"])/len(df_am_2017_mo["yield.wh.g/m2"]))

print("Average relative cheatgrass in biculture under ot conditions in 2017: ")
print(sum(df_ot_2017_bi["bio.cg.g/m2"]/df_ot_2017_bi["bio.wh.g/m2"])/len(df_ot_2017_bi["bio.cg.g/m2"]))

print("Average relative yield in biculture under ot conditions in 2017: ")
print(sum(df_ot_2017_bi["yield.wh.g/m2"]/df_ot_2017_bi["bio.wh.g/m2"])/len(df_ot_2017_bi["yield.wh.g/m2"]))

print("Average relative yield in monoculture under ot conditions in 2017: ")
print(sum(df_ot_2017_mo["yield.wh.g/m2"]/df_ot_2017_mo["bio.wh.g/m2"])/len(df_ot_2017_mo["yield.wh.g/m2"]))

print("Average relative cheatgrass in biculture under ro conditions in 2017: ")
print(sum(df_ro_2017_bi["bio.cg.g/m2"]/df_ro_2017_bi["bio.wh.g/m2"])/len(df_ro_2017_bi["bio.cg.g/m2"]))

print("Average relative yield in biculture under ro conditions in 2017: ")
print(sum(df_ro_2017_bi["yield.wh.g/m2"]/df_ro_2017_bi["bio.wh.g/m2"])/len(df_ro_2017_bi["yield.wh.g/m2"]))

print("Average relative yield in monoculture under ro conditions in 2017: ")
print(sum(df_ro_2017_mo["yield.wh.g/m2"]/df_ro_2017_mo["bio.wh.g/m2"])/len(df_ro_2017_mo["yield.wh.g/m2"]))
