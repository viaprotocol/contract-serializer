from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException

from etherscan.consts import ETHERSCAN_BASE_URL
from etherscan.readcontract.parser import (
    get_etherscan_readContract_html,
    parse_etherscan_readContract_html,
)
from etherscan.api.abi.abi import get_abi

app = FastAPI()

load_dotenv()


@app.get("/{chain_id}/{contract_address}/readcontract")
async def etherscan_readcontract(chain_id: int, contract_address: str):
    if chain_id not in ETHERSCAN_BASE_URL:
        raise HTTPException(status_code=404, detail="Can't work with that chain_id")

    _DEFAULT_DATA = {"contract_address": contract_address, "chain_id": chain_id}

    html = get_etherscan_readContract_html(contract_address, chain_id)
    if html is None:
        raise HTTPException(status_code=404, detail="Unable to retrieve a valid contract. Maybe it doesn't exist on that network.")

    data = parse_etherscan_readContract_html(html)
    return {"data": data, **_DEFAULT_DATA}


@app.get("/{chain_id}/{contract_address}/abi")
async def etherscan_get_abi(chain_id: int, contract_address: str):
    if chain_id not in ETHERSCAN_BASE_URL:
        raise HTTPException(status_code=404, detail="Can't work with that chain_id")
    
    abi = get_abi(chain_id, contract_address)
    if abi:
        return abi
    
    raise HTTPException(status_code=404, detail="Unable to retrieve a valid contract and find ABI.")
