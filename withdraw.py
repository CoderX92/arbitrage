import ccxt

# Prompt user for exchange details
binance_api_key = input("Enter your Binance API key: ")
binance_secret_key = input("Enter your Binance secret key: ")
binance_usdt_address = input("Enter your Binance USDT TRC20 withdrawal address: ")

kucoin_api_key = input("Enter your KuCoin API key: ")
kucoin_secret_key = input("Enter your KuCoin secret key: ")
kucoin_usdt_address = input("Enter your KuCoin USDT TRC20 withdrawal address: ")

kraken_api_key = input("Enter your Kraken API key: ")
kraken_secret_key = input("Enter your Kraken secret key: ")
kraken_usdt_address = input("Enter your Kraken USDT TRC20 withdrawal address: ")

bitget_api_key = input("Enter your Bitget API key: ")
bitget_secret_key = input("Enter your Bitget secret key: ")
bitget_usdt_address = input("Enter your Bitget USDT TRC20 withdrawal address: ")

# Initialize exchanges
binance = ccxt.binance({
    'apiKey': binance_api_key,
    'secret': binance_secret_key
})

kucoin = ccxt.kucoin({
    'apiKey': kucoin_api_key,
    'secret': kucoin_secret_key
})

kraken = ccxt.kraken({
    'apiKey': kraken_api_key,
    'secret': kraken_secret_key
})

bitget = ccxt.bitget({
    'apiKey': bitget_api_key,
    'secret': bitget_secret_key
})

# Define function to check balance and withdraw
def withdraw_usdt(exchange, usdt_address):
    if 'USDT' in exchange.fetch_balance()['free']:
        amount = exchange.fetch_balance()['free']['USDT']
        print(f"Withdrawing {amount} USDT from {exchange.id} to {usdt_address}")
        withdrawal_response = exchange.withdraw('USDT', amount, usdt_address)
        print("Withdrawal response:", withdrawal_response)
    else:
        print(f"No USDT balance available on {exchange.id}")

# Execute withdrawals
withdraw_usdt(binance, binance_usdt_address)
withdraw_usdt(kucoin, kucoin_usdt_address)
withdraw_usdt(kraken, kraken_usdt_address)
withdraw_usdt(bitget, bitget_usdt_address)
