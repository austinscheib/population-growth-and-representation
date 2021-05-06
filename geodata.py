# -*- coding: utf-8 -*-
"""
Created on Tue May  4 04:07:32 2021

@author: austi
"""

#%%
#Use the geopandas.read_file() function to read the US zip code shapefile. 

import geopandas

zipcodes = geopandas.read_file("zip://tl_2020_us_zcta510.zip")

print(zipcodes)
print( '\nOriginal length:', len(zipcodes) )


#%%
#get zip codes that correlate to 15 fastest growing cities in America
#get percent white in 2010, 2013, 2016, 2019
#regression for each; then average the slopes for average change in white population?

#get cities 

# 







#%%

#Read in current congressional district list (will need to filter down to 435, actually will
#naturally happen when I weed out later)

cong_districts = geopandas.read_file("zip://tl_2020_us_cd116.zip")

print(cong_districts)
print( '\nOriginal length:', len(cong_districts) )


#%%
#  Now filter out the states or equivalent entities that aren't part 
#  of or near specific congressional districts I'm interested in

# need to import list of zip codes I'm interested in?


po_notcon = ['AK','AS','GU','HI','MP','PR','VI']

is_conus = states['STUSPS'].isin(po_notcon) == False

conus = states[ is_conus ]

print( '\nFiltered length:', len(conus) )