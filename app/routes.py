from flask import Blueprint, render_template, request
from scraper.fetch import fetch_case_by_cnr
import sqlite3

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        cnr = request.form['cnr'].strip()
        result = fetch_case_by_cnr(cnr)

        # Save to database
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS cnr_logs (cnr TEXT, result TEXT)')
        c.execute('INSERT INTO cnr_logs VALUES (?, ?)', (cnr, result))
        conn.commit()
        conn.close()

    return render_template('index.html', result=result)
