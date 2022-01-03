from BlockchainUtils import BlockchainUtils


class Lot():

    def __init__(self, publicKey, iteration, lastBlockHash):
        self.publicKey = str(publicKey)
        self.iteration = iteration
        self.lastBlockHash = lastBlockHash

    def lotHash(self):    # creates the amount of hashes as the stake that person has, so they have more chance to be closer to the seed
        hashData = self.publicKey + self.lastBlockHash
        for _ in range(self.iteration):
            hashData = BlockchainUtils.hash(hashData).hexdigest()
        return hashData