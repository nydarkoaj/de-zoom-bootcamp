import sys
import pandas as pd
import pyarrow

print('arguments',sys.argv)

month = int(sys.argv[1])
print(f'pipeline month = {month}')

df = pd.DataFrame({"day": [1,2], "num_passengers":[3,5]})
df['month'] = month

print(df)

df.to_parquet(f"output_{month}.parquet")

