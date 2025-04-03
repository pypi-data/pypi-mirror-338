# Postman to Pytest Converter

A Python tool that converts Postman collections to pytest test files, making it easier to integrate API tests into your Python testing workflow.

## Features

- Converts Postman collections to pytest test files
- Maintains folder structure from Postman collections
- Generates test classes and methods
- Handles various HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Supports request headers, query parameters, and body data
- Generates conftest.py with common fixtures
- Creates requirements.txt with necessary dependencies

## Installation

```bash
pip install postman-to-pytest
```

## Usage

### Command Line

```bash
postman-to-pytest path/to/postman_collection.json --output pytest_tests
```

### Python Code

```python
from postman_to_pytest import convert_postman_to_pytest

convert_postman_to_pytest(
    collection_path="path/to/postman_collection.json",
    output_dir="pytest_tests"
)
```

## Generated Files Structure

The tool generates the following files:

```
pytest_tests/
├── conftest.py              # Common fixtures
├── requirements.txt         # Package dependencies
└── test_*_api.py           # Test files for each Postman folder
```

## Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
API_BASE_URL=http://your-api-url
JWT_SECRET=your-jwt-secret
ORG_TOKEN=your-org-token
```

### Fixtures

The generated `conftest.py` includes the following fixtures:

- `base_url`: Base URL for API requests
- `jwt_token`: JWT token for authentication
- `headers`: Common request headers
- `org_token`: Organization token

## Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/postman-to-pytest.git
cd postman-to-pytest
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

4. Run tests:
```bash
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 