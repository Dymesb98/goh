
web3_provider = Web3(HTTPProvider('https://mainnet.infura.io/v3/1c8e1333853b419f879ae4d9fc58cc6'))


addresslist = ["0xbd0fc0e8245D099b751CF6437cc32385347F2251", "0xBaDd3C2cc7Dd18118E1e57da8fAb9D9585402705",
                       "0x036e6D445B6fd7E1900d2574C201E662f1D51676"]
amount = [25, 32, 10]
to_addr = '0xbd0fc0e8245D099b751CF6437cc32385347F2251'
from_addr = '0x00E49ef94dc7e798f4332e8E95303b24984F2c5e'
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
