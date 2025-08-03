# 🏛️ Court-Data Fetcher (CNR-Based)

A Flask mini-dashboard to fetch Indian court case status using CNR number from the official eCourts portal.

## 🚀 Features
- 🔍 Search court cases by 16-digit CNR number
- 🧾 View full details (status, judge, orders, etc.)
- 💾 Stores all queries in SQLite database
- ✅ No captcha / login required

## 📦 Tech Stack
- Python + Flask
- BeautifulSoup for scraping
- SQLite for storing logs

## 🔧 Run Locally

```bash
git clone https://github.com/yourusername/fetcher_court.git
cd fetcher_court
python -m venv venv
venv\Scripts\activate    # or source venv/bin/activate on Linux/mac
pip install -r requirements.txt
python run.py
