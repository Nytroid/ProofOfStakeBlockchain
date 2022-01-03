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

def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])
    keyFile = None
    if len(sys.argv) > 4:
        keyFile = sys.argv[4]

    node = Node(ip, port, keyFile)
    node.startP2P()
    node.startAPI(ip, apiPort)


if __name__ == '__main__':
    main()


