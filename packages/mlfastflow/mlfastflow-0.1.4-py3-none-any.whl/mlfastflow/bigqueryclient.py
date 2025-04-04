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
    
    # def save_sql_to_gcs(self, sql: str, 
    #                    bucket_name: str, 
    #                    blob_name: str,
    #                    metadata: Optional[Dict[str, str]] = None,
    #                    create_bucket_if_not_exists: bool = False) -> bool:
    #     """
    #     Save a SQL query to Google Cloud Storage.
        
    #     Args:
    #         sql (str): The SQL query to save
    #         bucket_name (str): Name of the GCS bucket
    #         blob_name (str): Path/name for the file in the bucket
    #         metadata (Optional[Dict[str, str]]): Optional metadata to include with the file
    #         create_bucket_if_not_exists (bool): If True, create the bucket if it doesn't exist
            
    #     Returns:
    #         bool: True if save was successful, False otherwise
            
    #     Raises:
    #         ValueError: If SQL query is empty or parameters are invalid
    #     """
    #     # Input validation
    #     if sql is None or not sql.strip():
    #         raise ValueError("SQL query cannot be None or empty")
            
    #     if not bucket_name or not blob_name:
    #         raise ValueError("Bucket name and blob name must be provided")
            
    #     try:
    #         # Create storage client using the same credentials
    #         storage_client = storage.Client(
    #             credentials=self.credentials,
    #             project=self.project_id
    #         )
            
    #         # Check if bucket exists
    #         try:
    #             bucket = storage_client.get_bucket(bucket_name)
    #             print(f"Using existing bucket: {bucket_name}")
    #         except exceptions.NotFound:
    #             if create_bucket_if_not_exists:
    #                 print(f"Bucket {bucket_name} does not exist. Creating...")
    #                 bucket = storage_client.create_bucket(bucket_name)
    #                 print(f"Bucket {bucket_name} created successfully")
    #             else:
    #                 print(f"Error: Bucket {bucket_name} does not exist. Set create_bucket_if_not_exists=True to create it.")
    #                 return False
            
    #         # Create a new blob
    #         blob = bucket.blob(blob_name)
            
    #         # Set content type and metadata
    #         content_type = "text/plain"
    #         if blob_name.endswith('.sql'):
    #             content_type = "application/sql"
                
    #         # Add timestamp metadata if not provided
    #         if metadata is None:
    #             metadata = {}
                
    #         if 'timestamp' not in metadata:
    #             metadata['timestamp'] = datetime.datetime.now().isoformat()
                
    #         if 'source_project' not in metadata:
    #             metadata['source_project'] = self.project_id
                
    #         if 'source_dataset' not in metadata:
    #             metadata['source_dataset'] = self.dataset_id
                
    #         # Set metadata
    #         blob.metadata = metadata
            
    #         # Upload the SQL query
    #         blob.upload_from_string(
    #             data=sql,
    #             content_type=content_type
    #         )
            
    #         print(f"Successfully saved SQL query to gs://{bucket_name}/{blob_name}")
    #         return True
            
    #     except Exception as e:
    #         print(f"Error saving SQL to Google Cloud Storage: {str(e)}")
    #         return False
            
    # def sql_to_gcs_parquet(self, sql: str, 
    #                       bucket_name: str, 
    #                       blob_name: str,
    #                       metadata: Optional[Dict[str, str]] = None,
    #                       create_bucket_if_not_exists: bool = False,
    #                       compression: str = 'snappy') -> bool:
    #     """
    #     Execute a SQL query and save the results as a parquet file in Google Cloud Storage.
        
    #     Args:
    #         sql (str): The SQL query to execute
    #         bucket_name (str): Name of the GCS bucket
    #         blob_name (str): Path/name for the parquet file in the bucket (should end with .parquet)
    #         metadata (Optional[Dict[str, str]]): Optional metadata to include with the file
    #         create_bucket_if_not_exists (bool): If True, create the bucket if it doesn't exist
    #         compression (str): Compression codec for parquet file ('snappy', 'gzip', 'brotli', or None)
            
    #     Returns:
    #         bool: True if save was successful, False otherwise
            
    #     Raises:
    #         ValueError: If SQL query is empty or parameters are invalid
    #     """
    #     # Input validation
    #     if sql is None or not sql.strip():
    #         raise ValueError("SQL query cannot be None or empty")
            
    #     if not bucket_name or not blob_name:
    #         raise ValueError("Bucket name and blob name must be provided")
        
    #     # Add .parquet extension if not present
    #     if not blob_name.lower().endswith('.parquet'):
    #         blob_name = f"{blob_name}.parquet"
            
    #     # Step 1: Execute SQL query and get results as DataFrame
    #     try:
    #         print(f"Executing SQL query...")
    #         df = self.sql2df(sql)
            
    #         if df is None or df.empty:
    #             print("SQL query returned no results or failed to execute")
    #             return False
                
    #         print(f"SQL query executed successfully, retrieved {len(df)} rows")
            
    #         # Step 2: Create GCS client and check bucket
    #         storage_client = storage.Client(
    #             credentials=self.credentials,
    #             project=self.project_id
    #         )
            
    #         # Check if bucket exists
    #         try:
    #             bucket = storage_client.get_bucket(bucket_name)
    #             print(f"Using existing bucket: {bucket_name}")
    #         except exceptions.NotFound:
    #             if create_bucket_if_not_exists:
    #                 print(f"Bucket {bucket_name} does not exist. Creating...")
    #                 bucket = storage_client.create_bucket(bucket_name)
    #                 print(f"Bucket {bucket_name} created successfully")
    #             else:
    #                 print(f"Error: Bucket {bucket_name} does not exist. Set create_bucket_if_not_exists=True to create it.")
    #                 return False
            
    #         # Step 3: Create a local temporary file for the parquet
    #         tmp_path = Path(self.default_path) / f"temp_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.parquet"
            
    #         # Step 4: Save DataFrame as parquet
    #         df.to_parquet(
    #             tmp_path, 
    #             compression=compression,
    #             index=False  # Don't include the index in the parquet file
    #         )
            
    #         print(f"DataFrame saved as parquet file temporarily at {tmp_path}")
            
    #         # Step 5: Upload the parquet file to GCS
    #         blob = bucket.blob(blob_name)
            
    #         # Add metadata
    #         if metadata is None:
    #             metadata = {}
                
    #         if 'timestamp' not in metadata:
    #             metadata['timestamp'] = datetime.datetime.now().isoformat()
                
    #         if 'source_project' not in metadata:
    #             metadata['source_project'] = self.project_id
                
    #         if 'source_dataset' not in metadata:
    #             metadata['source_dataset'] = self.dataset_id
                
    #         if 'rows' not in metadata:
    #             metadata['rows'] = str(len(df))
                
    #         if 'columns' not in metadata:
    #             metadata['columns'] = ','.join(df.columns.tolist())
                
    #         if 'sql_query' not in metadata:
    #             # Truncate SQL if it's too long for metadata
    #             max_sql_length = 1500  # GCS metadata value size limit
    #             sql_for_metadata = sql[:max_sql_length]
    #             if len(sql) > max_sql_length:
    #                 sql_for_metadata += "... [truncated]"
    #             metadata['sql_query'] = sql_for_metadata
                
    #         # Set metadata
    #         blob.metadata = metadata
            
    #         # Upload file
    #         blob.upload_from_filename(
    #             tmp_path,
    #             content_type='application/octet-stream'
    #         )
            
    #         # Clean up the temporary file
    #         try:
    #             os.remove(tmp_path)
    #             print(f"Temporary file {tmp_path} removed")
    #         except Exception as e:
    #             print(f"Warning: Could not remove temporary file {tmp_path}: {str(e)}")
            
    #         print(f"Successfully saved query results as parquet to gs://{bucket_name}/{blob_name}")
    #         return True
            
    #     except Exception as e:
    #         print(f"Error saving query results to Google Cloud Storage: {str(e)}")
    #         return False
    
    def sql2gcs(self, sql: str,
                    destination_uri: str,
                    format: str = 'PARQUET',
                    compression: str = 'SNAPPY',
                    create_temp_table: bool = True,
                    wait_for_completion: bool = True,
                    timeout: int = 300,
                    use_sharding: bool = True,
                    max_bytes_per_file: int = None) -> bool:
        """
        Export BigQuery query results directly to Google Cloud Storage without downloading data locally.
        This uses BigQuery's extract job functionality for efficient data transfer.
        
        Args:
            sql (str): The SQL query to execute
            destination_uri (str): GCS URI to export to (e.g., 'gs://bucket-name/path/to/file')
                                  For large datasets, use a wildcard pattern like 'gs://bucket-name/path/to/file-*.parquet'
                                  or set use_sharding=True to automatically add the wildcard
            format (str): Export format ('PARQUET', 'CSV', 'JSON', 'AVRO')
            compression (str): Compression type ('NONE', 'GZIP', 'SNAPPY', 'DEFLATE')
            create_temp_table (bool): Whether to create a temporary table for the results
            wait_for_completion (bool): Whether to wait for the export job to complete
            timeout (int): Timeout in seconds for waiting for job completion
            use_sharding (bool): Whether to use sharded export with wildcards. If True and destination_uri doesn't
                                contain wildcards, '-*.ext' will be added before the extension.
            max_bytes_per_file (int, optional): Maximum number of bytes per file in the export.
                                              Default BigQuery values per format are roughly:
                                              CSV/JSON: 1 GB, Avro: 2 GB, Parquet: 5 GB
                                              Recommended values: 256000000 (256MB) to 5000000000 (5GB)
            
        Returns:
            bool: True if export was successful, False otherwise
        """
        # Input validation
        if sql is None or not sql.strip():
            raise ValueError("SQL query cannot be None or empty")
            
        if not destination_uri or not destination_uri.startswith('gs://'):
            raise ValueError("Destination URI must be a valid GCS path starting with 'gs://'")
            
        # Validate format and compression
        format = format.upper()
        compression = compression.upper()
        
        valid_formats = ['PARQUET', 'CSV', 'JSON', 'AVRO']
        valid_compressions = ['NONE', 'GZIP', 'SNAPPY', 'DEFLATE']
        
        if format not in valid_formats:
            raise ValueError(f"Format must be one of {valid_formats}")
            
        if compression not in valid_compressions:
            raise ValueError(f"Compression must be one of {valid_compressions}")
        
        # Check if sharding is needed and add a wildcard pattern if necessary
        if use_sharding and '*' not in destination_uri:
            # Extract file extension if any
            file_extension = ''
            if '.' in destination_uri.split('/')[-1]:
                base_name, file_extension = os.path.splitext(destination_uri)
                destination_uri = f"{base_name}-*{file_extension}"
            else:
                # No extension, just add the wildcard at the end
                destination_uri = f"{destination_uri}-*"
                
            print(f"Enabled sharding with destination URI: {destination_uri}")
        
        try:
            # BigQuery extract job requires a table as the source, not a query directly
            # So we first need to either run the query to a destination table or use a temporary table
            
            if create_temp_table:
                # Create a temporary table to hold the query results
                temp_table_id = f"temp_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                temp_table_ref = f"{self.project_id}.{self.dataset_id}.{temp_table_id}"
                
                print(f"Creating temporary table {temp_table_ref} for query results...")
                
                # Create a job config for the query
                job_config = bigquery.QueryJobConfig(
                    destination=temp_table_ref,
                    write_disposition="WRITE_TRUNCATE"
                )
                
                # Run the query to the temporary table
                query_job = self.client.query(sql, job_config=job_config)
                query_job.result()  # Wait for query to complete
                
                print(f"Query executed successfully, results stored in temporary table")
                
                # Now set up the source table for the extract job
                source_table = self.client.get_table(temp_table_ref)
            else:
                # When not using a temporary table, we need to create a destination table
                # in a different way as RowIterator doesn't have a .table attribute
                print("Running query and creating temporary destination...")
                
                # Generate a unique job ID
                job_id = f"export_job_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                
                # Create a destination table with a temporary name
                temp_table_id = f"temp_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                temp_table_ref = f"{self.project_id}.{self.dataset_id}.{temp_table_id}"
                
                # Configure the query job with the destination
                job_config = bigquery.QueryJobConfig(
                    destination=temp_table_ref,
                    write_disposition="WRITE_TRUNCATE"
                )
                
                # Run the query
                query_job = self.client.query(
                    sql,
                    job_config=job_config,
                    job_id=job_id
                )
                
                # Wait for query to complete
                query_job.result()
                
                # Get the destination table reference
                source_table = self.client.get_table(temp_table_ref)
                
                print(f"Query executed successfully, temporary results available")
            
            # Configure the extract job
            extract_job_config = bigquery.ExtractJobConfig()
            extract_job_config.destination_format = format
            
            # Set compression if not NONE
            if compression != 'NONE':
                extract_job_config.compression = compression
                
            # Set maximum bytes per shard if specified
            if max_bytes_per_file is not None:
                if max_bytes_per_file < 1000000:  # 1MB minimum
                    print(f"Warning: max_bytes_per_file {max_bytes_per_file} is very small. Setting to 1MB minimum.")
                    max_bytes_per_file = 1000000
                elif max_bytes_per_file > 5000000000:  # 5GB maximum for Parquet
                    if format == 'PARQUET':
                        print(f"Warning: max_bytes_per_file {max_bytes_per_file} exceeds 5GB limit for Parquet. Setting to 5GB.")
                        max_bytes_per_file = 5000000000
                    elif format in ['CSV', 'JSON']:
                        print(f"Warning: max_bytes_per_file {max_bytes_per_file} exceeds 1GB limit for {format}. Setting to 1GB.")
                        max_bytes_per_file = 1000000000
                    elif format == 'AVRO':
                        print(f"Warning: max_bytes_per_file {max_bytes_per_file} exceeds 2GB limit for AVRO. Setting to 2GB.")
                        max_bytes_per_file = 2000000000
                
                # Try to set the property if supported by the library version
                try:
                    # Try setting property directly first
                    try:
                        extract_job_config.max_bytes_per_file = max_bytes_per_file
                    except (AttributeError, TypeError):
                        # Alternative approach: set it in the _properties dictionary
                        if not hasattr(extract_job_config, '_properties'):
                            extract_job_config._properties = {}
                        if 'configuration' not in extract_job_config._properties:
                            extract_job_config._properties['configuration'] = {}
                        if 'extract' not in extract_job_config._properties['configuration']:
                            extract_job_config._properties['configuration']['extract'] = {}
                        
                        # Set the property in the underlying dictionary
                        extract_job_config._properties['configuration']['extract']['maxBytesPerFile'] = max_bytes_per_file
                    
                    print(f"Setting maximum bytes per file to {max_bytes_per_file} bytes")
                except Exception as e:
                    print(f"Warning: Could not set max_bytes_per_file: {str(e)}")
                    print(f"Your version of google-cloud-bigquery may not support this feature properly.")
                    print(f"Continuing with default file sizes...")
                
            # Start the extract job
            print(f"Starting extract job to {destination_uri}")
            extract_job = self.client.extract_table(
                source_table,
                destination_uri,
                job_config=extract_job_config
            )
            
            # Wait for the job to complete if requested
            if wait_for_completion:
                print(f"Waiting for extract job to complete (timeout: {timeout} seconds)...")
                extract_job.result(timeout=timeout)  # Wait for the job to complete
                print(f"Extract job completed successfully")
                
                # Clean up temporary table if created
                if create_temp_table:
                    print(f"Cleaning up temporary table {temp_table_ref}")
                    self.client.delete_table(temp_table_ref)
                
            else:
                print(f"Extract job started (job_id: {extract_job.job_id})")
                print(f"You can check the job status in the BigQuery console")
            
            return True
            
        except Exception as e:
            print(f"Error exporting query results to GCS: {str(e)}")
            return False