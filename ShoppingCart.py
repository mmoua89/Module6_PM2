"""
A Shopping Cart class that represent a customer name,
date and the added items with their prices and the total cost.
"""
from datetime import datetime
class ShoppingCart:
    def __init__(self, customerName="none", date=datetime(2010, 12,1 )):
        self.customerName = customerName
        self.datetime = datetime

    def addItem(self, item):
        pass

    def removeItem(self, item):
        pass

    def modifyItem(self):
        pass

    def getNumItemInCart(self):
        pass

    def getTotalCost(self):
        pass

    def printTotal(self):
        pass

    def printDescriptions(self):
        pass