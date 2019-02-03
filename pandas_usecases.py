import pandas as pd
import json


df = pd.read_json('supermarkets.json')
df.loc[df.shape[0]] = ['asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd']
df.loc[df.shape[0]] = ['asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd']
print(df)
