from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    print(account)
    # if we are on a persistant network like rinkeby, use the asscociated address
    # otherwise use mocks
    # publish_source not working. might be a compiler version issue
    # The AggregatorInterface and the contract are not using the same compiler version
    # You can use the .get() syntax for reading from the config file in case you
    #   forget to add the verify to the config
    # fund_me = FundMe.deploy({"from": account}, publish_source=config["networks"][network.show_active].get("verify"))
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed_address"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[
            -1
        ].address  # Take last deploy V3 contract

    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    # print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
