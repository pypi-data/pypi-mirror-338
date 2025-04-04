import requests
import concurrent.futures
import os  # Added missing import
from blockhouse.client.s3_connector import S3Connector


class Transfer:
    def __init__(self, api_key: str):
        """
        Initialize the Transfer class with an API key.

        Args:
            api_key (str): API key for authentication, used to connect to the Go API.
        """
        self.api_key = api_key
        self.api_url = "https://go-api.blockhouse.app"
        # self.api_url = "http://localhost:8080"
        
        self.s3_connector = None

    def fetch_aws_credentials(self) -> dict:
        """
        Fetch AWS credentials from the Go API.

        Returns:
            dict: AWS credentials including access key, secret key, and region.
        """
        headers = {"x-api-key": self.api_key}
        response = requests.get(
            self.api_url + "/transfer-data/s3-credentials", headers=headers
        )
        response.raise_for_status()

        credentials_data = response.json().get("data")
        if not credentials_data:
            raise ValueError("Failed to retrieve AWS credentials.")

        return credentials_data

    def initialize_s3_connector(self):
        """
        Initialize the S3 connector with fetched AWS credentials.
        """
        credentials = self.fetch_aws_credentials()
        self.s3_connector = S3Connector(
            aws_access_key_id=credentials["aws_access_key_id"],
            aws_secret_access_key=credentials["aws_secret_access_key"],
            region_name=credentials["s3_region"],
        )

    def send_file(self, local_file_path: str, bucket_name: str, object_name=None) -> dict:
        """
        Upload a file to an S3 bucket.

        Args:
            local_file_path (str): Path to the local file.
            bucket_name (str): Name of the S3 bucket.
            object_name (str, optional): Name to give the file in S3. Defaults to None.

        Returns:
            dict: Response from the S3 file upload.
        """
        try:
            if not self.s3_connector:
                self.initialize_s3_connector()

            response = self.s3_connector.upload_file(
                file_name=local_file_path, 
                bucket_name=bucket_name,
                object_name=object_name
            )
            return {"status": "success", "file": local_file_path, "message": "file uploaded successfully."}
        except Exception as e:
            return {"status": "error", "file": local_file_path, "message": str(e)}
        
    def process_data(self, market_data_path: str, trade_data_path: str, 
                    bucket_name: str, risk_factor: float, time_horizon: int, 
                    target_size: int, endpoint_path: str = "/fix/market") -> dict:
        """
        Process market and trade data with additional parameters.

        Args:
            market_data_path (str): Path to market data file (csv/parquet)
            trade_data_path (str): Path to trade data file (csv/parquet)
            bucket_name (str): Name of the S3 bucket
            risk_factor (float): Risk factor parameter
            time_horizon (int): Time horizon parameter (in days)
            target_size (int): Target size parameter
            endpoint_path (str, optional): API endpoint path. Defaults to "/fix/process-data".

        Returns:
            dict: Response containing file upload results and processing response
        """
        if not self.s3_connector:
            self.initialize_s3_connector()
            
        # Prepare file list for upload
        files_to_upload = [
            {"local_file_path": market_data_path, "object_name": "market_data_" + os.path.basename(market_data_path)},
            {"local_file_path": trade_data_path, "object_name": "trade_data_" + os.path.basename(trade_data_path)}
        ]
        
        file_results = []
        
        # Using ThreadPoolExecutor for concurrent uploads
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_to_file = {
                executor.submit(
                    self.send_file, 
                    file_info["local_file_path"], 
                    bucket_name,
                    file_info.get("object_name")
                ): file_info 
                for file_info in files_to_upload
            }
            
            for future in concurrent.futures.as_completed(future_to_file):
                file_info = future_to_file[future]
                try:
                    result = future.result()
                    file_results.append(result)
                except Exception as e:
                    file_results.append({
                        "status": "error", 
                        "file": file_info["local_file_path"], 
                        "message": str(e)
                    })
        
        # Check if both files were uploaded successfully
        if not all(result["status"] == "success" for result in file_results):
            return {
                "status": "error",
                "message": "Some files failed to upload",
                "file_uploads": file_results
            }
        
        # Create S3 URIs for the uploaded files
        market_data_s3_key = "market_data_" + os.path.basename(market_data_path)
        trade_data_s3_key = "trade_data_" + os.path.basename(trade_data_path)
        
        # Construct S3 URIs (s3://bucket-name/key)
        market_data_uri = f"s3://{bucket_name}/{market_data_s3_key}"
        trade_data_uri = f"s3://{bucket_name}/{trade_data_s3_key}"
        
        # Send processing parameters to API with S3 URIs
        processing_params = {
            "market_data_uri": market_data_uri,
            "trade_data_uri": trade_data_uri,
            "risk_factor": risk_factor,
            "time_horizon": time_horizon,
            "target_size": target_size
        }
        
        try:
            headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}
            
            # Send the processing request to the specified endpoint
            response = requests.post(
                self.api_url + endpoint_path,
                headers=headers,
                json=processing_params
            )
            response.raise_for_status()
            
            return {
                "status": "success",
                "file_uploads": file_results,
                "processing_response": response.json()
            }
        except Exception as e:
            return {
                "status": "error",
                "file_uploads": file_results,
                "message": f"Failed to process data: {str(e)}"
            }

    def trades_data(self) -> dict:
        """
        Calls the Go API to generate trades and transfer trading data to Kafka.

        Returns:
            dict: Response from the Go API.
        """
        headers = {"x-api-key": self.api_key}

        try:
            response = requests.get(
                self.api_url + "/transfer-data/trades", headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


if __name__ == "__main__":
    client = Transfer(api_key="56c4a3bd013d65426a615af19dc67963")
    
    result = client.process_data(
        market_data_path="..\\..\\..\\Strategy-Development\\SOR\\first_25000_rows_copy.csv",
        trade_data_path="..\\..\\..\\Strategy-Development\\SOR\\first_25000_rows.csv",
        bucket_name="blockhouse-sdk",
        risk_factor=0.5,
        time_horizon=30,
        target_size=1000,
        # endpoint_path="/fix/market"
    )
    
    print("Process result:", result["status"])
    
    if result["status"] == "success" and "processing_response" in result:
        print("Processing details:", result["processing_response"])
    else:
        print("Error message:", result.get("message", "Unknown error"))
        
    print("\nFile upload results:")
    for file_result in result["file_uploads"]:
        print(f"  {file_result['file']}: {file_result['status']}")










# import requests
# from blockhouse.client.s3_connector import S3Connector


# class Transfer:
#     def __init__(self, api_key: str):
#         """
#         Initialize the Transfer class with an API key.

#         Args:
#             api_key (str): API key for authentication, used to connect to the Go API.
#         """
#         self.api_key = api_key
#         self.api_url = "https://go-api.blockhouse.app"
#         self.s3_connector = None

#     def fetch_aws_credentials(self) -> dict:
#         """
#         Fetch AWS credentials from the Go API.

#         Returns:
#             dict: AWS credentials including access key, secret key, and region.
#         """
#         headers = {"x-api-key": self.api_key}
#         response = requests.get(
#             self.api_url + "/transfer-data/s3-credentials", headers=headers
#         )
#         response.raise_for_status()

#         credentials_data = response.json().get("data")
#         if not credentials_data:
#             raise ValueError("Failed to retrieve AWS credentials.")

#         return credentials_data

#     def initialize_s3_connector(self):
#         """
#         Initialize the S3 connector with fetched AWS credentials.
#         """
#         credentials = self.fetch_aws_credentials()
#         self.s3_connector = S3Connector(
#             aws_access_key_id=credentials["aws_access_key_id"],
#             aws_secret_access_key=credentials["aws_secret_access_key"],
#             region_name=credentials["s3_region"],
#         )

#     def send_file(self, local_file_path: str, bucket_name: str) -> dict:
#         """
#         Upload a file to an S3 bucket.

#         Args:
#             local_file_path (str): Path to the local file.
#             bucket_name (str): Name of the S3 bucket.

#         Returns:
#             dict: Response from the S3 file upload.
#         """
#         try:
#             if not self.s3_connector:
#                 self.initialize_s3_connector()

#             response = self.s3_connector.upload_file(
#                 file_name=local_file_path, bucket_name=bucket_name
#             )
#             # return response
#             return {"status": "success", "message": "file uploaded successfully."}
#         except Exception as e:
#             return {"status": "error", "message": str(e)}

#     def trades_data(self) -> dict:
#         """
#         Calls the Go API to generate trades and transfer trading data to Kafka.

#         Returns:
#             dict: Response from the Go API.
#         """
#         headers = {"x-api-key": self.api_key}

#         try:
#             response = requests.get(
#                 self.api_url + "/transfer-data/trades", headers=headers
#             )
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             return {"error": str(e)}


# if __name__ == "__main__":
#     client = Transfer(api_key="your_api_key_here")

#     send = client.send_file(local_file_path="test123.txt", bucket_name="blockhouse-sdk")

#     print(send)

#     trades = client.trades_data()

#     print(trades)
