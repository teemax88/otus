import pytest
import random

@pytest.fixture()
def fixture_len_list():
    items_list = [item for item in range(1, 5)]
    return len(items_list)


@pytest.fixture()
def fixture_string():
    word_one = "Hello"
    word_two = "World"
    return f'{word_one} {word_two}'


@pytest.fixture()
def fixture_float():
    value = [3.14, 5.65, 5.00, 8.99]
    return random.choice(value)


@pytest.fixture()
def fixture_float():
    value = [3.14, 5.65, 5.00, 8.99]
    return random.choice(value)
