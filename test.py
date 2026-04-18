import pandas as pd
import os

df = pd.DataFrame([{'a': None}, {'a':'a'}, {'a':''}, {'a':None}, {'a':'f'}])#, columns=['a'])
df['b'] = df['a'].ffill()
print(df)