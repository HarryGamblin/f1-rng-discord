import gsheets
import pathlib
import json
from constants import SPREADSHEET_ID

def _get_json_credentials(json_file):
    with open(json_file, 'r') as output:
        return json.load(output)

cwd = pathlib.Path.cwd()

credentials = _get_json_credentials(f"{cwd}/credentials.json")

sheets = gsheets.Sheets(credentials=credentials)

sheets.get(SPREADSHEET_ID)