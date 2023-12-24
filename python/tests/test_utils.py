import pytest
import discord
from src.utils import get_random_driver
from src.constants import DRIVERS_2024


def test_get_random_driver():
    result = get_random_driver()
    assert result["Abb"] in DRIVERS_2024
    assert result["FullName"] in DRIVERS_2024.values()
