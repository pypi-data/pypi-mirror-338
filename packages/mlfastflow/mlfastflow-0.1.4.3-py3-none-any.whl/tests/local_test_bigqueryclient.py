


#%%
import sys
import os
from pathlib import Path

# Add parent directory to path so Python can find the module
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import directly from the module file, bypassing __init__.py
from mlfastflow.bigqueryclient import BigQueryClient
import dotenv
dotenv.load_dotenv('/Users/jinwenliu/github/.env/.env', override=True)


gg = BigQueryClient(
    project_id = os.getenv('GCP_PROJECT_ID'),
    dataset_id = os.getenv('GCP_DATASET_ID'),
    key_file=os.getenv('GCP_KEY_FILE')
)


sql = f"SELECT * FROM `{gg.project_id}.{gg.dataset_id}.fear_and_greed_index`"

# Use sql2df instead of run_sql to get DataFrame results
df = gg.sql2df(sql)

print(df)



#%%
# Test export_query_to_gcs - this uses BigQuery's native export functionality
# This method is much more efficient for large datasets as it exports directly from BigQuery to GCS
# without pulling data through your client machine

# Basic usage with sharding and large file size (500MB per file)
gg.sql2gcs(
    sql=f"SELECT * FROM `{gg.project_id}.{gg.dataset_id}.stock_prices`",
    destination_uri="gs://mlfastflow/data/stock_prices.parquet",
    format="PARQUET",
    compression="SNAPPY",
    use_sharding=True,
    max_bytes_per_file=500000000  # 500MB per file instead of the default small size
)

#%%
# Export as CSV with GZIP compression - also using larger shards (250MB per file)
gg.sql2gcs(
    sql=sql,
    destination_uri="gs://mlfastflow/data/fear_and_greed_index.csv",
    format="CSV",
    compression="GZIP",
    use_sharding=True,
    max_bytes_per_file=250000000  # 250MB per file
)

#%%
# Try the raw implementation which should better handle file sizes
print("Testing the raw implementation with direct API access")
gg.sql2gcs_raw(
    sql=f"SELECT * FROM `{gg.project_id}.{gg.dataset_id}.stock_prices`",
    destination_uri="gs://mlfastflow/data/stock_prices_large_large.parquet",
    format="PARQUET",
    compression="SNAPPY",
    chunk_size=500000000  # 500MB chunks
)

#%%
# Try SQL-based EXPORT DATA approach - this is a completely different method
# Using BigQuery's native SQL EXPORT DATA statement with max_file_size parameter
print("Testing EXPORT DATA SQL method")
gg.sql2gcs_via_query(
    sql=f"SELECT * FROM `{gg.project_id}.{gg.dataset_id}.stock_prices`",
    destination_uri="gs://mlfastflow/data/stock_prices_sql_export-*.parquet",
    format="PARQUET",
    compression="SNAPPY"
)

# %%
