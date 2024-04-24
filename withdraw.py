import ccxt

#
binance_api_key = 'BINANCE_API_KEY'
binance_secret_key = 'BINANCE_SECRET_KEY'
kucoin_api_key = 'KUCOIN_API_KEY'
kucoin_secret_key = 'KUCOIN_SECRET_KEY'
kraken_api_key = 'KRAKEN_API_KEY'
kraken_secret_key = 'KRAKEN_SECRET_KEY'
bitget_api_key = 'BITGET_API_KEY'
bitget_secret_key = 'YOUR_BITGET_SECRET_KEY'

#
binance_usdt_address = 'BINANCE_USDT_TRC20_ADDRESS'
kucoin_usdt_address = 'KUCOIN_USDT_TRC20_ADDRESS'
kraken_usdt_address = 'KRAKEN_USDT_TRC20_ADDRESS'
bitget_usdt_address = 'BITGET_USDT_TRC20_ADDRESS'

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
