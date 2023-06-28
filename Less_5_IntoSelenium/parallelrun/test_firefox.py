from application import Application
import pytest
from my_test import TestSuit


@pytest.fixture(scope='function')
def app():
    return Application('firefox')
