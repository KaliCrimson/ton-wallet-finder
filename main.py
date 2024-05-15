from tonsdk.contract.wallet import WalletVersionEnum, Wallets
from tonsdk.crypto import mnemonic_new
import requests
import time
while True:
        wallet_workchain = 0
        wallet_version = WalletVersionEnum.v4r2
        wallet_mnemonics = mnemonic_new()

        _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(wallet_mnemonics, wallet_version, wallet_workchain)


        print(wallet_mnemonics)

        adres=wallet.address.to_string(True,True,True)
        print(adres)
        response = requests.get(f'https://toncenter.com/api/v2/getWalletInformation?address={adres}')
        data = response.json()
        result = data.get('result')
        balance = result.get('balance')
        if int(balance) > 0:
                print(balance)
                break
        time.sleep(0.5)

