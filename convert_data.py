import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

CSV_PATH = 'data/cancelamentos.csv'
PARQUET_PATH = 'data/cancelamentos.parquet'

# Convert csv to parquet (lighter on github)
df = pd.read_csv(CSV_PATH)
table = pa.Table.from_pandas(df)
pq.write_table(table, PARQUET_PATH)

# # Convert parquet back to csv, or refactor analysis.ipynb to use parquet instead
# df = pd.read_parquet(PARQUET_PATH, engine='pyarrow')
# df.to_csv(CSV_PATH, index=False)