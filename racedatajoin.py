# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:00:39 2021

@author: austi
"""

import pandas as pd

dtype_CD = {'congressional district':str}

CDpercentwhite2012 = pd.read_csv('CDpercentwhite2012.csv', dtype=dtype_CD)
CDpercentwhite2013 = pd.read_csv('CDpercentwhite2013.csv', dtype=dtype_CD)
CDpercentwhite2014 = pd.read_csv('CDpercentwhite2014.csv', dtype=dtype_CD)
CDpercentwhite2015 = pd.read_csv('CDpercentwhite2015.csv', dtype=dtype_CD)
CDpercentwhite2016 = pd.read_csv('CDpercentwhite2016.csv', dtype=dtype_CD)
CDpercentwhite2017 = pd.read_csv('CDpercentwhite2017.csv', dtype=dtype_CD)
CDpercentwhite2018 = pd.read_csv('CDpercentwhite2018.csv', dtype=dtype_CD)
CDpercentwhite2019 = pd.read_csv('CDpercentwhite2019.csv', dtype=dtype_CD)

CDpercentwhite2012.set_index('congressional district', inplace=True)
CDpercentwhite2013.set_index('congressional district', inplace=True)
CDpercentwhite2014.set_index('congressional district', inplace=True)
CDpercentwhite2015.set_index('congressional district', inplace=True)
CDpercentwhite2016.set_index('congressional district', inplace=True)
CDpercentwhite2017.set_index('congressional district', inplace=True)
CDpercentwhite2018.set_index('congressional district', inplace=True)
CDpercentwhite2019.set_index('congressional district', inplace=True)

# Create dataframe with percentages of population that were white in the 
# congressional districts in each year.

white = pd.DataFrame()
white['2012'] = CDpercentwhite2012['percent_white']
white['2013'] = CDpercentwhite2013['percent_white']
white['2014'] = CDpercentwhite2014['percent_white']
white['2015'] = CDpercentwhite2015['percent_white']
white['2016'] = CDpercentwhite2016['percent_white']
white['2017'] = CDpercentwhite2017['percent_white']
white['2018'] = CDpercentwhite2018['percent_white']
white['2019'] = CDpercentwhite2019['percent_white']

white = white.stack()
white = white.reset_index()
white.columns = ['district','year','w%']

districts = ['03','26','32','31','35','27','08','18','14']
in_districts = white['district'].isin(districts)

white = white[in_districts]
#put plotting data in separate script
#save new dataframe with just selected CDs to csv

#CDpercentwhite2012['white2014'] = CDpercentwhite2014['percent_white']
#CDpercentwhite2012['white2015'] = CDpercentwhite2015['percent_white']
#CDpercentwhite2012['white2016'] = CDpercentwhite2016['percent_white']
#CDpercentwhite2012['white2017'] = CDpercentwhite2017['percent_white']
#CDpercentwhite2012['white2018'] = CDpercentwhite2018['percent_white']
#CDpercentwhite2012['white2019'] = CDpercentwhite2019['percent_white']


#which congressional districts do I want to select?

#%%

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
sns.lineplot(x = "year", y = "w%", data=white, hue='district',ax=ax)
fig.suptitle("White Percent of Population in TX Congressional Districts, 2012-2019")
ax.set_xlabel("Year")
ax.set_ylabel("Percent of White-Only Population")
#ax.get_legend().remove()
plt.legend(title='District',loc=[1.1, 0.2])
fig.tight_layout()
fig.savefig("CDpercentwhite.png", dpi=300)

#drop legend
#plot only my selected congressional districts