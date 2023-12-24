from constants import DRIVERS_2024
from random import choice

def get_random_driver(drivers: dict = DRIVERS_2024) -> dict:
    driver_abb = choice(list(drivers.keys()))
    return {"Abb": driver_abb, "FullName": drivers[driver_abb]}