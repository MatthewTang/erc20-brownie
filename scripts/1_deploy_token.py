from brownie import OurToken, config, network
from scripts.helpful_script import get_account
from web3 import Web3

INITIAL_SUPPLY = 1000000000000000000000
initial_supply = Web3.toWei(1000, "ether")


def deploy_contract():
    account = get_account()
    our_token = OurToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(our_token.balanceOf(account.address))


def main():
    deploy_contract()
