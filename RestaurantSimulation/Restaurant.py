from Table import Table
from Party import Party

import numpy as N
import random


class Restaurant(object):

    def __init__(self, tableDefinition):
                
        self.eatingParties = []
        self.waitingParties = []
        self.abandonedParties = []
        self.satisfiedParties = []

        #self.sittingMethod = sittingMethod

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
    
    def sitWithWait(self):                                      
        for party in self.waitingParties:               
            # see if there's an empty table where size >= peopleCount
            table = self.getEmptyTable(party)
            # if the table exists
            if table != None:
                # sets the table's party data attribute to the first party 
                # in waitingParties
                table.setParty(party)
                # sets the party's Table data attribute to the empty table
                # obtained from tableList
                party.setTable(table)
                self.eatingParties.append(party)
                self.waitingParties.remove(party)
                return 
       

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
        #self.sitWithWait()
        #self.sitPartyRandomly()
        self.sittingMethod(self)
                          
        for waitingParty in self.waitingParties:
            waitingParty.timeUpdate()
            if waitingParty.abandonedLine():
                self.abandonedParties.append(waitingParty)       
                self.waitingParties.remove(waitingParty)   

