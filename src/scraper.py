"""A little baby data scrapper."""
import requests
import sys
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
    """Send GET request to King County Health Inspection API.

    The request will use the kwargs to fill out the requests parameters as the
    user specifies and fill in any unspecified ones with any required default
    values.
    """
    new_params = PAYLOAD.copy()
    new_params.update(kwargs)
    response = requests.get(URL, params=new_params)
    response.raise_for_status()
    return response.content, response.encoding


def load_inspection_page():
    """Open the inspection_page.html and read it.

    The purpose of this function is to keep the user from having to make
    repeated requests at the KCHI API which has a tendency to not like
    the attention. It will return a bytes version and a string version
    of the HTML.
    """
    with open('inspection_page.html') as f:
        content = f.read()
        return content


def parse_source(content):
    """."""
    parsed = BeautifulSoup(content, "lxml")
    return parsed

if __name__ == "__main__":
    kwargs = {
        "Zip_Code": "98116",
        "City": "Seattle"
    }
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        content = load_inspection_page()
    else:
        content, encoding = get_inspection_page(**kwargs)
    doc = parse_source(content)
    print(doc.prettify())
