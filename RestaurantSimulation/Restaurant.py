from Table import Table
from Party import Party

import numpy as N
import random

WIDTH = 5
LENGTH = 7

class Restaurant(object):

    def __init__(self, tableDefinition):
                
        self.eatingParties = []
        self.waitingParties = []
        self.abandonedParties = []
        self.satisfiedParties = []

        #create tablelist based on the tableDefinition
        self.tableList = []
        for i in xrange(0, len(tableDefinition)):
            tableCount = tableDefinition[i][0]
            for table in xrange(0, tableCount):
                tableCustomerCount = tableDefinition[i][1]
                self.tableList.append(Table(tableCustomerCount))
        #self.tableList.sort()
    
    def getEmptyTable(self, party):        
        for table in self.tableList:
            if(table.party == None and party.peopleCount <= table.maxCustomerCount):
                return table   
        return None 

    def getSmallestValidEmptyTable(self, party):   
        smallestValidTableSize = None
         
        # iterate through each available table in tableList
        # tableList will be sorted    
        for table in self.tableList:

            # find a table that doesn't have a party and whose size >= party size
            if(table.party == None and party.peopleCount <= table.maxCustomerCount):

                # if we haven't already set the smallestValidTableSize, set it
                # to this table's size -- tableList is sorted, so smallest tables
                # appear first
                if (smallestValidTableSize == None):
                    smallestValidTableSize = table.maxCustomerCount

                # if the table's size is the same as the smallestValidTableSize
                # for that party, return the table
                if (table.maxCustomerCount == smallestValidTableSize):
                     return table 

        return None 
 
    def getRandomEmptyTable(self, party):
        table = random.choice(self.tableList)                 
        if(table.party == None and party.peopleCount <= table.maxCustomerCount):
            return table
        return None                                  

    def sitPartyFIFO(self):
        
        if len(self.waitingParties) > 0:
            party = self.waitingParties[0]
            table = self.getEmptyTable(party)
            if table != None: 
                table.setParty(party)
                party.setTable(table)
                self.eatingParties.append(party)
                self.waitingParties.remove(party)
                return
    
    def sitCanSkipParties(self): 
        
        # iterate though each party in the list of parties                                     
        for party in self.waitingParties:    
                       
            # see if there's an empty table where size >= peopleCount
            table = self.getEmptyTable(party)

            # if the table exists
            if table != None:

                # sets the table's party data attribute to the current party 
                table.setParty(party)

                # sets the party's Table data attribute to the empty table
                # obtained from tableList
                party.setTable(table)

                # update eatingParties and waitingParties
                self.eatingParties.append(party)
                self.waitingParties.remove(party)
                return 

       # return      # don't need this one?

    def sitCanSkip_GetMinTable(self): 

        # iterate though each party in the list of parties                                     
        for party in self.waitingParties:    
                       
            # see if there's an empty table where the table size is the 
            # smallest in the restaurant than can accommodate the party
            table = self.getSmallestValidEmptyTable(party)

            # if the table exists and 
            if table != None:

                # sets the table's party data attribute to the current party 
                table.setParty(party)

                # sets the party's Table data attribute to the empty table
                # obtained from tableList
                party.setTable(table)

                # update eatingParties and waitingParties
                self.eatingParties.append(party)
                self.waitingParties.remove(party)
                return 

        #return      # don't need this one?

    def sitPartyRandomly(self):        
        for party in self.waitingParties:                     
            table = self.getRandomEmptyTable(party)
            if table != None: 
                table.setParty(party)
                party.setTable(table)
                self.eatingParties.append(party)
                self.waitingParties.remove(party)
                return
        return

    def timeUpdate(self):
        for eatingParty in self.eatingParties:        
            eatingParty.timeUpdate()
            if eatingParty.finishedEating():
                self.satisfiedParties.append(eatingParty)
                self.eatingParties.remove(eatingParty)                        
                eatingParty.table.setParty(None)
                eatingParty.setTable(None)
         
        # In this model, we sit only the first party per one time unit 
        #self.sitPartyFIFO()

        self.sitCanSkipParties()
       # self.sitPartyRandomly()
                          
        for waitingParty in self.waitingParties:
            waitingParty.timeUpdate()
            if waitingParty.abandonedLine():
                self.abandonedParties.append(waitingParty)       
                self.waitingParties.remove(waitingParty)   

        print ('Tables:    ', self.tableList)
        print ('Eating:    ', self.eatingParties)            
        print ('Waiting:   ', self.waitingParties)                  
        print ('Abandoned: ', self.abandonedParties)
        print ('Satisfied: ', self.satisfiedParties)