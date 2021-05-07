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

specificTXCDs = TXelections12_18_DR.query("district == '3' or district == '31' or district == '8' or district == '26' or district == '21' or district == '35' or district == '15' or district == '29' or district == '34' or district == '33'")

#need more analytical way to determine districts to analyze? bc rn just random

#%%
#specificTXCDs.set_index('district', inplace=True) ?


#%%  #this isn't specific to just the republican percents just yet
#don't know how to deal with only DEM or only REP candidate available for election
#do I need to eliminate them from data frame before plotting

rep = pd.DataFrame()
rep['2012'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100
rep['2014'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100
rep['2016'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100
rep['2018'] = specificTXCDs['candidatevotes']/specificTXCDs['totalvotes']*100

rep = rep.stack()
rep = rep.reset_index()
rep.columns = ['cd','year','w%']

#%%
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
sns.lineplot(x = "year", y = "%R", data=rep, hue='cd', ax=ax)
fig.suptitle("Percent of Votes for Republican Congressional Candidates in Texas Congressional Districts from 2012-2018")
ax.set_xlabel("Year")
ax.set_ylabel("Percent of Votes for Republican Congressional Candidates")
fig.tight_layout()
fig.savefig("CDpercentrepublican.png", dpi=300)



#I don't know what to do after I have both %w and %r plotted