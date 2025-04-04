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

# Basic usage
gg.export_query_to_gcs(
    sql=f"SELECT * FROM `{gg.project_id}.{gg.dataset_id}.stock_prices`",
    destination_uri="gs://mlfastflow/data/stock_prices.parquet",
    format="PARQUET",
    compression="SNAPPY",
    create_temp_table=True,
    wait_for_completion=True
)

#%%
# Export as CSV with GZIP compression
gg.export_query_to_gcs(
    sql=sql,
    destination_uri="gs://mlfastflow/data/fear_and_greed_index.csv",
    format="CSV",
    compression="GZIP"
)

# %%
