import random


class Table(object):
    """description of class"""
    
    def __init__(self):
        self.maxCustomerCount = random.randint(1, 4)
        self.isEmpty = True