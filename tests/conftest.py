import pytest
from dotenv import load_dotenv
import os

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    # setup environment
    print("Setting up environment")
    os.environ.clear()
    load_dotenv(dotenv_path="tests/.env.test")
    yield
    # clean up environment
    print("Cleaning up environment")
