# Contract Serializer
Microservice to extract structured information on EVM smart contract.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Why? 

Modern NFT contracts may have different names for `getPrice`, `mint` and `totalSupply` methods (or even be a property instead). So it is hard to extract the information and call methods - they just have different names!

The purpose of this tool is to extract NFT contract information in structured way with common names for same properties. 

## How does it work?
It basically utilises Etherscan API and parse Etherscan 'Read Contract' page using BS4.

# Local development
``` bash
uvicorn main:app --reload
```
