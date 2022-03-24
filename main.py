# importing modules
import os  # to change the title
import time  # to add a delay

# creating a new list to put the products in
shopping_list = []

# changing the console title
os.system("title Shopping List")

seperator = ", " # define seperator to print a clear list

# creating a new function
def menu():
    selection = input("1: Show Shopping list.\n2: Add Product\n3: Remove Product\n\nEnter: ")

    def adding():
        add_product = input("Product: ")
        shopping_list.append(add_product)
        print("\nProduct added.")
        time.sleep(3)

    def showing():
        if not shopping_list:
            print("\nCurrently no products in your shopping list.")
            time.sleep(3)
        else:
            print(seperator.join(map(str, shopping_list)))
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
