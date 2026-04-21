import pandas as pd
import os

df = pd.DataFrame([{'a': 'a', 'b': 1}, {'a':'aa', 'b': 'bb'}])
df['c'] = df[['a', 'b']].astype(str).agg(' '.join, axis=1)

print(df)