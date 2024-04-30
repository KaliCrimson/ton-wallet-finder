from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import requests
import time

while True:
	print("'"*50)
	mnem , pub , priv, wallet = Wallets.create(version=WalletVersionEnum.v4r2, workchain=0)
	print(mnem)
	print(wallet.address.to_string(True , True, True))
	adres = wallet.address.to_string(True,True , True)
	response = requests.get(f'https://toncenter.com/api/v2/getWalletInformation?address={adres}')
	data = response.json()
	result = data.get('result')
	balance = result.get('balance')
	if int(balance) > 0:
		print(balance)
		break
	time.sleep(1)
