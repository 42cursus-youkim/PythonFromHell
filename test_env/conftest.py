import pytest


@pytest.fixture
def main():
    return lambda: print("Hello World!" * 10)

