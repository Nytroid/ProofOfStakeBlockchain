from lot import Lot
from BlockchainUtils import BlockchainUtils


class ProofOfStake:

    def __init__(self):
        self.stakers = {}
        self.setGenesisNodeStake()

    def setGenesisNodeStake(self):
        genesisPublicKey = open("keys/genesisPublicKey.pem", 'r').read()
        self.stakers[genesisPublicKey] = 1

    def update(self, publicKeyString, stake):   # Updates the stake amount by the amount staked, and adds the publicKey to stakers list if not already there
        if publicKeyString in self.stakers.keys():
            self.stakers[publicKeyString] += stake
        else:
            self.stakers[publicKeyString] = stake

    def getStake(self, publicKeyString):
        if publicKeyString in self.stakers.keys():
            return self.stakers[publicKeyString]
        else:
            return None

    def validatorLots(self, seed):    # Gives every validator lots based on the s take they have
        lots = []
        for validator in self.stakers:
            for stake in range(self.getStake(validator)):
                lots.append(Lot(validator, stake+1, seed))
        return lots

    def winnerLot(self, lots, seed):     # Finds the lot closest to the reference hash and makes it the next forger
        winnerLot = None
        leastOffset = None
        referenceHashIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue-referenceHashIntValue)
            if leastOffset is None or offset < leastOffset:
                leastOffset = offset
                winnerLot = lot
        return winnerLot

    def forger(self, lastBlockHash):   # creates the lots using the validatorsLots method and gets the winner using the winnerLot method
        lots = self.validatorLots(lastBlockHash)
        winnerLot = self.winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey
