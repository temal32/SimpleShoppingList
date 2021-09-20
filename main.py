# importing modules
import os # to change the title
import time # to add a delay

# creating a new list
shopping_list = []

# changing the console title
os.system("title Shopping List")

#creating a new function
def menu():
    selection = input("1: Show Shoppinglist.\n2: Add Product\n3: Remove Product\n\nEnter: ")
    def adding():
        add_product = input("Product: ")
        shopping_list.append(add_product)
        print("\nProduct added.")
        time.sleep(3)
    def showing():
        try:
            print(shopping_list)
            time.sleep(3)
        except:
            print("\nCurrently no products in your shoppinglist.")
            time.sleep(3)
    def removing():
        try:
            remove_product = input("Product Name: ")
            shopping_list.remove(remove_product)
            print("\nProduct removed.")
            time.sleep(3)
        except:
            print("\nProduct not found.")
            time.sleep(3)
    if selection == "1":
        showing()
    if selection == "2":
        adding()
    if selection == "3":
        removing()
        
while 1 < 2:
    os.system("cls")
    print(menu())
