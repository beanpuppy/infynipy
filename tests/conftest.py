import os
import pytest

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def env_default(key):
    """Return environment variable or placeholder string"""
    return os.environ.get(
        "infynipytest_{}".format(key), "placeholder_{}".format(key)
    )


placeholders = {
    "username": env_default("username"),
    "api_key": env_default("api_key"),
    "broker_id": env_default("broker_id"),
}


class Placeholders:
    def __init__(self, _dict):
        self.__dict__ = _dict


def pytest_configure():
    pytest.placeholders = Placeholders(placeholders)
