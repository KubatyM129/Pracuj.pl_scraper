from app import app
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas
import os
from flask import render_template
import requests
import json
from app.kek import extract_tag, selectors, sub_selectors
from urllib.request import Request, urlopen


def link_create(job,id):
      name = job.lower().replace(" ", "-").replace("/","")
      return f"https://www.pracuj.pl/praca/{name},oferta,{id}"

@app.route("/index")
def index(): 
    req = Request(
        url='https://it.pracuj.pl/praca/sta%C5%BC;kw', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    all_offers=[]
    page_number=1
    while(req):
        page_number+=1
        print(page_number)
        html = urlopen(req).read()
        soup = BeautifulSoup(html, "html.parser")
        offers = soup.select("div.tiles_b1j1pbod")
        for offer in offers:
            single_offer = {}
            for key, value in selectors.items():
                single_offer[key] = extract_tag(offer, *value)
                if key == "link" and single_offer[key] is None: 
                    print("yes")
                    single_offer["link"] = link_create(single_offer["job"],single_offer["offer_id"])    
            all_offers.append(single_offer)
        print(extract_tag(soup, "button.listing_n1mxvncp"))
        if extract_tag(soup, "button.listing_n1mxvncp") == "Następna":
            req = Request(
                url=f"https://it.pracuj.pl/praca/sta%C5%BC;kw?pn={page_number}", 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
        else:
            req = False
        with open(f"./app/offers.json", "w", encoding="UTF-8") as jf:
                    json.dump(all_offers, jf, indent=4, ensure_ascii=False)
                    
@app.route("/all_offers")
def products():
    return render_template('products.html')