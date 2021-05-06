# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:00:39 2021

@author: austi
"""

import pandas as pd

CDpercentwhite2012 = pd.read_csv('CDpercentwhite2012.csv')
CDpercentwhite2013 = pd.read_csv('CDpercentwhite2013.csv')
CDpercentwhite2014 = pd.read_csv('CDpercentwhite2014.csv')
CDpercentwhite2015 = pd.read_csv('CDpercentwhite2015.csv')
CDpercentwhite2016 = pd.read_csv('CDpercentwhite2016.csv')
CDpercentwhite2017 = pd.read_csv('CDpercentwhite2017.csv')
CDpercentwhite2018 = pd.read_csv('CDpercentwhite2018.csv')
CDpercentwhite2019 = pd.read_csv('CDpercentwhite2019.csv')

#set index?
#white2012.set_index('congressional district')

# Add percent of population that was white in the congressional districts in each year
CDpercentwhite2012['white2013'] = CDpercentwhite2013['percent_white']
CDpercentwhite2012['white2014'] = CDpercentwhite2014['percent_white']
CDpercentwhite2012['white2015'] = CDpercentwhite2015['percent_white']
CDpercentwhite2012['white2016'] = CDpercentwhite2016['percent_white']
CDpercentwhite2012['white2017'] = CDpercentwhite2017['percent_white']
CDpercentwhite2012['white2018'] = CDpercentwhite2018['percent_white']
CDpercentwhite2012['white2019'] = CDpercentwhite2019['percent_white']

#drop other columns?

#%%

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
fig.suptitle("Percent of Population that is White in Texas Congressional Districts")
ax1.set_xlabel("Year")
ax1.set_ylabel("White Percent of Population")
fig.tight_layout()
fig.savefig("CDpercentwhite.png", dpi=300)