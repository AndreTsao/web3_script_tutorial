# Web3撸毛脚本 🧵 演示代码

from web3 import Web3
from env import *

# Your Infura Project ID
INFURA_SECRET_KEY = ENV.INFURA_SECRET_KEY.value


# get w3 endpoint by network name
def get_w3_by_network(network='goerli'):
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}' # 接入 Infura 节点
    w3 = Web3(Web3.HTTPProvider(infura_url))
    return w3


def transfer_eth(w3,from_address,private_key,target_address,amount,gas_price=10,gas_limit=21000,chainId=5):
    from_address = Web3.toChecksumAddress(from_address)
    target_address = Web3.toChecksumAddress(target_address)
    nonce = w3.eth.getTransactionCount(from_address) # 获取 nonce 值
    params = {
        'from': from_address,
        'nonce': nonce,
        'to': target_address,
        'value': w3.toWei(amount, 'ether'),
        'gas': gas_limit,
        #'gasPrice': w3.toWei(gas_price, 'gwei'),
        'maxFeePerGas': w3.toWei(gas_price, 'gwei'),
        'maxPriorityFeePerGas': w3.toWei(gas_price, 'gwei'),
        'chainId': chainId,
        
    }
    try:
        signed_tx = w3.eth.account.signTransaction(params, private_key=private_key)
        txn = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return {'status': 'succeed', 'txn_hash': w3.toHex(txn), 'task': 'Transfer ETH'}
    except Exception as e:
        return {'status': 'failed', 'error': e, 'task': 'Transfer ETH'}


def main():

    # 🐳 Task 2: ETH 转账

    # 接入 goerli Testnet
    w3 = get_w3_by_network('goerli')

    # 测试地址
    from_address = ENV.From_Address.value

    print(f'当前地址余额----------: {from_address} ')

    # 测试私钥， 千万不能泄漏你自己的私钥信息
    private_key = ENV.Private_Key.value

    # 测试转入地址
    target_address = ENV.Target_Address.value

    # 转账 ETH 金额
    amount = 0.0012

    # goerli Chain ID
    chainId = 5

    # 查询地址 ETH余额
    balance = w3.eth.get_balance(from_address) / 1e18
    print(f'当前地址余额: {balance = } ETH')

    result = transfer_eth(w3, from_address, private_key, target_address, amount, chainId=chainId)
    print(result)
    

if __name__ == "__main__":
    main()
