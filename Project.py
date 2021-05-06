# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:48:37 2021

@author: austi
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api = 'https://api.census.gov/data/2019/acs/acs5'

for_clause = 'zip code tabulation area:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.txt)
    assert False

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]

percent_white = pd.DataFrame(columns = colnames, data = datarows)
percent_white["num_white"] = percent_white["C02003_003E"].astype(float)
percent_white["total"] =  percent_white["C02003_001E"].astype(float)
percent_white["percent_white"] = percent_white["num_white"] / percent_white["total"] * 100
percent_white.to_csv('percent_white19.csv', index=False)

#%%
api = 'https://api.census.gov/data/2017/acs/acs5'

for_clause = 'zip code tabulation area:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.txt)
    assert False

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]

percent_white = pd.DataFrame(columns = colnames, data = datarows)
percent_white["num_white"] = percent_white["C02003_003E"].astype(float)
percent_white["total"] =  percent_white["C02003_001E"].astype(float)
percent_white["percent_white"] = percent_white["num_white"] / percent_white["total"] * 100
percent_white.to_csv('percent_white17.csv', index=False)

#%%
api = 'https://api.census.gov/data/2015/acs/acs5'

for_clause = 'zip code tabulation area:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.txt)
    assert False

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]

percent_white = pd.DataFrame(columns = colnames, data = datarows)
percent_white["num_white"] = percent_white["C02003_003E"].astype(float)
percent_white["total"] =  percent_white["C02003_001E"].astype(float)
percent_white["percent_white"] = percent_white["num_white"] / percent_white["total"] * 100
percent_white.to_csv('percent_white15.csv', index=False)

#%%
api = 'https://api.census.gov/data/2013/acs/acs5'

for_clause = 'zip code tabulation area:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.txt)
    assert False

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]

percent_white = pd.DataFrame(columns = colnames, data = datarows)
percent_white["num_white"] = percent_white["C02003_003E"].astype(float)
percent_white["total"] =  percent_white["C02003_001E"].astype(float)
percent_white["percent_white"] = percent_white["num_white"] / percent_white["total"] * 100
percent_white.to_csv('percent_white13.csv', index=False)

#%%
api = 'https://api.census.gov/data/2011/acs/acs5'

for_clause = 'zip code tabulation area:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.txt)
    assert False

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]

percent_white = pd.DataFrame(columns = colnames, data = datarows)
percent_white["num_white"] = percent_white["C02003_003E"].astype(float)
percent_white["total"] =  percent_white["C02003_001E"].astype(float)
percent_white["percent_white"] = percent_white["num_white"] / percent_white["total"] * 100
percent_white.to_csv('percent_white11.csv', index=False)

#%%


#dataframe.query()