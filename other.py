# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:13:49 2021

@author: austi
"""
#%%
#specificTXCDs.set_index('district', inplace=True) ??

#ax.get_legend().remove()


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