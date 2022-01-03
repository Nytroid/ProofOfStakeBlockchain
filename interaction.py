from Transaction import Transaction
from wallet import Wallet
from TransactionPool import TransactionPool
from block import Block
from blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
import pprint
from AccountModel import AccountModel
from node import Node
import sys
import requests

Bhavin = Wallet()
Devanshu = Wallet()
Devanshu.fromKey('keys/stakerPrivateKey.pem')
exchange = Wallet()


def postTransaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(
        receiver.publicKeyString(), amount, type)
    url = "http://192.168.68.128:5000/transaction"
    package = {"transaction": BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)


def interaction():
    postTransaction(exchange, Devanshu, 100, "EXCHANGE")
    postTransaction(Devanshu, Devanshu, 90, "STAKE")

    postTransaction(Devanshu, Bhavin, 10, "TRANSFER")



if __name__ == '__main__':
    interaction()
