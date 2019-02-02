import pandas as pd
import json


df = pd.read_json('supermarkets.json')
df.loc[6] = ['asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd']
print(df)
