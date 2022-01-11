

def find_mint_method(ABI):
    """
        Tries to find the 'mint' method in ABI
    """
    candidates = [
        c
        for c in ABI 
        if c.get("stateMutability") == "payable"
        and c.get("type") == "function"
        and "mint" in (c.get("name") or "").lower()
    ]
    
    print("mint candidates:", len(candidates))
    if len(candidates) == 0:
        raise Exception("Can't find 'mint' methods in contract")
    
    # classic mint should have 1 param: number of nfts to buy
    with_one_int_argument = [
        c 
        for c in candidates 
        if len(c["inputs"]) == 1 
        and "int" in c["inputs"][0]["type"]
    ]
    print("with one int argument:", len(with_one_int_argument))
    if len(with_one_int_argument) == 1:
        return with_one_int_argument[0]
    
    raise Exception(f"Can't find a proper 'mint' method among {len(candidates)} candidates")


def serialize_raw_abi(ABI):
    RES = {}

    try:
        mint_method = find_mint_method(ABI)
    except Exception as e:
        mint_method = {"error": str(e)}

    RES["mint_method"] = mint_method
    return RES
    