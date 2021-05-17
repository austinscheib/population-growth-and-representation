# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:00:39 2021

@author: austi
"""

# Import pandas as pd.

import pandas as pd

# Set the variable dtype_CD to a dictionary using the column name 
# 'congressional district' as a key with a value for the string data type 
# (str). This will tell Pandas to load data in string form.

dtype_CD = {'congressional district':str}

# Read the Texas congressional districts' yearly white percentage data. Create
# dataframes with variable names identifying corresponding years and call
# pd.read_csv() on the different yearly CSV files with the argument 
# dtype=dtype_DC.

CDpercentwhite2012 = pd.read_csv('CDpercentwhite2012.csv', dtype=dtype_CD)
CDpercentwhite2013 = pd.read_csv('CDpercentwhite2013.csv', dtype=dtype_CD)
CDpercentwhite2014 = pd.read_csv('CDpercentwhite2014.csv', dtype=dtype_CD)
CDpercentwhite2015 = pd.read_csv('CDpercentwhite2015.csv', dtype=dtype_CD)
CDpercentwhite2016 = pd.read_csv('CDpercentwhite2016.csv', dtype=dtype_CD)
CDpercentwhite2017 = pd.read_csv('CDpercentwhite2017.csv', dtype=dtype_CD)
CDpercentwhite2018 = pd.read_csv('CDpercentwhite2018.csv', dtype=dtype_CD)
CDpercentwhite2019 = pd.read_csv('CDpercentwhite2019.csv', dtype=dtype_CD)

# Set the index of each dataframe to the column "congressional district" with
# the inplace=True parameter to make change and overwrite existing dataframe.

CDpercentwhite2012.set_index('congressional district', inplace=True)
CDpercentwhite2013.set_index('congressional district', inplace=True)
CDpercentwhite2014.set_index('congressional district', inplace=True)
CDpercentwhite2015.set_index('congressional district', inplace=True)
CDpercentwhite2016.set_index('congressional district', inplace=True)
CDpercentwhite2017.set_index('congressional district', inplace=True)
CDpercentwhite2018.set_index('congressional district', inplace=True)
CDpercentwhite2019.set_index('congressional district', inplace=True)

# Create new dataframe with percentages of population that were white in the 
# Texas congressional districts for each year from 2012 to 2019. Set white
# equal to the pd.DataFrame() function.

white = pd.DataFrame()

# Create new columns in the white dataframe labeled by year that pull the 
# 'percent_white' columns from each of the eight dataframes above (from
# CDpercentwhite2012 to CDpercentwhite2019).

white['2012'] = CDpercentwhite2012['percent_white']
white['2013'] = CDpercentwhite2013['percent_white']
white['2014'] = CDpercentwhite2014['percent_white']
white['2015'] = CDpercentwhite2015['percent_white']
white['2016'] = CDpercentwhite2016['percent_white']
white['2017'] = CDpercentwhite2017['percent_white']
white['2018'] = CDpercentwhite2018['percent_white']
white['2019'] = CDpercentwhite2019['percent_white']

# Stack the white dataframe, reset its index, and set the columns of the 
# dataframe to 'district', 'year', and 'w%' (a shorter name for the column
# containing the percentages of the districts that are white only).

white = white.stack()
white = white.reset_index()
white.columns = ['district','year','w%']

# Select specific congressional districts to analyze. Be careful with zeros 
# before single-digit districts.

districts = ['03','26','32','31','35','27','08','18','14']
in_districts = white['district'].isin(districts)
white = white[in_districts]

# Write white dataframe to CSV file called 'white.csv'.

white.to_csv('white.csv')

#%%

# Import matplotlib.pyplot as plt and seaborn as sns.

import matplotlib.pyplot as plt
import seaborn as sns

# Create a Seaborn line plot from the white dataframe that displays the 
# changes in the percent of the white population in each of the selected 
# Texas congressional districts from 2012 to 2019. The x-axis represents the 
# year and the y-axis represents the percent of the white-only population.
# The legend indicates the districts that correspond to each of the nine
# plotted lines. Save the figure as 'CDpercentwhite.png'.

fig, ax = plt.subplots()
sns.lineplot(x = "year", y = "w%", data=white, hue='district',ax=ax)
fig.suptitle("White Percent of Population in TX Congressional Districts, 2012-2019")
ax.set_xlabel("Year")
ax.set_ylabel("Percent of White-Only Population")
plt.legend(title='District',loc=[1.1, 0.2])
fig.tight_layout()
fig.savefig("CDpercentwhite.png", dpi=300)