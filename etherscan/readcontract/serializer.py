
def find_nft_contract_properties(r):
    RES = {}

    # NFT PRICE
    if "getPrice" in r:
        RES["price"] = int(r["getPrice"])
    elif "cost" in r:
        RES["price"] = int(r["cost"])
    elif "baseCost" in r:
        RES["price"] = int(r["baseCost"])

    if "totalSupply" in r:
        RES["total_supply"] = int(r["totalSupply"])

    if "MAX_SUPPLY" in r:
        RES["max_supply"] = int(r["MAX_SUPPLY"])
    elif "maxSupply" in r:
        RES["max_supply"] = int(r["maxSupply"])
    elif "_maxTotalSupply" in r:
        RES["max_supply"] = int(r["_maxTotalSupply"])
        

    if "saleStarted" in r:
        RES["paused"] = r["saleStarted"] == "False"
    elif "paused" in r:
        RES["paused"] = r["paused"] == "True"
    elif "_paused" in r:
        RES["paused"] = r["_paused"] == "True"

    
    if "maxMintPerTransaction" in r:
        RES["max_tokens_per_mint"] = int(r["maxMintPerTransaction"])  
    elif "maxMintAmount" in r:  # ???? should we add max tokens per user separately?
        RES["max_tokens_per_mint"] = int(r["maxMintAmount"])
    elif "MAX_TOKENS_PER_MINT" in r:
        RES["max_tokens_per_mint"] = int(r["MAX_TOKENS_PER_MINT"])
    elif "nftPerAddressLimit" in r:
        RES["max_tokens_per_mint"] = int(r["nftPerAddressLimit"])
        

    if "baseURI" in r:
        RES["base_uri"] = r["baseURI"]

    return RES
    

def serialize_raw_data(r):
    RES = {}

    nft_contract_properties = find_nft_contract_properties(r)
    if nft_contract_properties:
        RES["nft_contract"] = nft_contract_properties

    return RES