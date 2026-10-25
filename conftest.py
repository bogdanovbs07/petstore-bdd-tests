import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://petstore.swagger.io/v2",
        help="Base URL for Petstore API"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture
def api_client(base_url):
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session, base_url
