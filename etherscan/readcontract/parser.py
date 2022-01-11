import requests
from bs4 import BeautifulSoup

from etherscan.consts import ETHERSCAN_BASE_URL
from etherscan.readcontract.serializer import serialize_raw_data


def get_etherscan_readContract_html(contract_address, chain_id):
    res = requests.get(
        f"https://{ETHERSCAN_BASE_URL[chain_id]}/readContract?m=normal&a={contract_address}&v={contract_address}&t=false",
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        },
    )
    return res.text if "unable to retrieve a valid" not in res.text else None


def parse_etherscan_readContract_html(html):
    """ returns constants from contract """
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.find_all("div", attrs={"class":"card mb-3"})
    
    RAW = {}
    for item in items:  # parse items 
        if item.find("input"):
            continue  # dynamical thing

        title = item.find("div", class_="card-header").find("a").text
        name = title.split(".")[-1].strip()

        value = item.find("div", class_="card-body").find("div", class_="form-group").text.replace("\x00", "")
        # remove types from value
        value = value.rsplit(" ", maxsplit=1)[0]

        RAW[name] = value

    serialised = serialize_raw_data(RAW)
        
    return {
        "raw_data": RAW,
        "serialized": serialised,
    }

