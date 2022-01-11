import os
import requests

from etherscan.consts import (
    ETHERSCAN_BASE_URL, 
    ETHERSCAN_CHAIN_ID_TO_ENV_API_TOKEN_NAME,
)


def get_abi(chain_id, contract_address):
    api_token = os.getenv(ETHERSCAN_CHAIN_ID_TO_ENV_API_TOKEN_NAME[chain_id])
    res = requests.get(
        f"https://api.{ETHERSCAN_BASE_URL[chain_id] }/api?module=contract&action=getabi&address={contract_address}&apikey={api_token}",
    )

    # TODO: handle not found
    return res.json()