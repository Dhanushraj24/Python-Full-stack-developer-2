
# Task Inventory Management

inventory = {}

# Using a while loop for (adding, removing, and exiting), once the condition is met, it will exit the program

while True:

    try:
        operation = input("Enter operation (add/remove/exit): ").lower()

        if operation == "add":
            item = input("Enter item: ")
            quantity = int(input("Enter quantity: "))
          
            inventory[item] = inventory.get(item, 0) + quantity
            print("Current inventory:", inventory)

        elif operation == "remove":
            item = input("Enter item: ")
            quantity = int(input("Enter quantity: "))
            if item in inventory:
                if inventory[item] >= quantity:
                    inventory[item] = inventory[item] - quantity
                    print("Current inventory:", inventory)
                else:
                    print("Error: Not enough quantity to remove.")
            else:
                print("Error: Item not found in inventory.")

        elif operation == "exit":
            print("Exiting. Final inventory:", inventory)
            break

        else:
            print("Invalid operation. Please enter add, remove, or exit.")
            
# Using exception handling to find out the error in the program
    
    except ValueError:
        print("Error: Quantity must be an integer.")
