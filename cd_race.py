# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:48:46 2021

@author: austi
"""

import requests
import pandas as pd

api = 'https://api.census.gov/data/2012/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2012.csv', index=False)

#%%

api = 'https://api.census.gov/data/2013/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2013.csv', index=False)

#%%
api = 'https://api.census.gov/data/2014/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2014.csv', index=False)

#%%
api = 'https://api.census.gov/data/2015/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2015.csv', index=False)

#%%
api = 'https://api.census.gov/data/2016/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2016.csv', index=False)

#%%
api = 'https://api.census.gov/data/2017/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2017.csv', index=False)

#%%
api = 'https://api.census.gov/data/2018/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2018.csv', index=False)

#%%
api = 'https://api.census.gov/data/2019/acs/acs5'

for_clause = 'congressional district:*'
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
percent_white.to_csv('CDpercentwhite2019.csv', index=False)