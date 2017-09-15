import pandas as pd
import math

def mean_std(L):
    m = sum(L)/len(L)
    v = math.sqrt(sum( [(l-m)**2 for l in L] ) / ( len(L)-1 ))
    return m,v

def split_by_climate(L):
    amb,hot,hot_dry = [],[],[]
    for (c,w) in zip(climate,L):
        if w != 0:
            if c =="am":
                amb.append(w)
            elif c=="ot":
                hot.append(w)
            else:
                hot_dry.append(w)
    print("Ambient: # datapoints, mean, std {}".format((len(amb),mean_std(amb))))
    print("Hot: # datapoints, mean, std {}".format((len(hot),mean_std(hot))))
    print("Hot/Dry: # datapoints, mean, std {}".format((len(hot_dry),mean_std(hot_dry))))


df = pd.read_csv("/Users/bcummins/ProjectData/cheatgrass/pf_whyld_bio_both.csv")
# print(len(df))
df = df[df.seedmass_wh.notnull()] # N/A data
# print(len(df))
wsmv = list(df.loc[:,"wsmv"])
print(wsmv)
wheat_seedmass = list(df.loc[:,"seedmass_wh"])
yield_loss = list(df.loc[:,"yield_loss_pct"])
cheatgrass_biomass = list(df.loc[:,"bio_cg"])
climate = df.loc[:,"climt"]

wheat_sm_lowcg = [ (c<100)*w for (c,w) in zip(cheatgrass_biomass,wheat_seedmass) ]
wheat_sm_highcg = [ (c>=100)*w for (c,w) in zip(cheatgrass_biomass,wheat_seedmass) ]

wheat_sm_nowsmv_lowcg = [ (1-v)*(c<100)*w for (v,c,w) in zip(wsmv,cheatgrass_biomass,wheat_seedmass) ]
wheat_sm_nowsmv_highcg = [ (1-v)*(c>=100)*w for (v,c,w) in zip(wsmv,cheatgrass_biomass,wheat_seedmass) ]
wheat_sm_wsmv_lowcg = [ v*(c<100)*w for (v,c,w) in zip(wsmv,cheatgrass_biomass,wheat_seedmass) ]
wheat_sm_wsmv_highcg = [ v*(c>=100)*w for (v,c,w) in zip(wsmv,cheatgrass_biomass,wheat_seedmass) ]

print("---------------------------------------------------------------")
print("Avg and std of wheat seedmass with low cheatgrass")
print("---------------------------------------------------------------")
split_by_climate(wheat_sm_lowcg)
print("---------------------------------------------------------------")
print("Avg and std of wheat seedmass with no virus and low cheat grass")
print("---------------------------------------------------------------")
split_by_climate(wheat_sm_nowsmv_lowcg)
print("---------------------------------------------------------------")
print("Avg and std of wheat seedmass with virus and low cheat grass")
print("---------------------------------------------------------------")
split_by_climate(wheat_sm_wsmv_lowcg)
print("---------------------------------------------------------------")
print("Avg and std of wheat seedmass with high cheatgrass")
print("---------------------------------------------------------------")
split_by_climate(wheat_sm_highcg)
print("---------------------------------------------------------------")
print("Avg and std of wheat seedmass with no virus and high cheat grass")
print("---------------------------------------------------------------")
split_by_climate(wheat_sm_nowsmv_highcg)
print("---------------------------------------------------------------")
print("Avg and std of wheat seedmass with virus and high cheat grass")
print("---------------------------------------------------------------")
split_by_climate(wheat_sm_wsmv_highcg)
print("---------------------------------------------------------------")


