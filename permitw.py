from web3 import Web3

# Avalanche veya Ethereum ağına bağlanın
web3 = Web3(Web3.HTTPProvider("https://api.avax.network/ext/bc/C/rpc"))  # Avalanche C-Chain
# veya
# web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))  # Ethereum Mainnet

# Sözleşme adresini checksum formatına çevirin
contract_address = Web3.toChecksumAddress("0x63682bdc5f875e9bf69e201550658492c9763f89")

# Sözleşme ABI'si
contract_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "owner", "type": "address"},
            {"name": "spender", "type": "address"},
            {"name": "value", "type": "uint256"},
            {"name": "deadline", "type": "uint256"},
            {"name": "v", "type": "uint8"},
            {"name": "r", "type": "bytes32"},
            {"name": "s", "type": "bytes32"},
        ],
        "name": "permit",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "from", "type": "address"},
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"}
        ],
        "name": "transferFrom",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    }
]

# Sözleşme ile etkileşim için instance oluşturun
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# 1. Permit işlemini gerçekleştirin
tx_hash_permit = contract.functions.permit(
    "0x86af4ad800feeb10c09dab7ddbb8bf3e5f86fb15",  # owner
    "0x09022D35C62a8B91d4e3E2b62b8E7bb1B23ed781",  # spender
    int("1158472395435294898592384258348512586931256000000000000000000"),  # value
    int("1749926017139"),  # deadline
    27,  # v
    Web3.toBytes(hexstr="0x0be40158b720478161f79f2cab26e59488b3db2b5149ee5c862a64f95380ebe5"),  # r
    Web3.toBytes(hexstr="0x1b366e2c3a354aa19086e2a2db6caf795a16fac72829d3ca9411fb6387397d16")   # s
).transact({'from': '0xB3265a2d7edc8577F88772d1A87F7adeFC5b5700'})

# Permit işleminin onaylanmasını bekleyin
receipt_permit = web3.eth.wait_for_transaction_receipt(tx_hash_permit)
print("Permit işlemi tamamlandı:", receipt_permit)

# 2. Transfer işlemini gerçekleştirin
tx_hash_transfer = contract.functions.transferFrom(
    "0x86af4ad800feeb10c09dab7ddbb8bf3e5f86fb15",  # owner
    "0xB3265a2d7edc8577F88772d1A87F7adeFC5b5700",  # sizin adresiniz
    int("1158472395435294898592384258348512586931256000000000000000000")  # value
).transact({'from': '0xB3265a2d7edc8577F88772d1A87F7adeFC5b5700'})

# Transfer işleminin onaylanmasını bekleyin
receipt_transfer = web3.eth.wait_for_transaction_receipt(tx_hash_transfer)
print("Transfer işlemi tamamlandı:", receipt_transfer)
