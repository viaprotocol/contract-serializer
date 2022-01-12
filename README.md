# Contract Serializer
Microservice to extract structured information on EVM smart contract.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Why? 

Modern NFT contracts may have different names for `getPrice`, `mint` and `totalSupply` methods (or even be a property instead). So it is hard to extract the information and call methods - they just have different names!

The purpose of this tool is to extract NFT contract information in structured way with common names for same properties. 

## How does it work?
It basically utilises Etherscan API and parse Etherscan 'Read Contract' page using BS4.

# Example
Check deployed demo: https://contractserializer.herokuapp.com/. Open link to read the swagger docs.

## Get contract's static variables
GET https://cs.webill.io/137/0xbc1fe0f3b02ce5ff516f14ac7b79dd6397a54b9c/readcontract
Params: chain_id, contract_address
<details>
  <summary>Example response</summary>
  
```json
{
  "data": {
    "raw_data": {
      "DEVELOPER": "https://buildship.dev",
      "DEVELOPER_ADDRESS": "0x704c043ceb93bd6cbe570c6a2708c3e1c0310587",
      "MAX_SUPPLY": "10000",
      "MAX_TOKENS_PER_MINT": "20",
      "PROVENANCE_HASH": " ",
      "REFERRAL_PERCENT": "3000",
      "baseURI": "https://metadata.buildship.dev/api/token/moon/",
      "contractURI": "https://metadata.buildship.dev/api/token/moon/",
      "getPrice": "200000000000000000000",
      "getReservedLeft": "0",
      "name": "NFT Moon Metaverse",
      "owner": "0x197727ad2ec7326952843fbd83a0d57b907afbdf",
      "saleStarted": "True",
      "startingIndex": "0",
      "symbol": "MOON",
      "totalSupply": "178"
    },
    "serialized": {
      "nft_contract": {
        "price": 200000000000000000000,
        "total_supply": 178,
        "max_supply": 10000,
        "paused": false,
        "max_tokens_per_mint": 20,
        "base_uri": "https://metadata.buildship.dev/api/token/moon/"
      }
    }
  },
  "contract_address": "0xbc1fe0f3b02ce5ff516f14ac7b79dd6397a54b9c",
  "chain_id": 137
} 
```
</details>

## Get ABI of a contract in network
GET https://cs.webill.io/137/0xbc1fe0f3b02ce5ff516f14ac7b79dd6397a54b9c/abi
Params: chain_id, contract_address
Example response:


# Local development
1. Copy .env_template file to .env and fill it with your Etherscan creadentials.


2. Run fastapi server:
``` bash
uvicorn main:app --reload
```


---
<i>Made by [webill.io](https://webill.io) team</i>
