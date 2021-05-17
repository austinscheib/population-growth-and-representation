# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:42:37 2021

@author: austi
"""

# Import pandas as pd.

import pandas as pd

# Set data types for specific columns by setting the variable fix_dtype to a 
# dictionary with column names as keys and data types as values.

fix_dtype = {'year':str,
             'state':str,
             'district':str,
             'party':str,
             'candidatevotes':float,
             'totalvotes':float}

# Read CSV file containing 1976 to 2018 U.S. House election data from MIT 
# Election Data and Science Lab after you have downloaded it. 

electionresults = pd.read_csv('1976-2018-house3.csv', dtype = fix_dtype)

# Filter the data down to only the 2012, 2014, 2016, and 2018 elections in 
# Texas. Further filter that data down to only Republican and Democrat
# congressional candidates.

election12_18 = electionresults.query("year == '2012' or year == '2014' or year == '2016' or year == '2018'")
TXelections12_18 = election12_18.query("state == 'TEXAS'")
TXelections12_18_DR = TXelections12_18.query("party == 'DEMOCRAT' or party == 'REPUBLICAN'")

# Filter that data down to the specific congressional districts you want to
# analyze.

districts = ['3','26','32','31','35','27','8','18','14']
in_districts = TXelections12_18_DR['district'].isin(districts)
specificTXCDs = TXelections12_18_DR[in_districts]

#%%

# Create a new dataframe containing the year, the district, the number of 
# votes per political party, the total number of votes per election, the 
# percent of the votes for Republican candidates, the percent of the votes
# for Democratic candidates, and the party in control of the seat after the
# election. Set CDrep equal to the pd.DataFrame() function.

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

# Import matplotlib.pyplot as plt and seaborn as sns.

import matplotlib.pyplot as plt
import seaborn as sns

# Create a Seaborn line plot from the CDrep dataframe that displays the 
# percentage of the votes for the Republican congressional candidates in each 
# of the nine Texas congressional districts' U.S. House elections from 2012 to 
# 2018. The x-axis represents the year and the y-axis represents the percent 
# of the votes that went to the Republican candidate. The legend indicates the 
# districts that correspond to each of the nine plotted lines. Save the figure 
# as 'CDpercentrepublican.png'.

fig, ax = plt.subplots()
sns.lineplot(x = "year", y = "REPpercent", data=CDrep, hue='district', ax=ax)
fig.suptitle("Percent of Votes for TX Republican U.S. House Candidates, 2012-2018")
ax.set_xlabel("Year")
ax.set_ylabel("Percent of Votes for Republican Candidates")
plt.legend(title='District',loc=[1.1, 0.2])
fig.tight_layout()
fig.savefig("CDpercentrepublican.png", dpi=300)

#%%

# Query the CDrep dataframe to filter out the uncontested elections (where the 
# percentage of votes for Democratic or Republican candidates equalled zero).

CDrepcontested = CDrep.query("REPpercent != 0")
CDrepdemcontested = CDrepcontested.query("DEMpercent != 0")

#%%

# Create a Seaborn line plot from the CDrepdemcontested dataframe that 
# displays the percentage of the votes for the Republican congressional 
# candidates in only the contested U.S. House elections (where both Democratic 
# and Republican candidates ran for public office). The x-axis still represents 
# the year and the y-axis represents the percent of the votes that went to the 
# Republican candidate. The legend indicates the districts that correspond to 
# each of the nine plotted lines. Save the figure as
# 'CDpercentrepcontested.png'.

fig, ax = plt.subplots()
sns.lineplot(x = "year", y = "REPpercent", data=CDrepdemcontested, hue='district', ax=ax)
fig.suptitle("Votes for TX Republican U.S. House Candidates in Contested Elections")
ax.set_xlabel("Year")
ax.set_ylabel("Percent of Votes for Republican Candidates")
plt.legend(title='District',loc=[1.1, 0.2])
fig.tight_layout()
fig.savefig("CDpercentrepcontested.png", dpi=300)

#%%

# Write the CDrepdemcontested dataframe to CSV file. and read them into new variables


CDrepdemcontested.to_csv('CDrepdemcontested.csv')

reppercent = pd.read_csv('CDrepdemcontested.csv')
whitepercent = pd.read_csv('white.csv')

#  Inner join whitepercent onto reppercent to get only records in both
# Merge the two datasets using a one-to-one inner join based on their shared
# "year" and "district" columns

join = reppercent.merge(whitepercent, 
                      on=["year","district"],
                      how='inner', 
                      validate='1:1', 
                      indicator=True)
print(len(join))
print( '\nInner:\n', join['_merge'].value_counts(), sep='' )
join.to_csv('join.csv')

#%%

# Create a Seaborn line plot from the white dataframe that displays the 
# changes in the percent of the white population in each of the selected 
# Texas congressional districts from 2012 to 2019. The x-axis represents the 
# year and the y-axis represents the percent of the white-only population.
# The legend indicates the districts that corresond to each of the nine
# plotted lines. Save the figure as 'CDpercentwhite.png'.

join['s_district'] = join['district'].astype(str)
fig, ax = plt.subplots()
sns.lineplot(x = "w%", y = "REPpercent", data=join, hue='s_district', ax=ax)
fig.suptitle("Percent White vs % of Votes for TX Republican Candidates, 2012-2018")
ax.set_xlabel("Percent of Population that is White Only")
ax.set_ylabel("Percent of Votes for Republican Candidates")
plt.legend(title='District',loc=[1.1, 0.2])
fig.tight_layout()
fig.savefig("whitevsrep.png", dpi=300)

#%%

# Create new column in join dataframe for margins of victory

join['MoV'] = join['REPpercent'] - join['DEMpercent']


# Create a Seaborn line plot from the white dataframe that displays the 
# changes in the percent of the white population in each of the selected 
# Texas congressional districts from 2012 to 2019. The x-axis represents the 
# year and the y-axis represents the percent of the white-only population.
# The legend indicates the districts that corresond to each of the nine
# plotted lines. Save the figure as 'CDpercentwhite.png'.


fig, ax = plt.subplots()
sns.lineplot(x = "year", y = "MoV", data=join, hue='s_district', ax=ax)
fig.suptitle("Margins of Victory in Texas Congressional Districts, 2012-2018")
ax.set_xlabel("Year of Election")
ax.set_ylabel("Margin of Victory")
plt.legend(title='District',loc=[1.1, 0.2])
fig.tight_layout()
fig.savefig("marginsofvictory.png", dpi=300)

#%%

# Query to get only districts where Republicans won

#republicanwon = join.query("REPpercent != 0")



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

#I don't know what to do after I have both %w and %r plotted