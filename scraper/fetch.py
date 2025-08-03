import requests
from bs4 import BeautifulSoup

def fetch_case_by_cnr(cnr):
    try:
        session = requests.Session()
        url = "https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index"
        post_url = "https://services.ecourts.gov.in/ecourtindia_v6/cases/case_no"

        payload = {
            "cnrno": cnr,
            "submit": "Search"
        }

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": url
        }

        res = session.post(post_url, data=payload, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        case_table = soup.find("table", class_="table table-striped table-bordered")
        if not case_table:
            return "⚠️ No case found. Please check the CNR number."

        return case_table.get_text(separator='\n', strip=True)

    except Exception as e:
        return f"❌ Error occurred: {str(e)}"
