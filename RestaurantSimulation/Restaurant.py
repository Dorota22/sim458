from Table import Table
from Party import Party

import numpy as N

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

    def timeUpdate(self):

        for eatingParty in self.eatingParties:        
            eatingParty.timeUpdate()
            if eatingParty.finishedEating():
                self.satisfiedParties.append(eatingParty)
                self.eatingParties.remove(eatingParty)                        
                eatingParty.table.setParty(None)
                eatingParty.setTable(None)
         
        # In this model, we sit only the first party per one time unit 
        self.sitPartyFIFO()
                          
        for waitingParty in self.waitingParties:
            waitingParty.timeUpdate()
            if waitingParty.abandonedLine():
                self.abandonedParties.append(waitingParty)       
                self.waitingParties.remove(waitingParty)   

        print 'Tables:    ', self.tableList
        print 'Eating:    ', self.eatingParties            
        print 'Waiting:   ', self.waitingParties                  
        print 'Abandoned: ', self.abandonedParties
        print 'Satisfied: ', self.satisfiedParties