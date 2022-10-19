# web3_script_tutorial

Web3脚本交互（撸毛）极简入门指南

* 目标：通过4个小例子循序渐进学习并使用 Web3.py 模块实现链上数据查询、转账、合约交互等简单功能。
* 合约交互四部曲：
1. 确定合约地址
2. 找到合约ABI
3. 研究函数名及参数具体含义
4. 写交互代码，广播交易信息

## 00: 前期准备工作

1. 安装 Python3
2. 安装 web3.py 库 `pip install web3`
3. 申请 Infura API Key: https://infura.io/
4. 申请测试币 https://faucets.chain.link/
❕注意：保管好示例代码中的私钥，注意风险。

## 01: 读取链上信息

* 目标：通过 Infura 接入以太坊主网并查询v神钱包余额信息
* 代码： https://github.com/JetCyC/web3_script_tutorial/blob/main/1-serch.py

* 接入节点后的Web3对象为我们通向区块链世界的钥匙，不论是查询链上数据，还是进行转账、合约交互，都是通过它来实现。


## 02: Goerli 测试网转账 ETH

* 目标：接入 Goerli 测试网并完成一笔转账交易
* 代码: https://github.com/JetCyC/web3_script_tutorial/blob/main/2-transferETH.py

* 转账是所有链上交互的灵魂，是一种改变区块链状态的行为。相比较前面的“查询地址余额”，属于“写入”的操作类型。转账、合约交互等操作，都需要用地址对应的私钥签名交易并广播。


## 03: Arbitrum 测试网跨链桥交互

* 目标： 完成 Arbitrum 测试网的跨链桥存入 ETH 的交互
* 代码： https://github.com/JetCyC/web3_script_tutorial/blob/main/3-ArbitrumBridge.py

* 合约交互比起普通转账，又要复杂了一些。从合约交互开始，会需要额外几个参数：▪️ 合约地址 ▪️ 合约ABI ▪️ 交互的函数名称及具体参数
* 获取合约abi的途径  ▪️ etherscan ▪️ 项目前端开发者模式—>Sources->查找目录下是否有abi文件 ▪️ https://twitter.com/gm365/status/1521058983838380032?s=20&t=5GJAoEw0teYA9ZPcyhTGYg



## 04: zkSync 测试网跨链桥交互

* 目标： 完成 zkSync 测试网的跨链桥存入 ETH 交互

* 代码： https://github.com/JetCyC/web3_script_tutorial/blob/main/4-zkSyncBridge.py
* 相比较于 Arbitrum，zkSync 的难度稍微高了一点。因为后者使用了一个可升级合约，导致无法在 Etherscan 网站找到确切的 ABI 信息。不过，通过前一条 🧵 中的方法，最终在网站 chunk-vendor-xxx.js 文件中定位到了完整的 ABI 信息。



## 进阶

* 交互大师
测试网简单合约 ➜ 测试网复杂合约 ➜ 主网合约 ➜ 多账号单合约 ➜ 多账号多合约 ➜ 多账号切断关联 ➜ 多账号多合约模拟真实用户行为轨迹 ➜ ( Ξ ) ➜ 躺平

* 套利大师
MEV套利 ➜ ( Ξ Ξ Ξ ) ➜ 躺平
