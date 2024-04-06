import json


def read_abi(fname: str) -> dict:
    with open(fname, "r") as f:
        abi = json.load(f)
    return abi
