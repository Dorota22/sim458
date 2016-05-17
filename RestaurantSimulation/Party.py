from Customer import Customer
import random
import numpy as N

MIN_PEOPLE_COUNT = 1
MAX_PEOPLE_COUNT = 4

class Party(object):
    """description of class"""
  
    def __init__(self):
        self.numberOfPeople = random.randint(MIN_PEOPLE_COUNT, MAX_PEOPLE_COUNT)
        partyList = []

        for i in xrange(numberOfPeople):
            partyList.append(Customer())

        self.maxWaitingTime = N.min(partyList.Customer.maxWaitingTime)
        self.maxEatingTime = N.max(partyList.Customer.maxEatingTime)
        #self.color 

    def finishedEating():
        return True

    def abandonedLine():
        return True

    def timeUpdate():
        return True