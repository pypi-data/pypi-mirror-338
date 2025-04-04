

import pandas as pd
import json

class SheetsManager:
    # Class-level variables to store the URL and sheet data
    sheet_url = ""
    sheet_data = {}

    """
    A class to manage and load Google Sheets data from all tabs.

    Attributes:
        sheet_url (str): The URL of the Google Sheet.
        sheet_data (dict): A dictionary to store the data loaded from all tabs.
    """

    @staticmethod
    def init(sheet_id: str, force_string=False):
        """
        Initialize the SheetsManager with a Google Sheet ID.

        This method constructs the Google Sheets URL for the given sheet_id
        and initializes an empty dictionary to store the sheet data.

        Args:
            sheet_id (str): The ID of the Google Sheet to load data from.
        """
        SheetsManager.sheet_url = f"https://docs.google.com/spreadsheets/d/e/{sheet_id}/pub?output=xlsx"
        SheetsManager.force_string = force_string
        SheetsManager.reload(force_string=False)

    @staticmethod
    def reload():
        """
        Load data from all tabs in the Google Sheet.

        This method fetches the data from the Google Sheets URL and loads all tabs into 
        a dictionary. Each key in the dictionary corresponds to a tab name, and the 
        value is a list of records in JSON format.

        Raises:
            ValueError: If there is an issue loading the data (e.g., network issues, wrong URL).
        """
        try:
            xls = pd.ExcelFile(SheetsManager.sheet_url)
            data = {}
            
            for sheet_name in xls.sheet_names:
                rows_data = pd.read_excel(xls, sheet_name, dtype="string" if SheetsManager.force_string else None)
                rows_data = json.loads(rows_data.to_json(orient='records'))
                
                data[sheet_name] = rows_data
                
            SheetsManager.sheet_data = data
        
        except Exception as e:
            raise ValueError(f"Error loading data from spreadsheet: {e}")


