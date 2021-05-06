# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:17:56 2021

@author: austi
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api = 'https://api.census.gov/data/2019/acs/acs5/geography'

#state› consolidated city
#"place:XXX", "consolidated city:XXX"

for_clause = "consolidated city:27684 " #what is Frisco's code
in_clause = "state:48"
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 'for':for_clause, 'in':in_clause, 'key':key_value}
response = requests.get(api, payload)

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.text)
    assert False

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]


#%%

The key is the "geography hierarchy" column: the thing at the end 
(say "county", "tract", "place") shows what you can put in the "for" 
clause and the part to the left of that shows what you can use for the "in" 
clause. In your case, you might use "place:XXX", "consolidated city:XXX" or 
"combined statistical area (or part):XXX" for the for clause and "state:48" 
for the "in" clause where XXX is the FIPS code for the place. There are a lot 
of other options as well that could be even better. In any case, it would be a 
lot simpler than aggregating up the zip codes.

One other thing: you can ask for multiple items in the for clause. For example, 
"place:XXX,YYY". That would let you set it up as just a couple of requests.
#%%
percent_white = pd.DataFrame(columns = colnames, data = datarows)
percent_white["num_white"] = percent_white["C02003_003E"].astype(float)
percent_white["total"] =  percent_white["C02003_001E"].astype(float)
percent_white["percent_white"] = percent_white["num_white"] / percent_white["total"] * 100
percent_white.to_csv('percent_white.csv', index=False)