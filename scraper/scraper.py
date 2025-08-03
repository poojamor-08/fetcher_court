import requests
from bs4 import BeautifulSoup

def fetch_case_data():
    url = "https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract specific elements you want here
        return soup.prettify()
    else:
        return "Failed to fetch data"
