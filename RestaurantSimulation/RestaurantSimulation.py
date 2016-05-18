from Restaurant import Restaurant
from Party import Party
from Visualization import Visualization

import random
import time

MIN_PEOPLE_COUNT = 1
MAX_PEOPLE_COUNT = 4



class RestaurantSimulation(object):

    def __init__(self):

        tableDefinition = [[5, 2], [1, 4]]
        
        self.restaurant = Restaurant(tableDefinition)


    def simulate(self):

        id = 1
        while(True):
            #randomly add new party 
            if id < 10 and random.random() < 0.3:
                peopleCount = random.randint(MIN_PEOPLE_COUNT, MAX_PEOPLE_COUNT)
                party = Party(peopleCount, id)
                id += 1     
                self.restaurant.waitingParties.append(party)
            self.restaurant.timeUpdate()
            time.sleep(1)
            if id == 10 and len(self.restaurant.waitingParties) == 0 and len(self.restaurant.eatingParties) == 0:
                return
            #Visualization
                            
    def addToLine(self):
        return True

simulation = RestaurantSimulation()
simulation.simulate()