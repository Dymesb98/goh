
web3_provider = Web3(HTTPProvider('https://rinkeby.infura.io/v3/1c8e1333853b419f879ae4d9fc58cc61'))


addresslist = ["0xbd0fc0e8245D099b751CF6437cc32385347F2251"]
amount = [25]
to_addr = '0xDE9e1Ec15e962025d90062Ff02CdaB781272817A'
from_addr = '0x19B6158e215Af4DBDF0a30744bE9C1f048e0E4a6'
key = '0x2a2a730616f2f3230e97af69f7243b041863dcad2b8c02659eb1101ac0ca015b'
#
transaction = {
    'to': to_addr,
    'from': from_addr,
    'value': 100,
    'gas': 200000,
    'gasPrice': 100000000,
    'chainId': 42,
    # 'nonce': w3.eth.getTransactionCount(from_addr)
    'nonce': web3_provider.eth.getTransactionCount(from_addr)
    }
c = contract.function.start(addresslist, amount).buildransaction(transaction)
