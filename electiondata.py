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
# analyze. Be careful about not including zeros before single-digit districts
# when working with this dataset.

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
# percentage of votes for Democratic or Republican candidates equaled zero).

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

# Write the CDrepdemcontested dataframe to a CSV file and read it into a new 
# variable.

CDrepdemcontested.to_csv('CDrepdemcontested.csv')
reppercent = pd.read_csv('CDrepdemcontested.csv')

# Read 'white.csv' into a new variable.

whitepercent = pd.read_csv('white.csv')

# Merge the reppercent and whitepercent datasets into new join dataframe using 
# a one-to-one inner join based on their shared "year" and "district" columns.
# Write join dataframe to CSV file.

join = reppercent.merge(whitepercent, 
                      on=["year","district"],
                      how='inner', 
                      validate='1:1', 
                      indicator=True)
print(len(join))
print( '\nInner:\n', join['_merge'].value_counts(), sep='' )
join.to_csv('join.csv')

#%%

# Create a Seaborn line plot from the join dataframe that displays the 
# percent of the white population in each of the selected 
# Texas congressional districts opposite the percent of the votes that went to
# Republican candidates in contested U.S. House elections from 2012 to 2018. 
# The x-axis represents the percent of the population that is white only and
# the y-axis represents the percent of votes that went to the Republican 
# congressional candidate in a given election. The legend indicates the 
# districts that correspond to each of the nine plotted lines. Save the figure 
# as 'whitevsrep.png'.

# Ensure that the 'district' column is treated as a categorical variable by
# converting the 'district' column in the join dataframe to a string data type.

join['s_district'] = join['district'].astype(str)
fig, ax = plt.subplots()
sns.lineplot(x = "w%", y = "REPpercent", data=join, hue='s_district', ax=ax)
fig.suptitle("Percent White vs % of Votes for TX Republican Candidates, 2012-2018")
ax.set_xlabel("Percent of Population that is White Only")
ax.set_ylabel("Percent of Votes for Republican Candidates")
plt.legend(title='District',loc=[1.1, 0.2])
fig.tight_layout()
fig.savefig("whitevsrep.png", dpi=300)