
import time
import logging
from typing import Any
from hexbytes import HexBytes
import colorlog
import logging

from utils.constants import DEFAULT_GAS, DEFAULT_GAS_PRICE

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)

handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "bold_red",
        "CRITICAL": "bold_red",
    },
)

handler.setFormatter(formatter)
logger.addHandler(handler)


def check_transaction_status(web3_client, txn_hash) -> int:
    # Wait for the transaction to be mined
    while True:
        try:
            txn_receipt = web3_client.eth.get_transaction_receipt(txn_hash)
            if txn_receipt is not None:
                break
            time.sleep(5)  # Wait for 5 seconds before checking again
        except Exception as e:
            logging.error(f"Error checking transaction status {e}")

    # Check if the transaction was successful
    return int(txn_receipt["status"])

def build_and_send_transaction(
    web3_client,
    contract_address: str,
    function_name: str,
    abi: str,
    account_address: str,
    private_key: str,
    function_args: tuple,
    scan_url: str = "https://sepolia.arbiscan.io/tx/",
    gas: int = DEFAULT_GAS,
    gas_price: int = DEFAULT_GAS_PRICE,
    lz_value: float = 0,
) -> None:
    contract = web3_client.eth.contract(
        address=web3_client.to_checksum_address(contract_address), abi=abi
    )

    # Build the transaction
    transaction = contract.functions[function_name](*function_args).build_transaction(
        {
            "from": account_address,
            "nonce": web3_client.eth.get_transaction_count(account_address),
            # "gas": gas, # re-enable if you don't want it to automatically match network gas
            "gasPrice": gas_price,
            "value": web3_client.to_wei(lz_value, "ether"),
        }
    )

    # Sign the transaction
    signed_txn = web3_client.eth.account.sign_transaction(transaction, private_key)

    # Send the transaction
    txn_hash = web3_client.eth.send_raw_transaction(signed_txn.rawTransaction)
    time.sleep(1)
    status = check_transaction_status(web3_client, txn_hash)
    if status:
        logging.info(
            f"{function_name} - Transaction sent: {scan_url}{txn_hash.hex()} with status: {status}"
        )
    else:
        logging.error(
            f"{function_name} - Transaction failed: {scan_url}{txn_hash.hex()} with status: {status}"
        )
