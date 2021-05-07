# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:42:37 2021

@author: austi
"""

import pandas as pd

fix_dtype = {'year':str,'state':str,'district':str,'party':str,'candidatevotes':float,
            'totalvotes':float}
electionresults = pd.read_csv('1976-2018-house3.csv', dtype = fix_dtype)

election12_18 = electionresults.query("year == '2012' or year == '2014' or year == '2016' or year == '2018'")

TXelections12_18 = election12_18.query("state == 'TEXAS'")

TXelections12_18_DR = TXelections12_18.query("party == 'DEMOCRAT' or party == 'REPUBLICAN'")

districts = ['3','26','33','31','35','27','8','29']
in_districts = TXelections12_18_DR['district'].isin(districts)

specificTXCDs = TXelections12_18_DR[in_districts]

#%%
#need more analytical way to determine districts to analyze?? bc rn just random. can just do case study
CDrep = pd.DataFrame()
CDrep['year'] = specificTXCDs['year']
CDrep['district'] = specificTXCDs['district']
CDrep['party'] = specificTXCDs['party']
CDrep['candidatevotes'] = specificTXCDs['candidatevotes']

CDrep = CDrep.set_index(['year','district','party'])
CDrep = CDrep.unstack() 
CDrep.fillna(0, inplace=True)
CDrep = CDrep['candidatevotes']

CDrep['totalvotes'] = CDrep.sum(axis='columns')
CDrep['REPpercent'] = 100 * CDrep['REPUBLICAN'] / CDrep['totalvotes']
CDrep['DEMpercent'] = 100 * CDrep['DEMOCRAT']/ CDrep['totalvotes']

CDrep['electedREP'] = CDrep['REPUBLICAN'] > CDrep['DEMOCRAT']

#%%

#margin of victory; build lil dataframe CDrep drop where REP = 0 and where DEM = 0
#CDrep.dropna() ??
#CDrep query (rep greater than 0 and vice versa)


#fillna (victory margin, tell who won, tell who was uncontested)
#take data frame and drop uncontested elections
#y = x.fillna 0
#dropna

#contested_vs_uncontested = specificTXCDs.groupby(['year','district']).size()

#contested_vs_uncontested['rep2012'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100
#FIX !!

#%%
#this isn't specific to just the republican percents just yet
#don't know how to deal with only DEM or only REP candidate available for election
#do I need to eliminate them from data frame before plotting

#rep = pd.DataFrame()
#rep['2012'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100
#rep['2014'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100
#rep['2016'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100
#rep['2018'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100

#rep = rep.stack()
#rep = rep.reset_index()
#rep.columns = ['cd','year','%rep']

#%%
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
sns.lineplot(x = "year", y = "%rep", data=rep, hue='cd', ax=ax)
fig.suptitle("Percent of Votes for Republican Congressional Candidates in Texas Congressional Districts from 2012-2018")
ax.set_xlabel("Year")
ax.set_ylabel("Percent of Votes for Republican Congressional Candidates")
fig.tight_layout()
fig.savefig("CDpercentrepublican.png", dpi=300)


#shorten title or get them formatted differently.
#I don't know what to do after I have both %w and %r plotted