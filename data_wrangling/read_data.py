import pandas as pd
import os

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
