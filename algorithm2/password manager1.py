import random
import generate passwords
import tkinter
# creating a password creater and manager

# """
# Product Inventory Project - Create an application which manages
# an inventory of products. Create a product class which has a
# price, id, and quantity on hand. Then create an inventory class
# which keeps track of various products and can sum up the inventory
# value.
# """


#print ("Hello! Welcome to password creator! Do you want to create a password or look at an account? (p/a)")
    welcome = input()
    if welcome == p:
        pass
        #add words to list of words
        # list of passwords
        # text box for passwords

    elif welcome == a:
        generatePasswords.genPassword() #generates password
        pass
        #list accounts
        #index for a certain one

class Account:

    def __init__(self, userName, passWord):
        
        #Class constructor that needs a username and password
        self.userName = userName
        self.passWord = passWord

    #def update_qty(self, qty, method='add'):

        #Updates the quantity of produts. By default, adds the
        #passed quantity. Pass method as 'subtract' to subtract
        #the quantity.

        # if method == 'add':
        #     self.qty += qty
        # elif method == 'subtract':
        #     self.qty = max(0, self.qty - qty)

    def print_product(self):
        # Prints a single product 

        print ('%d\t%s\t%.02f each' % (self.pid, self.qty, self.price))

    def create_password(self):
        x = len(words)
        tempPass = []
        tempPass.append(words[x] + words [])

class Inventory:

    def __init__(self):
        """
        Initializes the class instance.
        """
        self.products = [] # list to hold all products

    def add(self, product):
        """
        Adds a passed Product to the list of products.
        """
        self.products.append(product)

    # def print_inventory(self):
    #     """
    #     Prints the current inventory, and the total value
    #     of products.
    #     """
    #     value = 0
    #     for product in self.products:
    #         print '%d\t%s\t%.02f each' % (product.pid,
    #                                       product.qty,
    #                                       product.price)
    #         value += (product.price * product.qty)
    #     print '\nTotal value: %.02f' % value

# if __name__ == '__main__':
#     p1 = Product(1.4, 123, 5)
#     p2 = Product(1, 3432, 100)
#     p3 = Product(100.4, 2342, 99)


#     i = Inventory()
#     i.add(p1)
#     i.add(p2)
#     i.add(p3)
#     i.print_inventory()

#     p1.update_qty(10)
#     i.print_inventory()
    
#     p1.update_qty(10, method='subtract')
#     i.print_inventory()