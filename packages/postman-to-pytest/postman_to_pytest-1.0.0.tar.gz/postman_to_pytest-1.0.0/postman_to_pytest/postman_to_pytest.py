import json
import os
import argparse
import re
from urllib.parse import urlparse

def sanitize_name(name):
    """Convert API name to a valid Python identifier for test class/method names."""
    # Replace non-alphanumeric chars with underscore
    name = re.sub(r'\W+', '_', name)
    # Remove leading numbers/underscores
    name = re.sub(r'^[0-9_]+', '', name)
    # Ensure not empty
    if not name:
        name = "test"
    return name.lower()

def parse_request_url(url):
    """Parse URL to extract base URL and path."""
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    path = parsed.path
    return base_url, path

def generate_test_method(request, index):
    """Generate pytest test method for a request."""
    request_name = request.get("name", f"request_{index}")
    method_name = f"test_{sanitize_name(request_name)}"
    
    request_data = request.get("request", {})
    method = request_data.get("method", "GET")
    url = request_data.get("url", "")
    
    if isinstance(url, dict):
        url = url.get("raw", "")
    
    _, path = parse_request_url(url)
    
    # Extract headers
    headers = {}
    for header in request_data.get("header", []):
        headers[header.get("key")] = header.get("value")
    
    # Extract body
    body = None
    if "body" in request_data and request_data["body"].get("mode") == "raw":
        try:
            body_text = request_data["body"].get("raw", "{}")
            if "json" in request_data["body"].get("options", {}).get("raw", {}).get("language", "").lower():
                body = json.loads(body_text)
            else:
                body = body_text
        except:
            body = request_data["body"].get("raw", "{}")
    
    # Generate test method
    test_code = f"""
    def {method_name}(self, base_url, headers, org_token):
        \"\"\"Test {request_name}\"\"\"
"""
    
    # Add headers merging
    test_code += "        request_headers = headers.copy()\n"
    for key, value in headers.items():
        if key.lower() != 'content-type':  # Skip content-type as it's usually set in the base headers
            test_code += f"        request_headers[\"{key}\"] = \"{value}\"\n"
    
    # Add request code with proper params
    params = {}
    if "query" in request_data:
        for param in request_data.get("query", []):
            key = param.get("key")
            value = param.get("value")
            if "orgToken" in key or "token" in key.lower():
                params[key] = "org_token"
            else:
                params[key] = f"\"{value}\""
    
    # Add params to test code if exists
    if params:
        test_code += "        params = {\n"
        for key, value in params.items():
            test_code += f"            \"{key}\": {value},\n"
        test_code += "        }\n"
    
    # Add request with proper arguments
    test_code += f"        response = requests.{method.lower()}(\n"
    test_code += f"            f\"{{base_url}}{path}\",\n"
    test_code += f"            headers=request_headers,\n"
    
    if params:
        test_code += f"            params=params,\n"
    
    if body and method.upper() in ["POST", "PUT", "PATCH"]:
        if isinstance(body, dict):
            test_code += "            json={\n"
            for key, value in body.items():
                if isinstance(value, str):
                    test_code += f"                \"{key}\": \"{value}\",\n"
                else:
                    test_code += f"                \"{key}\": {value},\n"
            test_code += "            },\n"
        else:
            test_code += f"            data=\"{body}\",\n"
    
    test_code += "        )\n\n"
    
    # Add assertions
    test_code += "        assert response.status_code == 200\n"
    test_code += "        data = response.json()\n"
    if method.upper() in ["POST", "PUT", "PATCH"]:
        test_code += "        # Add your assertions based on expected response structure\n"
        test_code += "        # For example: assert \"id\" in data\n"
    else:
        test_code += "        # Add your assertions based on expected response structure\n"
        test_code += "        # For example: assert isinstance(data, list) or assert \"result\" in data\n"
    
    return test_code

def generate_test_class(folder_name, requests):
    """Generate a pytest test class for a folder of requests."""
    class_name = f"Test{sanitize_name(folder_name).title().replace('_', '')}"
    
    test_class = f"""import pytest
import requests
import json
import uuid
from datetime import datetime, timedelta

class {class_name}:
    \"\"\"Tests for {folder_name} API endpoints\"\"\"
"""
    
    for i, request in enumerate(requests):
        test_class += generate_test_method(request, i)
    
    return test_class

def process_folder(folder, output_dir):
    """Process a folder in the Postman collection."""
    folder_name = folder.get("name", "Unknown")
    requests = folder.get("item", [])
    
    # Filter out nested folders
    actual_requests = []
    for req in requests:
        if "request" in req:
            actual_requests.append(req)
    
    if actual_requests:
        file_name = f"test_{sanitize_name(folder_name)}_api.py"
        file_path = os.path.join(output_dir, file_name)
        
        with open(file_path, "w") as f:
            f.write(generate_test_class(folder_name, actual_requests))
        
        print(f"Generated {file_path}")
    
    # Process nested folders
    for item in requests:
        if "item" in item:
            process_folder(item, output_dir)

def create_conftest(output_dir):
    """Create a conftest.py file with common fixtures."""
    conftest_content = """import pytest
import os
import json
from dotenv import load_dotenv
import jwt
import datetime

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    \"\"\"Base URL for the API\"\"\"
    return os.getenv("API_BASE_URL", "http://localhost:9000")

@pytest.fixture(scope="session")
def jwt_token():
    \"\"\"Generate a JWT token for authentication\"\"\"
    secret = os.getenv("JWT_SECRET", "funnel-secret")
    
    # Prepare payload
    payload = {
        "iss": "funnel-wizard",
        "user_data": json.dumps({
            "fullName": "Test User",
            "email": "test@example.com",
            "id": 1,
            "extraData": None,
            "selectedOrg": {
                "token": "test-org-token",
                "domain": "test.ai",
                "name": "Test Org"
            }
        }),
        "exp": datetime.datetime.now().timestamp() + 3600  # Token expires in 1 hour
    }
    
    # Generate token
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

@pytest.fixture(scope="session")
def headers(jwt_token):
    \"\"\"Common headers for API requests\"\"\"
    return {
        "Authorization": f"Bearer {jwt_token}",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="session")
def org_token():
    \"\"\"Organization token for API requests\"\"\"
    return os.getenv("ORG_TOKEN", "test-org-token")
"""
    
    file_path = os.path.join(output_dir, "conftest.py")
    with open(file_path, "w") as f:
        f.write(conftest_content)
    
    print(f"Generated {file_path}")

def create_requirements(output_dir):
    """Create a requirements.txt file."""
    requirements_content = """pytest>=7.4.0
requests>=2.31.0
python-dotenv>=1.0.0
PyJWT>=2.8.0
"""
    
    file_path = os.path.join(output_dir, "requirements.txt")
    with open(file_path, "w") as f:
        f.write(requirements_content)
    
    print(f"Generated {file_path}")

def convert_postman_to_pytest(collection_path, output_dir):
    """Convert a Postman collection to pytest test files."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the Postman collection file
    with open(collection_path, "r") as f:
        collection = json.load(f)
    
    # Extract collection items
    items = collection.get("item", [])
    if not items and "collection" in collection:
        # Handle the format where the collection is inside a "collection" key
        items = collection.get("collection", {}).get("item", [])
    
    # Process each folder in the collection
    for item in items:
        if "item" in item:
            process_folder(item, output_dir)
    
    # Create common files
    create_conftest(output_dir)
    create_requirements(output_dir)
    
    print(f"Conversion complete. Test files generated in {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Postman collection to pytest tests")
    parser.add_argument("collection_path", help="Path to the Postman collection JSON file")
    parser.add_argument("--output", "-o", default="pytest_tests", help="Output directory for pytest files")
    
    args = parser.parse_args()
    convert_postman_to_pytest(args.collection_path, args.output)