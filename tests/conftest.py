import pytest
from dotenv import load_dotenv

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    # setup environment
    print("Setting up environment")
    load_dotenv('tests/.env.test')
    yield
    # clean up environment
    print("Cleaning up environment")
