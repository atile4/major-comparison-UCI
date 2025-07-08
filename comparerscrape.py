import requests
from bs4 import BeautifulSoup
import regex as re

def make_table_list(website : str) -> list | list: 
    r = requests.get(website)
    soup = BeautifulSoup(r.text, 'html.parser')
    course_table1 = soup.find('table', class_ ='sc_courselist')
    rows = course_table1.find_all('tr')

    table_list = []
    course_list = []

    for row in rows:
        cols = row.find_all('td')
        first_col = cols[0].get_text(strip=True).replace("\xa0", " ")
        if len(cols) == 1:
            table_list.append(first_col)
        else:
            title = cols[1].get_text(strip=True)
            table_list.append(first_col + " : " + title)
            course_list.append(first_col + " : " + title)
    return (table_list, course_list)

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


