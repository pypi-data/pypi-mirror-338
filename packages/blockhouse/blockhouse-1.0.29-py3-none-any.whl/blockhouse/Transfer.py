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


    def _prune_url_fields(self, data: dict):
            """
            Recursively removes keys that contain 'url' in their name from a nested dictionary.

            Args:
                data (dict): The dictionary to prune.
            """
            keys_to_delete = [key for key in data if 'url' in key.lower()]
            for key in keys_to_delete:
                del data[key]

            for key, value in data.items():
                if isinstance(value, dict):
                    self._prune_url_fields(value)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            self._prune_url_fields(item)

    


    def register_file(self, file_name: str, local_file_path: str = None) -> dict:
        """
        Register a file mapping for the dashboard using the Blockhouse upload API.
        
        Args:
            file_name (str): Name of the file to register in S3
            local_file_path (str, optional): Path to the local file. If provided, this will be used
                                            instead of trying to open file_name directly.
                
        Returns:
            dict: Response from the API
        """
        try:
            # print(f"DEBUG: register_file called with file_name={file_name}, local_file_path={local_file_path}")
            
            headers = {"x-api-key": self.api_key}
            
            # Use local_file_path if provided, otherwise use file_name
            file_path_to_open = local_file_path if local_file_path else file_name
            # print(f"DEBUG: Attempting to open file at path: {file_path_to_open}")
            
            try:
                file_to_upload = open(file_path_to_open, 'rb')
                # print(f"DEBUG: Successfully opened file: {file_path_to_open}")
            except FileNotFoundError:
                # print(f"DEBUG: File not found: {file_path_to_open}")
                return {
                    "status": "error",
                    "message": f"File {file_name} not found for registration"
                }
            
            # Create the payload for the multipart/form-data request
            # Use the base filename from file_name for the S3 object, but the local file content
            files = [('files', (os.path.basename(file_name), file_to_upload))]
            
            # Hardcoded values as per requirement
            data = {
                'platform': 'blockhouse',
                'user_email': 'prasannavijaynatu3@gmail.com',
                'system_platform': 'sdk'
            }
            
            # API endpoint URL from the documentation
            api_url = "https://fast-api.blockhouse.app/api/analytics/upload/{platform}"
            api_url = api_url.replace("{platform}", "blockhouse")
            
            # print(f"DEBUG: Sending registration request to: {api_url}")
            
            try:
                response = requests.post(
                    api_url,
                    headers=headers,
                    files=files,
                    data=data,
                    timeout=30
                )
                
                # Close the file after upload
                file_to_upload.close()
                
                # print(f"DEBUG: Registration response status code: {response.status_code}")
                
                try:
                    response_json = response.json()
                    self._prune_url_fields(response_json)
                    # print(f"DEBUG: Registration response JSON: {response_json}")
                except:
                    # print(f"DEBUG: Registration response body (not JSON): {response.text[:200]}...")
                    return {
                        "status": "error",
                        "message": f"Invalid JSON response: {response.text[:200]}..."
                    }
                
                # Handle error statuses gracefully
                if response.status_code >= 400:
                    # print(f"DEBUG: API error (status {response.status_code}): {response.text}")
                    return {
                        "status": "error",
                        "message": f"API returned error {response.status_code}: {response.text[:200]}..."
                    }
                
                return {
                    "status": "success",
                    "message": "File registered successfully",
                    "response": response_json
                }
            except requests.exceptions.RequestException as e:
                # print(f"DEBUG: Registration request exception: {str(e)}")
                return {
                    "status": "error",
                    "message": f"Registration request failed: {str(e)}"
                }
                    
        except Exception as e:
            # print(f"DEBUG: Unexpected error during registration: {str(e)}")
            import traceback
            traceback.print_exc()
            
            return {
                "status": "error",
                "message": f"Registration encountered an error: {str(e)}"
            }



    def send_file(self, local_file_path: str, bucket_name: str, object_name=None) -> dict:
        """
        Upload a file to an S3 bucket and register it with the dashboard.

        Args:
            local_file_path (str): Path to the local file.
            bucket_name (str): Name of the S3 bucket.
            object_name (str, optional): Name to give the file in S3. Defaults to None.

        Returns:
            dict: Response from the S3 file upload and registration.
        """
        try:
            if not self.s3_connector:
                self.initialize_s3_connector()

            # Determine the object name if not provided
            if object_name is None:
                object_name = os.path.basename(local_file_path)

            # Upload file to S3
            upload_response = self.s3_connector.upload_file(
                file_name=local_file_path, 
                bucket_name=bucket_name,
                object_name=object_name
            )
            
            # Register the file after upload
            register_result = self.register_file(file_name=object_name, local_file_path=local_file_path)
            print(register_result)
            result = {
                "status": "success" if register_result["status"] == "success" else "partial_success", 
                "file": local_file_path, 
                "object_name": object_name,
                "upload_status": "success",
                "register_status": register_result["status"],
                "message": "File uploaded successfully."
            }
            
            # Add registration message
            if register_result["status"] == "success":
                result["message"] += " File registered successfully."
            else:
                result["message"] += f" File registration failed: {register_result.get('message', 'Unknown error')}"
            
            return result
        except Exception as e:
            return {"status": "error", "file": local_file_path, "message": str(e)}

    def process_data(self, 
              bucket_name: str, risk_factor: float = None, time_horizon: int = None, 
              market_data_path: str = None,, trade_data_path: str = None, #target_size: int,
              endpoint_path: str = "/fix/market") -> dict:
        """
        Process market and trade data with additional parameters.

        Args:
            trade_data_path (str): Path to trade data file (csv/parquet)
            bucket_name (str): Name of the S3 bucket
            risk_factor (float, optional): Risk factor parameter. Defaults to None.
            time_horizon (int, optional): Time horizon parameter (in days). Defaults to None.
            market_data_path (str, optional): Path to market data file (csv/parquet). Defaults to None.
            endpoint_path (str, optional): API endpoint path. Defaults to "/fix/market".

        Returns:
            dict: Response containing file upload results and processing response
        """
        if not self.s3_connector:
            self.initialize_s3_connector()
                
        # Prepare file list for upload
        files_to_upload = []

        if trade_data_path:
            trade_filename = os.path.basename(trade_data_path)
            files_to_upload.append({
            "local_file_path": trade_data_path, 
            "object_name": trade_filename
            })
        
        # Get just the filenames without prefixes
        # trade_filename = os.path.basename(trade_data_path)
        
        # Add market data file if provided
        if market_data_path:
            market_filename = os.path.basename(market_data_path)
            files_to_upload.append({
                "local_file_path": market_data_path, 
                "object_name": market_filename
            })
        
        # Always add trade data file
        # files_to_upload.append({
        #     "local_file_path": trade_data_path, 
        #     "object_name": trade_filename
        # })
        
        file_results = []
        
        # Using ThreadPoolExecutor for concurrent uploads
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            future_to_file = {
                executor.submit(
                    self.send_file, 
                    file_info["local_file_path"], 
                    bucket_name,
                    file_info["object_name"]  # Always provide the object_name explicitly
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
        
        # Check if all files were uploaded successfully (accept both success and partial_success)
        if not all(result["status"] in ["success", "partial_success"] for result in file_results):
            return {
                "status": "error",
                "message": "Some files failed to upload",
                "file_uploads": file_results
            }
        
        # Prepare processing parameters as an empty dict first
        processing_params = {}
        
        # Only add optional parameters if they are provided
        if risk_factor is not None:
            processing_params["risk_factor"] = risk_factor
        
        if time_horizon is not None:
            processing_params["time_horizon"] = time_horizon
        
        # Add trade data URI using the exact filename
        trade_data_uri = f"s3://{bucket_name}/{trade_filename}"
        processing_params["trade_data_uri"] = trade_data_uri
        
        # Add market data URI if available, using the exact filename
        if market_data_path:
            market_data_uri = f"s3://{bucket_name}/{market_filename}"
            processing_params["market_data_uri"] = market_data_uri
        
        try:
            headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}
            
            # Send the processing request to the specified endpoint
            response = requests.post(
                self.api_url + endpoint_path,
                headers=headers,
                json=processing_params
            )
            response.raise_for_status()
            
            # Get the response JSON
            response_data = response.json()
            
            # Filter out URLs from the response
            if isinstance(response_data, dict):
                self._prune_url_fields(response_data)
            
            return {
                "status": "file uploaded successfully",
                "file_uploads": file_results,
                "processing_response": response_data
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
    client = Transfer(api_key="bff86ee42149430452d71ca10c4c2336")
    
    # try:
    result = client.process_data(
        market_data_path="..\\..\\..\\Strategy-Development\\SOR\\first_25000_rows_copy.csv",
        # trade_data_path='D:\\Blockhouse\\Backend\\PythonSDK\\123456789.csv',  # "..\\..\\..\\Strategy-Development\\SOR\\first_25000_rows.csv",
        bucket_name="blockhouse-sdk",

    )
    
    print("Process result:", result["status"])
  