import json
from eth_account import Account
from web3 import Web3
import csv

#写入wallets.csv文件
def saveETHWalletInCsv(jsonData):
    with open('wallets.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["序号", "钱包地址", "私钥", "助记词"])
        csv_writer.writerows(jsonData)
    

def read_wallets_and_callback(csv_path, callback):
    print("---- 开始读取钱包 ----")
    with open(csv_path) as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for each_wallet in f_csv:
            callback(each_wallet)


def create_new_wallet(self):
    Account.enable_unaudited_hdwallet_features()
    account = Account.create()
    privateKey = str.lower(self.bytes_to_hex(account.key))
    address = account.address
    return address, privateKey


def bytes_to_hex(bs):
    return ''.join(['%02X' % b for b in bs])

# 批量创建私钥与地址  同一助记词对应多个钱包地址
def create_new_wallet_with_mnemonic(quantity):
    print("---- 开始创建钱包 ----")
    Account.enable_unaudited_hdwallet_features()
    create_result = Account.create_with_mnemonic()
    #account = create_result[0]
    mnemonic = create_result[1]
    wallets = []
    for index in range(quantity):

        localAccount = Account.from_mnemonic(mnemonic=mnemonic,
                                             account_path="m/44'/60'/0'/0/"+ str(index))
        privateKey = str.lower(bytes_to_hex(localAccount.key))
        address = localAccount.address
        wallet = {
            "id": index,
            "address": address,
            "privateKey": privateKey,
            "mnemonic": mnemonic
        }
        wallets.append(wallet.values())

    print(wallets)
    saveETHWalletInCsv(wallets)
    print("---- 写入csv完成 ----")
    return wallets


if __name__ == "__main__":
    

    # 创建一定数量的钱包地址
    create_new_wallet_with_mnemonic(11)
    
    # 读取.csv钱包地址
    # callback = lambda wallet: {
    # 拿到底wallet对象之后处理
    #    print(wallet[1])
    # print(wallet.address)
    # print(wallet.privateKey)
    # print(wallet.publicKey)
    # }
    # read_wallets_and_callback('wallets.csv',callback)
