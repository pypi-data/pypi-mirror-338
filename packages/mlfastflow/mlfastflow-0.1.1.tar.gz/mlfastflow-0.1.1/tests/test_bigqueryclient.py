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


sql = f"SELECT * FROM `{gg.project_id}.{gg.dataset_id}.fear_and_greed_index` LIMIT 10"

# Use sql2df instead of run_sql to get DataFrame results
df = gg.sql2df(sql)

print(df)
