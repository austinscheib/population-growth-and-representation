# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:48:46 2021

@author: austi
"""

# Import requests and pandas as pd.

import requests
import pandas as pd

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2012.

api = 'https://api.census.gov/data/2012/acs/acs5'

# Set the variable for_clause to 'congressional district:*'

for_clause = 'congressional district:*'

# Set the variable in_clause to 'state:48' since Texas' FIPS code is 48.

in_clause = 'state:48' 

# Set the variable key_value to the Census API you are given in quotes.

key_value = 'ed474d261838d3b77d2f80d5678b76e0b83c4982'

# Set the variable payload to a dictionary with these keys and values because
# they set the parameters for the data request:
# 'get':"NAME,C02003_003E,C02003_001E" 
#       C02003_003E: variable corresponding to the estimate of the total 
#       population of one race (white)
#       C02003_001E: variable corresponding to the estimate of the total 
#       population
# 'for':for_clause
# 'in':in_clause
# 'key':key_value

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}

# Set the variable response to the call requests.get() with the arguments api
# and payload to collect the response of the census query.

response = requests.get(api, payload)

# Set up if and else statements to see if the census request succeeded.

if response.status_code == 200:
    print('Request succeeded')
else:
    print(response.status_code, response.txt)
    assert False

# Set the variable row_list to the call of .json() on the response variable to
# transform JSON returned by Census server into a list of rows. To organize 
# the coming dataframe, set the variable colnames to the first row of row_list
# and set the variable datarows to the remaining rows of row_list.

row_list = response.json() 
colnames = row_list[0]
datarows = row_list[1:]

# Convert the data into a dataframe. Set the variable percent_white to the
# pd.DataFrame() call with the arguments columns=colnames and data=datarows.

percent_white = pd.DataFrame(columns = colnames, data = datarows)

# Create new column "num_white" in percent_white and set it equal to the 
# "C02003_003E" column of percent_white, and then cast the pandas objects to 
# a float data type with .astype() method.

percent_white["num_white"] = percent_white["C02003_003E"].astype(float)

# Create new column "total" in percent_white and set it equal to the 
# "C02003_001E" column of percent_white, and then cast the pandas objects to 
# a float data type with .astype() method.

percent_white["total"] =  percent_white["C02003_001E"].astype(float)

# Create new column "percent_white" in percent_white and set it equal to  
# dividing the "num_white" column of percent_white by the "total" column of
# percent_white, followed by multiplying the quotient by 100.

percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write your percent_white pandas DataFrame to a CSV file using the .to_csv() 
# method on percent_white to a file called 'CDpercentwhite2012.csv'.

percent_white.to_csv('CDpercentwhite2012.csv', index=False)

#%%

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2013.

api = 'https://api.census.gov/data/2013/acs/acs5'

# Follow the remaining steps as described above for the 2012 year.

for_clause = 'congressional district:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}
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
percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write percent_white to a file called 'CDpercentwhite2013.csv'.

percent_white.to_csv('CDpercentwhite2013.csv', index=False)

#%%

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2014.

api = 'https://api.census.gov/data/2014/acs/acs5'

# Follow the remaining steps as described above for the 2012 year.

for_clause = 'congressional district:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}
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
percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write percent_white to a file called 'CDpercentwhite2014.csv'.

percent_white.to_csv('CDpercentwhite2014.csv', index=False)

#%%

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2015.

api = 'https://api.census.gov/data/2015/acs/acs5'

# Follow the remaining steps as described above for the 2012 year.

for_clause = 'congressional district:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}
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
percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write percent_white to a file called 'CDpercentwhite2015.csv'.

percent_white.to_csv('CDpercentwhite2015.csv', index=False)

#%%

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2016.

api = 'https://api.census.gov/data/2016/acs/acs5'

# Follow the remaining steps as described above for the 2012 year.

for_clause = 'congressional district:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}
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
percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write percent_white to a file called 'CDpercentwhite2016.csv'.

percent_white.to_csv('CDpercentwhite2016.csv', index=False)

#%%

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2017.

api = 'https://api.census.gov/data/2017/acs/acs5'

# Follow the remaining steps as described above for the 2012 year.

for_clause = 'congressional district:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}
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
percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write percent_white to a file called 'CDpercentwhite2017.csv'.

percent_white.to_csv('CDpercentwhite2017.csv', index=False)

#%%

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2018.

api = 'https://api.census.gov/data/2018/acs/acs5'

# Follow the remaining steps as described above for the 2012 year.

for_clause = 'congressional district:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}
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
percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write percent_white to a file called 'CDpercentwhite2018.csv'.

percent_white.to_csv('CDpercentwhite2018.csv', index=False)

#%%

# Set the variable api to the American Community Survey 5-Year estimate 
# endpoint for the year 2019.

api = 'https://api.census.gov/data/2019/acs/acs5'

# Follow the remaining steps as described above for the 2012 year.

for_clause = 'congressional district:*'
in_clause = 'state:48' 
key_value = "ed474d261838d3b77d2f80d5678b76e0b83c4982"

payload = {'get':"NAME,C02003_003E,C02003_001E", 
           'for':for_clause, 
           'in':in_clause, 
           'key':key_value}
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
percent_white["percent_white"]=percent_white["num_white"]/percent_white["total"]*100

# Write percent_white to a file called 'CDpercentwhite2019.csv'.

percent_white.to_csv('CDpercentwhite2019.csv', index=False)