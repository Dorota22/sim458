import random

class Customer(object):

    def __init__(self):       
        self.maxWaitingTime = random.randint(1,10)
        self.maxEatingTime = random.randint(10, 20)
        self.waitingTime  = 0
        self.eatingTime = 0
        self.table = None

    def finishedEating(self):
        return self.eatingTime >= self.maxEatingTime

    def abandonedLine(self):
        return self.waitingTime >= self.maxWaitingTime
    
    def timeUpdate(self):
        if self.table == None:
            self.waitingTime += 1
        else:
            self.eatingTime += 1

    def setTable(self, table):
        self.table = table