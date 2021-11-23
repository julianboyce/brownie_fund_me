from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if (
        len(MockV3Aggregator) >= 0
    ):  # MockV3Aggregator is a list of all deploy V3 contracts
        MockV3Aggregator.deploy(
            DECIMALS,
            # Web3.toWei(STARTING_PRICE, "ether"),
            STARTING_PRICE,
            {"from": get_account()},  # toWei with ether adds 18 decimals
        )
    print("Mocks deployed!")