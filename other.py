# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:13:49 2021

@author: austi
"""
#%%
#specificTXCDs.set_index('district', inplace=True) ??

#ax.get_legend().remove()

#from racedatajoin import white
#white.to_csv('white.csv')

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
#%%
cd = {'congressional district':str}
race12 = pd.read_csv("percent_whiteCDs12.csv",dtype=cd)

race12 = race12.set_index(['congressional district'])

#  Sort the congressional districts by number
race12 = race12.sort_values('congressional district')


race14 = pd.read_csv("percent_whiteCDs14.csv")

race14 = race14.merge(race12,left_on='percent_white',right_on='percent_white',how='inner',validate='1:1',indicator=True)

print(race14['_merge'].value_counts())

#fh.open ?
#DataFrame = ... .csv
#read csv

#%%

pct_by_bin[bars].plot.bar(ax=ax1)

#%%

pop = pd.DataFrame(columns = colnames, data = datarows)

new_names = pop.rename( {"B01001_001E":"pop", "zip code tabulation area":"zip"}, axis='columns')

new_names = new_names.set_index("zip")
new_names.to_csv("pop.csv")

percent_white = percent_white.set_index("congressional district")
#%%
trim = trim.drop("_merge", axis='columns') 