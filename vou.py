
web3_provider = Web3(HTTPProvider('https://rinkeby.infura.io/v3/1c8e1333853b419f879ae4d9fc58cc61'))


addresslist = ["0xbd0fc0e8245D099b751CF6437cc32385347F2251"]
amount = [25]
to_addr = '0xbd0fc0e8245D099b751CF6437cc32385347F2251'
from_addr = '0x19B6158e215Af4DBDF0a30744bE9C1f048e0E4a6'
key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
#
transaction = {
    'to': to_addr,
    'from': from_addr,
    'value': 100,
    'gas': 200000,
    'gasPrice': 100000000,
    'chainId': 4,
    # 'nonce': w3.eth.getTransactionCount(from_addr)
    'nonce': web3_provider.eth.getTransactionCount(from_addr)
    }
c = contract.function.start(addresslist, amount).buildransaction(transaction)
