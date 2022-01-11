import os
import json
import requests

from etherscan.consts import (
    ETHERSCAN_BASE_URL, 
    ETHERSCAN_CHAIN_ID_TO_ENV_API_TOKEN_NAME,
)

from etherscan.api.abi.serializer import serialize_raw_abi


def get_abi(chain_id, contract_address):
    api_token = os.getenv(ETHERSCAN_CHAIN_ID_TO_ENV_API_TOKEN_NAME[chain_id])
    res = requests.get(
        f"https://api.{ETHERSCAN_BASE_URL[chain_id]}/api?module=contract&action=getabi&address={contract_address}&apikey={api_token}",
    )

    result = res.json()
    if not result.get("result"):
        return None  # can't find abi


    abi_dict = json.loads(result["result"])
    serialized = serialize_raw_abi(abi_dict)
    return {
        "serialized": serialized,
        "abi": abi_dict,
    }

    