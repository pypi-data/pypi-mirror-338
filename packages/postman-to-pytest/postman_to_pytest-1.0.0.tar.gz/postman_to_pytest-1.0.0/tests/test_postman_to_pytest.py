import pytest
import json
import os
import tempfile
from postman_to_pytest import (
    sanitize_name,
    parse_request_url,
    generate_test_method,
    generate_test_class,
    process_folder,
    create_conftest,
    create_requirements,
    convert_postman_to_pytest
)

def test_sanitize_name():
    # Test basic name sanitization
    assert sanitize_name("Test API") == "test_api"
    assert sanitize_name("123Test") == "test"
    assert sanitize_name("Test-API") == "test_api"
    assert sanitize_name("Test@API") == "test_api"
    assert sanitize_name("") == "test"

def test_parse_request_url():
    # Test URL parsing
    base_url, path = parse_request_url("https://api.example.com/v1/users")
    assert base_url == "https://api.example.com"
    assert path == "/v1/users"

    base_url, path = parse_request_url("http://localhost:8000/api")
    assert base_url == "http://localhost:8000"
    assert path == "/api"

def test_generate_test_method():
    # Test test method generation
    request = {
        "name": "Get Users",
        "request": {
            "method": "GET",
            "url": "https://api.example.com/users",
            "header": [
                {"key": "Content-Type", "value": "application/json"}
            ]
        }
    }
    
    test_code = generate_test_method(request, 0)
    assert "def test_get_users" in test_code
    assert "response = requests.get" in test_code
    assert "assert response.status_code == 200" in test_code

def test_generate_test_class():
    # Test test class generation
    folder_name = "User Management"
    requests = [{
        "name": "Get Users",
        "request": {
            "method": "GET",
            "url": "https://api.example.com/users"
        }
    }]
    
    test_class = generate_test_class(folder_name, requests)
    assert "class TestUserManagement" in test_class
    assert "import pytest" in test_class
    assert "import requests" in test_class

def test_process_folder():
    # Test folder processing
    with tempfile.TemporaryDirectory() as temp_dir:
        folder = {
            "name": "Test Folder",
            "item": [{
                "name": "Test Request",
                "request": {
                    "method": "GET",
                    "url": "https://api.example.com/test"
                }
            }]
        }
        
        process_folder(folder, temp_dir)
        assert os.path.exists(os.path.join(temp_dir, "test_test_folder_api.py"))

def test_create_conftest():
    # Test conftest.py creation
    with tempfile.TemporaryDirectory() as temp_dir:
        create_conftest(temp_dir)
        conftest_path = os.path.join(temp_dir, "conftest.py")
        assert os.path.exists(conftest_path)
        
        with open(conftest_path, "r") as f:
            content = f.read()
            assert "@pytest.fixture" in content
            assert "base_url" in content
            assert "jwt_token" in content
            assert "headers" in content
            assert "org_token" in content

def test_create_requirements():
    # Test requirements.txt creation
    with tempfile.TemporaryDirectory() as temp_dir:
        create_requirements(temp_dir)
        requirements_path = os.path.join(temp_dir, "requirements.txt")
        assert os.path.exists(requirements_path)
        
        with open(requirements_path, "r") as f:
            content = f.read()
            assert "pytest==" in content
            assert "requests==" in content
            assert "python-dotenv==" in content
            assert "PyJWT==" in content

def test_convert_postman_to_pytest():
    # Test full conversion process
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a sample Postman collection
        collection = {
            "item": [{
                "name": "Test Folder",
                "item": [{
                    "name": "Test Request",
                    "request": {
                        "method": "GET",
                        "url": "https://api.example.com/test"
                    }
                }]
            }]
        }
        
        collection_path = os.path.join(temp_dir, "test_collection.json")
        with open(collection_path, "w") as f:
            json.dump(collection, f)
        
        output_dir = os.path.join(temp_dir, "output")
        convert_postman_to_pytest(collection_path, output_dir)
        
        # Verify output files
        assert os.path.exists(os.path.join(output_dir, "test_test_folder_api.py"))
        assert os.path.exists(os.path.join(output_dir, "conftest.py"))
        assert os.path.exists(os.path.join(output_dir, "requirements.txt")) 