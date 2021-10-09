from brownie import network, accounts, config


LOCAL_DEVELOPMENT = ["development"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id=id)
    if network.show_active() in LOCAL_DEVELOPMENT:
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])
