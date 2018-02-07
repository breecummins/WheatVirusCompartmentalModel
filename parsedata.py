import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(os.path.expanduser("~/Downloads/PF_All_Yield_Bio_Den_Cov_Ht.csv"))
df_am_2015 = df.loc[(df['year']==2015) & (df['climt']=='am') & (df['spp']=='wh')]
df_ot_2015 = df.loc[(df['year']==2015) & (df['climt']=='ot') & (df['spp']=='wh')]
df_ro_2015 = df.loc[(df['year']==2015) & (df['climt']=='ro') & (df['spp']=='wh')]


# for z in zip(df_am_2015["yield.wh.g/m2"],df_am_2015["pcntcov.wh"],df_am_2015["bio.wh.g/m2"]):
#     print(z)

# plt.scatter(df_am_2015["bio.wh.g/m2"],df_am_2015["yield.wh.g/m2"])
# plt.show()
#
# plt.scatter(df_am_2015["pcntcov.wh"],df_am_2015["yield.wh.g/m2"])
# plt.show()

df_am_2016 = df.loc[(df['year']==2016) & (df['climt']=='am') & (df['spp']=='wh')]
df_amb_2017 = df.loc[(df['year']==2017) & (df['climt']=='amb') & (df['spp']=='wh')]
df_ot_2016 = df.loc[(df['year']==2016) & (df['climt']=='ot') & (df['spp']=='wh')]
df_otc_2017 = df.loc[(df['year']==2017) & (df['climt']=='otc') & (df['spp']=='wh')]
df_ro_2016 = df.loc[(df['year']==2016) & (df['climt']=='ro') & (df['spp']=='wh')]
df_ros_2017 = df.loc[(df['year']==2017) & (df['climt']=='ros') & (df['spp']=='wh')]

# plt.figure()
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

plt.figure()
plt.hold('on')
plt.title('2017')
plt.scatter(df_amb_2017["bio.wh.g/m2"],df_amb_2017["yield.wh.g/m2"], color="red",label="am")
plt.scatter(df_otc_2017["bio.wh.g/m2"],df_otc_2017["yield.wh.g/m2"], color="blue",label="ot")
plt.scatter(df_ros_2017["bio.wh.g/m2"],df_ros_2017["yield.wh.g/m2"], color="black",label="ro")
plt.legend()
plt.show()

