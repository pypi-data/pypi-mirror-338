import base64
import json
import os
import requests
import pandas as pd
import hashlib
import pickle
import datetime
from pathlib import Path
from datetime import datetime, timedelta
from urllib.parse import urlparse


def encoded(filepath):
    with open(filepath, "rb") as file:
        encoded_content = base64.b64encode(file.read()).decode("utf-8")
    return f"data:application/pdf;base64,{encoded_content}"


class VaultFile:
    def __init__(self, file_path: str, api_key: str, vault_url="https://api.tela.com/__hidden/services/vault", cache_dir=".vault_cache"):
        self.file_path = file_path
        self.api_key = api_key
        self.vault_url = vault_url
        self.name = self._generate_file_name()
        self.vault_identifier = f"vault://{self.name}"
        self.file_hash = self._calculate_file_hash() if not file_path.startswith("vault://") else None
        self.cache_dir = cache_dir
        self.cache_file = os.path.join(cache_dir, "cache.json")
        self.cache = self._load_cache()

    def upload(self):
        if self.file_path.startswith("vault://"):
            # Skip upload for vault:// URLs as they're already in the vault
            return
            
        # Check if file is already in cache with the same hash
        if self.file_hash in self.cache:
            # print(f"File already in cache, skipping upload: {self.file_hash}")
            self.name = self.cache[self.file_hash]
            self.vault_identifier = f"vault://{self.name}"
            return
            
        upload_url = self._get_upload_url()
        # Upload the file to the URL
        with open(self.file_path, 'rb') as file:
            response = requests.put(upload_url, data=file)

        # Check if the upload was successful
        if response.status_code != 200:
            raise Exception(f"Failed to upload file: {self.name}, {response.text}")
        
        # Update cache with new file hash
        self.cache[self.file_hash] = self.name
        self._save_cache()
        
    def get_download_url(self):
        # Get a download URL for the file
        response = requests.get(
            f"{self.vault_url}/v2/files/{self.name}",
            headers={
                "Authorization": f"{self.api_key}"
            }
        )
    
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Failed to get download URL for file: {self.name}")
            
        # Return the URL from the response
        return response.json().get('url')
    
    def _calculate_file_hash(self):
        """Calculate SHA-256 hash of file contents"""
        if not os.path.exists(self.file_path):
            return None
            
        sha256_hash = hashlib.sha256()
        with open(self.file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    def _load_cache(self):
        """Load the cache from disk"""
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_cache(self):
        """Save the cache to disk"""
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f)

    def _generate_file_name(self):
        if self.file_path.startswith("vault://"):
            return self.file_path.replace("vault://", "")
            
        timestamp = int(datetime.datetime.now().timestamp() * 1000)
        name = f"tela_law_{timestamp}_{self.file_path.split('/')[-1]}"
        return name
    
    def _get_upload_url(self):
        # Make a POST request to the API endpoint
        response = requests.post(f"{self.vault_url}/v2/files/{self.name}", headers={
            "Authorization": f"{self.api_key}"
        })
        
        if response.status_code != 200:
            raise Exception(f"Failed to get upload URL: {response.json()}")

        # Parse and return the URL from the response
        return response.json().get('url')


def is_vault_url(url):
    return url and url.startswith("vault://")


def get_file_url(filepath, api_key):
    """Get appropriate URL for a file, handling vault:// URLs"""
    if not filepath:
        return None
    
    if filepath.startswith(('http://', 'https://')):
        return filepath
    
    if is_vault_url(filepath):
        return filepath
    
    return encoded(filepath)


def file(filepath, parser_type="tela-pdf-parser", range=None, api_key=None, **options):
    file_options = options.copy()
    file_options["parserType"] = parser_type
    if range is not None:
        file_options["range"] = range
    # print(filepath)
    file_url = get_file_url(filepath, api_key)
    
    return {
        "file_url": file_url,
        "options": file_options
    }

def files(file_paths, parser_type="tela-pdf-parser", range=None, api_key=None, **options):
    """
    Create a files payload from a list of file paths with optional parameters.
    
    Args:
        file_paths (list): List of file paths or URLs to process
        parser_type (str, optional): Type of parser to use. Defaults to "tela-pdf-parser"
        range (str, optional): Page range to process. Defaults to None
        api_key (str, optional): API key for vault access
        **options: Additional options to pass to the parser
        
    Returns:
        dict: Files payload with list of processed files
    """
    file_list = []
    for f in file_paths:
        file_list.append(file(f, parser_type=parser_type, range=range, api_key=api_key, **options))
        
    return {
        "files": file_list
    }

class TelaClient:
    def __init__(self, api_key, api_url="https://api.tela.com", max_attempts=3, cache_dir=".tela_cache", enable_logging=True):
        self.api_key = api_key
        self.api_url = api_url
        self.max_attempts = max_attempts
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self._canvas_version_cache = {}
        self._canvas_version_cache_time = {}
        self.enable_logging = enable_logging
        self.log_file = Path(".tela_logs.jsonl")
        if enable_logging and not self.log_file.parent.exists():
            self.log_file.parent.mkdir(exist_ok=True)

    def upload_file(self, file_path):
        """
        Upload a file to Tela API and return the download URL
        
        Args:
            file_path (str): Path to the file to upload
            
        Returns:
            str: Download URL for the uploaded file
        """
        # Check if file is a vault URL
        if is_vault_url(file_path):
            vault_file = VaultFile(file_path, self.api_key)
            return vault_file.get_download_url()
            
        # Check if file exists in cache
        file_hash = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()
        cache_key = f"upload_{file_hash}"
        
        cached_response = self._get_cached_response(cache_key, check_age=True)
        if cached_response:
            return cached_response['download_url']
            
        # Get upload URL from Tela API
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(f'{self.api_url}/v2/file', headers=headers)
        upload_url = response.json()['upload_url']
        
        # Upload file to the provided URL
        with open(file_path, 'rb') as file:
            upload_response = requests.put(upload_url, data=file)
            upload_response.raise_for_status()
        
        # Cache the response
        self._cache_response(cache_key, response.json())
        
        # Return the download URL
        return response.json()['download_url']

    def upload_to_vault(self, file_path):
        """
        Upload a file to Vault and return the vault URL
        
        Args:
            file_path (str): Path to the file to upload
            
        Returns:
            str: Vault URL for the uploaded file
        """
        vault_file = VaultFile(file_path, self.api_key)
        vault_file.upload()
        return vault_file.vault_identifier

    def get_vault_download_url(self, vault_url):
        """
        Get a download URL for a vault file
        
        Args:
            vault_url (str): Vault URL to get download URL for
            
        Returns:
            str: Download URL for the vault file
        """
        vault_file = VaultFile(vault_url, self.api_key)
        return vault_file.get_download_url()
    def _get_cache_key(self, documents, canvas_id, override, canvas_version=None, run_id=None):
        # Create a string containing all input parameters including canvas version
        print("**run_id on cache key", run_id)
        if run_id is None:
            cache_str = f"{json.dumps(documents, sort_keys=True)}_{canvas_id}_{json.dumps(override, sort_keys=True) if override else ''}_{canvas_version}"
        else:
            print("**run_id on cache key", run_id)
            cache_str = f"{json.dumps(documents, sort_keys=True)}_{canvas_id}_{json.dumps(override, sort_keys=True) if override else ''}_{canvas_version}_{run_id}"
        # Create a hash of the input parameters
        return hashlib.sha256(cache_str.encode()).hexdigest()

    def _get_cached_response(self, cache_key, check_age=False):
        cache_file = self.cache_dir / f"{cache_key}.pickle"
        if cache_file.exists():
            if check_age:
                cache_age = datetime.now() - datetime.fromtimestamp(cache_file.stat().st_mtime)
                if cache_age >= timedelta(hours=12):
                    return None
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        return None

    def _cache_response(self, cache_key, response):
        cache_file = self.cache_dir / f"{cache_key}.pickle"
        with open(cache_file, 'wb') as f:
            pickle.dump(response, f)

    def get_canvas_version(self, canvas_id):
        """
        Get the promoted version of a canvas
        
        Args:
            canvas_id (str): Canvas ID to get version for
            
        Returns:
            str: Version ID of the promoted canvas version
        """
        # Check if we have a cached version and it's less than 20 seconds old
        current_time = datetime.now()
        if canvas_id in self._canvas_version_cache and canvas_id in self._canvas_version_cache_time:
            cache_age = current_time - self._canvas_version_cache_time[canvas_id]
            if cache_age < timedelta(seconds=20):
                return self._canvas_version_cache[canvas_id]
        
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(
            f'{self.api_url}/prompt-version',
            headers=headers,
            params={"promptId": canvas_id}
        )
        
        if response.status_code != 200:
            return None
            
        versions = response.json()
        for version in versions:
            if version.get("promoted"):
                # Cache the version and timestamp
                self._canvas_version_cache[canvas_id] = version.get("id")
                self._canvas_version_cache_time[canvas_id] = current_time
                return version.get("id")
        
        return None

    def clear_canvas_cache(self, canvas_id):
        # Iterate through all cache files
        cleared_count = 0
        for cache_file in self.cache_dir.glob("*.pickle"):
            # Read the cache file to check if it contains the canvas_id
            with open(cache_file, 'rb') as f:
                try:
                    cache_data = pickle.load(f)
                    # Check if the cache entry is related to the specified canvas_id
                    if isinstance(cache_data, dict) and cache_data.get("uses") == canvas_id:
                        # Delete the cache file
                        cache_file.unlink()
                        cleared_count += 1
                except:
                    # Skip if there's any error reading the cache file
                    continue
        return cleared_count

    def clear_all_cache(self):
        # Delete all cache files in the cache directory
        cleared_count = 0
        for cache_file in self.cache_dir.glob("*.pickle"):
            try:
                cache_file.unlink()
                cleared_count += 1
            except:
                continue
        return cleared_count
    
    def get_logs(self, limit=None, canvas_id=None):
        """
        Get logs from the log file, optionally filtered by canvas ID
        
        Args:
            limit (int, optional): Maximum number of logs to return
            canvas_id (str, optional): Filter logs by canvas ID
            
        Returns:
            list: List of log entries
        """
        if not self.log_file.exists():
            return []
            
        logs = []
        with open(self.log_file, 'r') as f:
            for line in f:
                try:
                    log = json.loads(line.strip())
                    if canvas_id and log.get('canvas_id') != canvas_id:
                        continue
                    logs.append(log)
                except:
                    continue
                    
        # Sort by timestamp, newest first
        logs.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        
        if limit:
            return logs[:limit]
        return logs
        
    def log_request(self, canvas_id, input_data, output, used_cache, run_id=None, duration_ms=None):
        """
        Log request details to a jsonl file
        """
        if not self.enable_logging:
            return
            
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "canvas_id": canvas_id,
            "input": input_data,
            "output": output,
            "used_cache": used_cache,
            "run_id": run_id
        }
        
        if duration_ms is not None:
            log_entry["duration_ms"] = duration_ms
            
        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    def request(self, documents, canvas_id, override=None, use_cache=True, run_id=None):
        # Get the current canvas version
        canvas_version = self.get_canvas_version(canvas_id) if use_cache else None
        
        # Flag to track if cache was used
        used_cache = False
        
        if use_cache:
            # print("**using cache for ", canvas_id)
            cache_key = self._get_cache_key(documents, canvas_id, override, canvas_version, run_id)
            cached_response = self._get_cached_response(cache_key)
            if cached_response:
                print("**using cache for ", canvas_id)
                # Mark that we used the cache
                used_cache = True
                # Add a metadata field to indicate this was served from cache
                cached_response["_cached"] = True
                return cached_response
        print("**not using cache for ", canvas_id)
        try:
            # print("v2")
            url = f"{self.api_url}/v2/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            }
            data = {
                "canvas_id": canvas_id,
                "variables": documents,
                "long_response": True,
            }
            # Check if any variables contain vault:// URLs and replace them with download URLs
            # Create a new data object with processed vault URLs
            import copy
            processed_data = copy.deepcopy(data)
            if "variables" in processed_data:
                print("**variables in processed data")
                for key, value in processed_data["variables"].items():
                    # Replace None values with empty string
                    if value is None:
                        print("**value is none")
                        processed_data["variables"][key] = ""
                    # Check if the value is a dictionary with file_url
                    elif isinstance(value, dict) and "file_url" in value and is_vault_url(value["file_url"]):
                        print("**is vault url", value["file_url"])
                        vault_file = VaultFile(value["file_url"], self.api_key)
                        value["file_url"] = vault_file.get_download_url()
                    # Check if the value is a list of dictionaries (like in 'files' payload)
                    elif isinstance(value, dict) and "files" in value and isinstance(value["files"], list):
                        print("**is list of files")
                        for file_item in value["files"]:
                            if isinstance(file_item, dict) and "file_url" in file_item and is_vault_url(file_item["file_url"]):
                                print("**is vault url", file_item["file_url"])
                                vault_file = VaultFile(file_item["file_url"], self.api_key)
                                file_item["file_url"] = vault_file.get_download_url()
            
            if override:
                processed_data["override"] = override
            # print(data)
            response = requests.post(url, headers=headers, data=json.dumps(processed_data))
            # print(response.json())
            if response.status_code != 200:
                print("**error on request", processed_data)
                print(response.status_code)
                print(response.json())
                return response.json()
            response_data = response.json()
            
            # Add a metadata field to indicate this was not from cache
            response_data["_cached"] = False
            
            if use_cache:
                self._cache_response(cache_key, response_data)
                
            return response_data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def new_canvas(self, canvas_id, expected_input=None):
        return Canvas(self, canvas_id, expected_input, self.max_attempts)


class Canvas:
    def __init__(self, tela_client, canvas_id, expected_input=None, max_attempts=3):
        self.canvas_id = canvas_id
        self.tela_client = tela_client
        self.expected_input = expected_input
        self.max_attempts = max_attempts

    def run(self, output_type='json', override=None, use_cache=True, run_id=None, **kwargs):
        documents = {}
        if self.expected_input:
            for i in self.expected_input:
                if i in kwargs:
                    documents[i] = kwargs[i]
                else:
                    raise ValueError(f"Missing expected input: {i}")
        else:
            documents = kwargs

        # Process any file inputs to handle vault URLs
        print("**documents", documents)
        for key, value in documents.items():
            if isinstance(value, dict) and "file_url" in value and is_vault_url(value["file_url"]):
                # Replace vault URL with download URL
                print("**is vault url", value["file_url"])
                vault_file = VaultFile(value["file_url"], self.tela_client.api_key)
                value["file_url"] = vault_file.get_download_url()

        attempts = 0
        response = None
        if override:
            print("**override", override)
            
        # Track if we used cache and measure execution time
        actually_used_cache = False
        start_time = datetime.now()
        
        while attempts < self.max_attempts:
            response = self.tela_client.request(documents, self.canvas_id, override, use_cache, run_id)
            if response and "choices" in response and len(response["choices"]) > 0:
                break
            attempts += 1
        
        # Calculate duration in milliseconds
        duration_ms = int((datetime.now() - start_time).total_seconds() * 1000)
        
        if response and "choices" in response and len(response["choices"]) > 0:
            content = response["choices"][0]["message"]["content"]
            
            # Check if cache was actually used
            if "_cached" in response:
                actually_used_cache = response["_cached"]
            
            # Log the request
            safe_documents = self._sanitize_for_logging(documents)
            self.tela_client.log_request(
                canvas_id=self.canvas_id,
                input_data=safe_documents,
                output=content if isinstance(content, str) else str(content)[:1000],
                used_cache=actually_used_cache,
                run_id=run_id,
                duration_ms=duration_ms
            )
            
            if output_type == 'dataframe':
                return self._json_to_dataframe(content)
            return content
        return None
        
    def _sanitize_for_logging(self, data):
        """Sanitize sensitive data for logging"""
        # Create a copy to avoid modifying the original
        import copy
        result = copy.deepcopy(data)
        
        # For simplicity, just truncate large values and remove file content
        for key, value in result.items():
            if isinstance(value, dict) and "file_url" in value:
                # Replace file content with just the URL reference
                if "file_url" in value and isinstance(value["file_url"], str) and len(value["file_url"]) > 100:
                    value["file_url"] = f"[file:{value['file_url'][:50]}...]"
            elif isinstance(value, str) and len(value) > 1000:
                result[key] = value[:1000] + "..."
                
        return result

    def run_batch(self, inputs, output_type='json', max_workers=5, use_cache=True):
        print("will run batch")
        from concurrent.futures import ThreadPoolExecutor, as_completed

        def process_input(index, input_data):
            print("running for")
            result = self.run(output_type=output_type, use_cache=use_cache, **input_data)
            print("finished running")
            return {'input': input_data.get('name', f'input_{index}'), 'result': result}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(process_input, i, input_data) for i, input_data in enumerate(inputs)]
            results = []
            for future in as_completed(futures):
                results.append(future.result())

        return results

    def _json_to_dataframe(self, json_data):
        def flatten_json(data, prefix=''):
            items = {}
            for key, value in data.items():
                new_key = f"{prefix}{key}"
                if isinstance(value, dict):
                    items.update(flatten_json(value, f"{new_key}_"))
                elif isinstance(value, list):
                    items[new_key] = json.dumps(value)
                else:
                    items[new_key] = value
            return items

        def process_json(data):
            if isinstance(data, dict):
                return [flatten_json(data)]
            elif isinstance(data, list):
                return [flatten_json(item) if isinstance(item, dict) else item for item in data]

        processed_data = process_json(json_data)
        df = pd.DataFrame(processed_data)

        # Expand columns that contain JSON strings (lists or list of objects)
        for column in df.columns:
            try:
                df[column] = df[column].apply(json.loads)
                if df[column].apply(lambda x: isinstance(x, list)).all():
                    if isinstance(df[column].iloc[0][0], dict):
                        # Handle list of objects
                        expanded_df = pd.json_normalize(df[column].explode().tolist())
                        expanded_df.index = df.index.repeat(df[column].str.len())
                        expanded_df.columns = [f"{column}_{subcol}" for subcol in expanded_df.columns]
                        df = df.drop(columns=[column]).join(expanded_df)
                    else:
                        # Handle simple lists
                        df = df.explode(column)
            except:
                pass

        return df


# EXAMPLE USAGE
# from tela.tela import TelaClient, file

# TELA_API_KEY = "Your API KEY"
# tela_client = TelaClient(TELA_API_KEY)

# canvas_id = "2b57f4ae-c48e-4883-a0a4-130a573ffdfc"
# canvas = tela_client.new_canvas(canvas_id, expected_input=['document'])

# FILE_NAME = "./Cartao CNPJ produtor.pdf"
# canvas.run(document=file(FILE_NAME))