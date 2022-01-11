
def find_nft_contract_properties(r):
    RES = {}

    # NFT PRICE
    if "getPrice" in r:
        RES["price"] = int(r["getPrice"])
    elif "cost" in r:
        RES["price"] = int(r["cost"])

    if "totalSupply" in r:
        RES["total_supply"] = int(r["totalSupply"])

    if "MAX_SUPPLY" in r:
        RES["max_supply"] = int(r["MAX_SUPPLY"])
    elif "maxSupply" in r:
        RES["max_supply"] = int(r["maxSupply"])
        

    if "saleStarted" in r:
        RES["sale_started"] = bool(r["saleStarted"])
    elif "paused" in r:
        RES["sale_started"] = not bool(r["paused"])

    
    if "maxMintAmount" in r:
        RES["max_tokens_per_mint"] = int(r["maxMintAmount"])
    elif "MAX_TOKENS_PER_MINT" in r:
        RES["max_tokens_per_mint"] = int(r["MAX_TOKENS_PER_MINT"])

    if "baseURI" in r:
        RES["base_uri"] = r["baseURI"]

    return RES
    

def serialize_raw_data(r):
    RES = {}

    nft_contract_properties = find_nft_contract_properties(r)
    if nft_contract_properties:
        RES["nft_contract"] = nft_contract_properties

    return RES