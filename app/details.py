from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
from app.kek import extract_tag, sub_selectors
from urllib.request import Request, urlopen



def detail_extraction():
    req = Request(
    url='https://www.pracuj.pl/praca/praktyki-java--salesforce,oferta,1003328961', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
    all_details=[]
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    details = soup.select(".o1eg7akv")
    for detail in details:
        single_detail = {}
        for key, value in sub_selectors.items():
            single_detail[key] = extract_tag(detail, *value)
        all_details.append(single_detail)
    with open(f"./app/details.json", "w", encoding="UTF-8") as jf:
        json.dump(all_details, jf, indent=4, ensure_ascii=False)

detail_extraction()



