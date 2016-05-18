import random


class Table(object):
    """description of class"""
    
    def __init__(self, maxCustomerCount):
        self.maxCustomerCount = maxCustomerCount
        self.party = None 

    #def __cmp__(self, other):       
    #    return self.maxCustomerCount.__cmp__(other.maxCustomerCount)  


    def __repr__(self):
        peopleCount = ' ' if self.party == None else ':(id '+ str(self.party.id) + ': C '+ str(self.party.peopleCount) + ')'
        return str(self.maxCustomerCount) + peopleCount

    def setParty(self, party):
        self.party = party