import threading
import time
from message import Message
from BlockchainUtils import BlockchainUtils


class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socketCommunication = node

    def start(self):   # starts the 2 threads
        statusThread = threading.Thread(target=self.status, args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self.discovery, args=())
        discoveryThread.start()

    def status(self):   #
        while True:
            print("Current Connections:")
            for peer in self.socketCommunication.peers:
                print(f'{peer.ip}:{peer.port}')
            time.sleep(7)

    def discovery(self):    # Broadc ast handshake method to all nodes
        while True:
            handshakeMessage = self.handshakeMessage()
            self.socketCommunication.broadcast(handshakeMessage)
            time.sleep(7)

    def handshake(self, connected_node):
        handshakeMessage = self.handshakeMessage()
        self.socketCommunication.send(connected_node, handshakeMessage)

    def handshakeMessage(self):
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        messageType = 'DISCOVERY'
        message = Message(ownConnector, messageType, data)
        encodedMessage = BlockchainUtils.encode(message)
        return encodedMessage

    def handleMessage(self, message):    # Check if the peer is new, and if it is, add it to the list of peers
        peersSocketConnector = message.senderConnector
        peersPeerList = message.data
        newPeer = True
        for peer in self.socketCommunication.peers:
            if peer.equals(peersSocketConnector):
                newPeer = False
        if newPeer == True:
            self.socketCommunication.peers.append(peersSocketConnector)

        for peersPeer in peersPeerList:   # if there is a new peer, and it's not ourselves, connect to it
            peerKnown = False
            for peer in self.socketCommunication.peers:
                if peer.equals(peersPeer):
                    peerKnown = True
            if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):
                self.socketCommunication.connect_with_node(peersPeer.ip, peersPeer.port)
