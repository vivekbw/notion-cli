import os
import pytest
from notion_cli.notion_wrapper import clear_database


def pytest_configure(config):
    """Sets PYTEST_ENVIRONMENT to True before Running Test Suite"""
    os.environ["PYTEST_ENVIRONMENT"] = "True"


@pytest.fixture(scope="session", autouse=True)
def empty_database():
    """Clears the entire TEST_DATABASE before each Test Suite"""
    yield
    clear_database()
