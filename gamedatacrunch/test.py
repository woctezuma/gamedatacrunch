import pandas as pd
import json


# df = pd.DataFrame(list(dict.items()),columns = ['column1','column2']) 

f = open('C:/Users/James Schiele/Documents/GitHub/gamedatacrunch/gamedatacrunch/test_pull.json', 'r')
db = json.load(f) # dict

# print(db['ranks'][0]['steam_appid'])
# print(type(db['ranks']))

print(type(db))

list = []

for i in db['ranks']:
    list.append(i)
    print(i)

df = pd.DataFrame.from_records(list)
print(df)

test_csv = df.to_csv('testcsv.csv')