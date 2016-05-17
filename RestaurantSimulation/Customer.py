import random

class Customer(object):

    def __init__(self):       
        self.maxWaitingTime = random.randint(1,30)
        self.maxEatingTime = random.randint(20, 60)

    def finishedEating():
        return True

    def abandonedLine():
        return True
    
    def timeUpdate():
        return True