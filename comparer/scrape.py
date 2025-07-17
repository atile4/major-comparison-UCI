import requests
from bs4 import BeautifulSoup
import regex as re

def getTable(website : str) -> list:
    r = requests.get(website)
    soup = BeautifulSoup(r.text, 'html.parser')
    course_table = soup.find('table', class_ ='sc_courselist')
    rows = course_table.find_all('tr')
    return rows

def getMajors():
    r = requests.get("https://catalogue.uci.edu/undergraduatedegrees/")
    soup = BeautifulSoup(r.text, 'html.parser')
    anchors = soup.find_all('a', href=True)

    pattern = re.compile(r"_(ba|bs|bfa|bed)/$")

    majors = {}
    for a in anchors:
        href = a['href']
        text = a.get_text(strip=True)
        mod_text = text[0:len(text)-6].lower()

        if pattern.search(href) and text and mod_text not in majors:
            majors[text[0:len(text)-6].lower()] = f"https://catalogue.uci.edu{href}"
            
    return majors
