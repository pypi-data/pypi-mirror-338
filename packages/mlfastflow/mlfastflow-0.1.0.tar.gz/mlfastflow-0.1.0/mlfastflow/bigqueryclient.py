from typing import Optional, Dict, List, Any, Union
import pandas as pd
from google.cloud import bigquery, storage
from google.oauth2 import service_account
from google.api_core import exceptions as google_exceptions
import datetime
import pandas_gbq
import os
from google.api_core import exceptions
import pyarrow.parquet as parquet
from pathlib import Path
import json
import dotenv


class BigQueryClient:
    def __init__(
                self, 
                project_id: str, 
                dataset_id: str, 
                key_file: str
                ):
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.key_file = key_file

        self.client = None
        self.credentials = None
        self.job_config = None
        self.full_table_id = None
        self.sql = None
        
        self.default_path = Path('/tmp/data/bigquery/')
        if not self.default_path.exists():
            self.default_path.mkdir(parents=True)

        if self.key_file:
            self.credentials = service_account.Credentials.from_service_account_file(
                self.key_file,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
            self.client = bigquery.Client(
                credentials=self.credentials,
                project=self.credentials.project_id,
            )

        
        

    def get_client(self):
        return BigQueryClient(
            self.project_id, 
            self.dataset_id, 
            self.key_file
        )

    def show(self) -> None:
        # Use a consistent format for better readability
        config_info = {
            "GCP Configuration": {
                "Project ID": self.project_id,
                "Dataset ID": self.dataset_id,
                "Bucket Name": self.bucket_name or "Not set"
            },
            "Client Status": {
                "BigQuery Client": "Initialized" if self.client else "Not initialized",
                "Credentials": "Set" if self.credentials else "Not set"
            },
            "File Configuration": {
                "Default Path": str(self.default_path),
                "Key File": self.key_file or "Not set",
                "Output Path": str(self.output_path) if self.output_path else "Not set"
            }
        }

        # Print with clear section formatting
        for section, details in config_info.items():
            print(f"\n{section}:")
            print("-" * (len(section) + 1))
            for key, value in details.items():
                print(f"{key:15}: {value}")
    

    def close(self) -> bool:
        """Close the BigQuery client and clean up resources.
        
        This method ensures proper cleanup of the BigQuery client connection
        and associated resources. If no client exists, it will return silently.
        
        The method will attempt to clean up all resources even if an error occurs
        during client closure.
        
        Returns:
            bool: True if cleanup was successful, False if an error occurred
        """
        # Early return if there's no client to close
        if not hasattr(self, 'client') or self.client is None:
            return True
        
        success = True
        
        try:
            self.client.close()
        except Exception as e:
            print(f"Warning: Error while closing client: {str(e)}")
            success = False
        finally:
            # Define all attributes to reset in a list for maintainability
            attrs_to_reset = [
                'client', 'credentials', 'job_config',
                'sql', 'bucket_name', 'default_path', 'output_path'
            ]
            
            # Reset all attributes to None
            for attr in attrs_to_reset:
                if hasattr(self, attr):
                    setattr(self, attr, None)
                    
        return success
    


    def __del__(self):
        """Destructor to ensure proper cleanup of resources."""
        self.close()
    


    def run_sql(self, sql: str) -> None:
        if sql is None:
            raise ValueError("sql must be a non-empty string")
        
        # Check if SQL contains DELETE or TRUNCATE operations
        sql_upper = sql.upper()
        if "DELETE" in sql_upper or "TRUNCATE" in sql_upper:
            print("ERROR: Cannot execute DELETE or TRUNCATE operations for safety reasons")
            return
        
        try:
            self.client.query(sql)
            print("Query run complete")
        except Exception as e:
            print(f"Error running query: {str(e)}")

    def sql2df(self, sql: str = None) -> Optional[pd.DataFrame]:
        if sql is None or not sql.strip():
            raise ValueError("sql must be a non-empty string")
        
        # Check if SQL contains DELETE or TRUNCATE operations
        sql_upper = sql.upper()
        if "DELETE" in sql_upper or "TRUNCATE" in sql_upper:
            print("ERROR: Cannot execute DELETE or TRUNCATE operations for safety reasons")
            return None
        
        try:
            query_job = self.client.query(sql)
            return query_job.to_dataframe()
        except Exception as e:
            print(f"Error running query: {str(e)}")
            return None

    
    def df2table(self, df: pd.DataFrame, 
                 table_id: str, 
                 if_exists: str = 'fail',
                 schema: Optional[List[Dict[str, Any]]] = None) -> bool:
        """
        Upload a pandas DataFrame to a BigQuery table.
        
        Args:
            df (pd.DataFrame): The DataFrame to upload
            table_id (str): Target table ID
            if_exists (str): Action if table exists: 'fail', 'replace', or 'append'
            schema (Optional[List[Dict[str, Any]]]): BigQuery schema for the table
            
        Returns:
            bool: True if upload was successful, False otherwise
        
        Raises:
            ValueError: If DataFrame is empty or parameters are invalid
        """
        # Input validation
        if df is None or df.empty:
            raise ValueError("DataFrame cannot be None or empty")
        
        if if_exists not in ('fail', 'replace', 'append'):
            raise ValueError("if_exists must be one of: 'fail', 'replace', 'append'")
        
        # Set target table
        target_table_id = table_id
        if not target_table_id:
            raise ValueError("No table_id provided (neither in method call nor in instance)")
        
        # Construct full table ID
        full_table_id = f"{self.project_id}.{self.dataset_id}.{target_table_id}"
        
        try:
            # Configure job options
            job_config = bigquery.LoadJobConfig(
                schema=schema,
                write_disposition={
                    'fail': 'WRITE_EMPTY',
                    'replace': 'WRITE_TRUNCATE',
                    'append': 'WRITE_APPEND'
                }[if_exists]
            )
            
            # Execute the upload
            job = self.client.load_table_from_dataframe(
                df, 
                full_table_id, 
                job_config=job_config
            )
            
            # Wait for the job to complete
            job.result()
            
            print(f"Successfully uploaded {len(df)} rows to {full_table_id}")
            return True
            
        except Exception as e:
            print(f"Error uploading DataFrame to BigQuery: {str(e)}")
            return False