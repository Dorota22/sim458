from Restaurant import Restaurant
from Party import Party
import Visualization as V

import random
import time

MIN_PEOPLE_COUNT = 5
MAX_PEOPLE_COUNT = 8



class RestaurantSimulation(object):

    def __init__(self):

        tableDefinition = [[15, 2], [2, 4],[4,6],[3,8]]
        
        self.restaurant = Restaurant(tableDefinition)


    def simulate(self):

        id = 1
        while(True):
            #randomly add new party 
            if id < 20 and random.random() < 0.6:
                peopleCount = random.randint(MIN_PEOPLE_COUNT, MAX_PEOPLE_COUNT)
                party = Party(peopleCount, id)
                id += 1     
                self.restaurant.waitingParties.append(party)
            V.plotRestaurant(self.restaurant)
            self.restaurant.timeUpdate()
            time.sleep(1)
            if id == 10 and len(self.restaurant.waitingParties) == 0 and len(self.restaurant.eatingParties) == 0:
                return
            #Visualization
            #V.plotRestaurant(self.restaurant)
                            
    def addToLine(self):
        return True

simulation = RestaurantSimulation()
simulation.simulate()