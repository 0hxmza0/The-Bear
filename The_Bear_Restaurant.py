def read_inventory(filename): #defining a function to read the inventory with the specific filename in the parameters
    inventory = {}  # defining an empty dictionary to store the inventory as keys and values
    with open(filename, 'r') as file: #opening the filename in read mode and closes the file automatically
        for line in file: #loops through each line in the file
            lines = line.strip()    #removing lead and tracing whitespaces
            if lines:   # works when the line is not empty
                split = lines.split(',')    #splitting the line into a list of strings with using the comma to seperate
                dish = split[0] # the first index is the dish name
                price = float(split[1]) #second index is the the price of the dish and it is converted to a float
                qty = int(split[2]) #the third index is the quantity left of the dish and converta it into an integer
                inventory[dish] = [price, qty]  # adds the dish as the key with price and quatity being values in a list to the inventory dictionry
    return inventory    #returns the completed inventory dictionary 

def display_inventory(inventory):   #defining a funtion tp display the current inventory
    for dish, value in inventory.items():   #loops through each of the key and value pair in the inventory dictionary
        price = value[0]    #getting the price from the list in values with index 0
        qty = value[1]  #getting the quantity of the dish from the list in values with index 1
        print(f"{dish} ${price:.2f} Qty:{qty}") # printing a formated string to show the dish, price with two decimal places, and quatity 

def add_item(inventory):    #  defining a function to add an item to the inventory
    new_item = input("Enter item: ")    #asks the user to input the name of a dish they would like to add
    if new_item in inventory.keys():    # loops through the inventory keys whether the item already exists or not
        print(f"{new_item} already exists") # prints statement to informn the user that the dish already exists
    else: #checks if it dosen't exist
        price = float(input("Enter price: "))  # if it dosen't exist then asks the user for the item's price and converts it to a float
        quantity = int(input("Enter availability:"))    #asks the user to input the quantity of the dish and converts it into an integer
        inventory[new_item] = [price, quantity] #stores the new item as the key storing price and quantity as the values in the inventory dictionary
        print(f"Added {new_item}")  #Shows the user that the item has been added to the inventory

def delete_item(inventory): # defining a funtion to delete an item from the inventory
    remove_item = input("Enter item: ") #asks the user to input an item they would like to remove
    if remove_item in inventory.keys(): #loops through the inventory keys to check if the item inputted exists in the inventory
        inventory.pop(remove_item)     #removes the item from the inventory dictionary 
        print(f"Deleted {remove_item}") # prints statement confirming the removal of the item
    else:   # if the item does not exist
        print(f"{remove_item} Not Found")   #informs the user that the item is not found in the invenotry 
            
def update_cost(inventory): #defining a funtion to update the cost of an item in the dictionary
    update = input("Enter item: ") #asks the user to input an item to update the price on
    if update in inventory: # checks if the item exists in the inventory
        percentage_increase = float(input("Enter percentage increase: "))   #asks the user to input the percentage increase and converts it into a float
        old_price = inventory[update][0]    # gets the original price of the item of the specific dish
        new_price = round(old_price * (1 + percentage_increase / 100), 2)  # Calculating the new price after dividing the percentage increase with 100 and then adding one then multiplying with the old price and rounding it to 2 decimal places
        inventory[update][0] = new_price  #updates the price in the inventory for the chosen dish
        print(f"Updated {update}")  #informs the user that the price has been updated for the inputted item
    else: #if its not found
        print(f"{update} Not Found") # Informs the user the item does not exist

def above_avg_cost(inventory):  # defining a function to find and display the items that are above the average cost 
    prices = [] #creating an empty list for storing the prices of the dishes
    for values in inventory.values():   #looping through all the values in the inventory dictionary
        prices.append(float(values[0])) # adds the price of all the dishes and converts it to a float to the empty list
    average_cost = sum(prices) / len(prices)    # calculating the average cost by taking the sum of all the values in the list and then divinding it by the number of values in the list
    print(f"Average cost:", average_cost) # prints the average cost after calculating 
    print("Items above average cost:")    #prints header of items having a higher price than the average cost
    for dish, values in inventory.items():  #loops through the keys and values of the inventory dictionary
        price = values[0]   #gets the price of the item in the dictionary
        if price > average_cost:    #checks if the price is greater than the calculated average cost 
            print(f"{dish} - ${price}") #prints the dishes that have a higher price than the average cost
    return average_cost #returns the average cost 

def sell_item(inventory):   #defining a funtion to sell an item from the dictionary
    sell = input("Enter Item: ")    #asks the user to input the item they would like to sell

    if sell not in inventory:   # if the item not in the inventory dictionary
        print(f"{sell} not found")  # informs the user the item is not found
        return #exits the funtion

    price, qty = inventory[sell]    #gets the price and quatity from the inventory dictionary
    
    quantity = int(input("Enter quantity: "))   #asks the user to input the quantity they would like to sell and converts to integer 
    if qty == 0:    # checks if the item is out of stock
        print(f"{sell} not available")  #informs the user that the item is not available
        return  #exits program
    if quantity > qty:  #checks if the inputted quantity is greater than what's available
        total = (price * qty)   #calculating the total price by multiplyinh the price of the item with the quantity available
        print(f"{qty} out of {qty} units sold for ${total:.2f}, with 0 units remaining.")   #prints the details of the quantity sold and left with the total price
        inventory[sell][1] = 0  #sets the quantity to 0 of that item
    else: #checks if the waanted quantity is less than or equal to what's available.
        total = (price * quantity)  # Calculating the total price for the sold quantity 
        inventory[sell][1] -= quantity  # decreases the item's quantity with the desired amount needed
        remaining = inventory[sell][1]  # stores the remaining quantity in the inventory
        print(f"{quantity} out of {qty} units sold for ${total:.2f}, with {remaining} units remaining.")  # prints the details of how much is sold from the stock and the total cost
        
def out_of_stock(inventory):    #defining a function to show items that are out of stock
    print("Out of Stock:")  #prints the heading of the items out of stock
    full = True # a flag to check if any items are out of stock
    for dish, value in inventory.items():  #loops through the keys and values in the inventory
        if value[1] == 0:      #checks if the quantity of the item is equals to zero
           print(dish)  #prints the dish that has no stock left
           full = False # sets the flag to false
    if full:    # if all items in stock
        print('All items are in stock') #informs the user that all the items are availabe
            
def main(): #defining the main function to execute the program
    file = input("Enter filename: ")    #asks the user to input the filename   
    inventory = read_inventory(file)    #reads the inventory in the specified file and is stored in the varoable inventory

    menu_actions = {"1": display_inventory, "3": add_item, "4": delete_item, "5": update_cost, "6": above_avg_cost, "7": sell_item, "8": out_of_stock}  # a dictionary to map the user's choices to functions

    running = True  # a flag for the while loop
    while running:  # starts the while loop
        print("\nMENU:\n1. Display inventory\n2. Exit\n3. Add Item\n4. Delete Item\n5. Update Cost\n6. Items above average cost\n7. Sell Item\n8. Out of stock") #diplays the menu options to the user
        choice = input("Enter choice: ")    #asks the user to input their choice
        if choice == "2":   #if the user picks 2
            print("Goodbye")    #it prints a farewell statement 
            return False    #exits the loop by returning false
        elif choice in menu_actions:    # checks if the choice is a valid menu option
            menu_actions[choice](inventory) # then calls the related function with the inventory as an argument.
        else:   #checks if the choice is invalid
            print("Invalid Choice") #informs the user the choice is invalid and then loops until it is valid
main() #executes program