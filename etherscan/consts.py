ETHERSCAN_BASE_URL = {
    # chain_id --> base URL for API, parsing & more
    1: "etherscan.io",
    56: "bscscan.com",
    137: "polygonscan.com",

    # TODO: add testnets
}


ETHERSCAN_CHAIN_ID_TO_ENV_API_TOKEN_NAME = {
    1: "ETHERSCAN_API_KEY",
    56: "BSCSCAN_API_KEY",
    137: "POLYGONSCAN_API_KEY",
}