# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:48:37 2021

@author: austi
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api = 'https://api.census.gov/data/2018/acs/acs5'

for_clause = 'zip code tabulation area:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E", 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.txt)
    assert False

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]
#%%
percent_white = pd.DataFrame(columns = colnames, data = datarows)
earnings['GEOID'] = earnings['state'] + earnings['county'] 
percent_white["median"] = percent_white["C02003_003E"].astype(float)
percent_white.to_csv('percent_white.csv', index=False)

#%%
#
#  Read the shapefile
#

states = geopandas.read_file("zip://tl_2019_us_state.zip")

print( '\nOriginal length:', len(states) )

#
#  Now filter out the states or equivalent entities that aren't part 
#  of the contiguous (or conterminous) US
#

po_notcon = ['AK','AS','GU','HI','MP','PR','VI']

is_conus = states['STUSPS'].isin(po_notcon) == False

conus = states[ is_conus ]

print( '\nFiltered length:', len(conus) )