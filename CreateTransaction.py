from interaction import postTransaction, Bhavin, Devanshu, exchange

def createTransaction(sender, receiver, amount, type):
    postTransaction(sender, receiver, amount, type)

if __name__ == '__main__':
    createTransaction(Bhavin, Devanshu, 10, "TRANSFER")
    createTransaction(Bhavin, Devanshu, 1000, "TRANSFER")

