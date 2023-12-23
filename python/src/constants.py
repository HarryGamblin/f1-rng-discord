from enum import Enum
from dotenv import load_dotenv
import os

load_dotenv()

BOT_NAME = "F1-RNG-Bot"

MESSAGE_PREFIX = "f1-rng"

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

DRIVERS_2024 = {"VER": "Max Verstappen", "PER": "Sergio Perez",
                "HAM": "Lewis Hamilton", "RUS": "George Russell",
                "LEC": "Charles Leclerc", "SAI": "Carlos Sainz",
                "NOR": "Lando Norris", "PIA": "Oscar Piastri",
                "ALO": "Fernando Alonso", "STR": "Lance Stroll",
                "GAS": "Pierre Gasly", "OCO": "Esteban Ocon",
                "ALB": "Alex Albon", "SAR": "Logan Sargeant",
                "TSU": "Yuki Tsunoda", "RIC": "Daniel Ricciardo",
                "BOT": "Valtteri Bottas", "ZHO": "Zhou Guanyu",
                "HUL": "Nico Hulkenberg", "MAG": "Kevin Magnussen"}

class CommandNames(Enum):
    register = "register"