"""
A Shopping Cart class that represent a customer name,
date and the added items with their prices and the total cost.
"""
from datetime import datetime
from Item import Item
class ShoppingCart:
    def __init__(self, customerName="none", currentDate=datetime(2020, 12, 1)):
        self.customerName = customerName
        self.currentDate = currentDate
        self.cartItems = []

    def addItem(self, itemToPurchase):
        self.cartItems.append(itemToPurchase)

    def removeItem(self, itemName):
        for item in self.cartItems:
            if itemName == item.itemName:
                self.cartItems.remove(item)
                return
        print('Item not found in cart. Nothing removed.')

    def modifyItem(self, itemToPurchase):
        for item in self.cartItems:
            itemInstance = Item(**itemToPurchase)
            if item.itemName == itemInstance.itemName:
                if itemInstance.itemDescription != "none":
                    item.itemDescription = itemInstance.itemDescription
                if itemInstance.itemPrice != 0:
                    item.itemPrice = itemInstance.itemPrice
                return
        print('Item not found in cart. Nothing modified.')

    def getNumItemInCart(self):
        totalQuantity = 0
        for item in self.cartItems:
            totalQuantity += item.itemQuantity
        return totalQuantity

    def getTotalCost(self):
        totalCost = 0.0
        for item in self.cartItems:
            totalCost += item.calculate_total_cost()
        return totalCost

    def printTotal(self):
        if len(self.cartItems) == 0:
            print('SHOPPING CART IS EMPTY.')
            return

        for item in self.cartItems:
            item.print_item_cost()

        print('Total: {:.2f}'.format(self.getTotalCost()))


    def printDescriptions(self):
        for item in self.cartItems:
            print('{}: {}'.format(item.itemName, item.itemDescription))