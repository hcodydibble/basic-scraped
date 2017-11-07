"""A little baby data scrapper."""
import requests
from bs4 import BeautifulSoup


URL = "http://info.kingcounty.gov/health/ehs/foodsafety/inspections/Results.aspx"
PAYLOAD = {"Business_Name": "",
           "Business_Address": "",
           "Longitude": "",
           "Latitude": "",
           "City": "",
           "Zip_Code": "",
           "Inspection_Type": "All",
           "Inspection_Start": "",
           "Inspection_End": "",
           "Inspection_Closed_Business": "A",
           "Violation_Points": "",
           "Violation_Red_Points": "",
           "Violation_Descr": "",
           "Fuzzy_Search": "N",
           "Sort": "B"}


def get_inspection_page(**kwargs):
    """."""
    new_params = PAYLOAD.copy()
    new_params.update(kwargs)
    response = requests.get(URL, params=new_params)
    response.raise_for_status()
    return response.content, response.encoding


def load_inspection_page():
    """."""
    with open('inspection_page.html') as f:
        content = f.read().encode('utf8')
        encoding = f.read()
        return content, encoding


def parse_source(html):
    """."""
    return BeautifulSoup(html, "lxml")
