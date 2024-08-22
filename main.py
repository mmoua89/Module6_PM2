"""
Author: Meng Moua
Course: CSC500
Assignment: Module 6, Portfolio Milestone 2
"""
from ShoppingCart import ShoppingCart
from Item import Item
def main():
    shoppingCart = ShoppingCart()
    userInput = ""

    while userInput != 'q' or userInput != 'quit':
        printMenu()
        userInput = input()

        if userInput == 'a':
            itemName = input('Item name:\n')
            itemPrice = input('Item price:\n')
            itemQuantity = input('Item quantity:\n')
            itemDescription = input('Item description:\n')

            # valid item_price and item_quantity
            # if not valid_numbers(itemPrice, itemQuantity):
            #     return

            # append item in (Item) class
            item = Item(itemName, float(itemPrice), int(itemQuantity), itemDescription)
            shoppingCart.addItem(item)
        elif userInput == 'o':
            shoppingCart.printTotal()



def printMenu():
    menuList = ['a - Add item to cart',
                'r - Remove item from cart',
                'c - Change item quantity',
                "i - Output items' description",
                'o - Output shopping cart',
                'q - quit']
    print('Menu')
    for menuItem in menuList:
        print(menuItem)
    print('Choose an option:\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
