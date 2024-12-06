inventory = {}
while True:
    print("\n--------------------------------")
    print("         sari-sari Store")
    print("--------------------------------\n")
    choose = input('1. List Available Items.\n2. Add new item.\n3. Update Stock Quantity.\n4. Update price of existing Item.\n5. Exit.\nChoose Option (1-5):')
    if choose == '1':
        for item in inventory:
            details = inventory[item]
            print(f"Product name: {item} | Price: {details['priceItem']} | Quantity: {details['quantity']}")
    elif choose == '2':
        print("\n----------ADD ITEM----------")
        nameItem = input("Product name: ")
        quantityOfItem = input("Quantity: ")
        priceItem = input("Price: ")
        inventory[nameItem] = {'quantity': quantityOfItem, 'priceItem': priceItem}
        print('Added Successfully........')
    elif choose == '3':
        print("\n----------UPDATE STOCK----------")
        inputStockQuan = input("Enter the product name: ")
        if inputStockQuan in inventory:
            amountOfQuantity = input("Enter new stock of quantity: ")
            inventory[inputStockQuan]['quantity'] = amountOfQuantity
            print("Update successfully...........")
        else:
            print(f"{inputStockQuan} not exist in our inventory.")
    elif choose == '4':
        print("\n----------UPDATE PRICE----------")
        inputUpdatePrice_product = input('Enter the product name: ')
        if inputUpdatePrice_product in inventory:
            amountUpdatePrice = input("Enter the new price: ")
            inventory[inputUpdatePrice_product]['priceItem'] = amountUpdatePrice
            print("Update successfully...........")
        else:
            print(f"{inputUpdatePrice_product} not exist in our inventory.")
    else:
        print("Invalid option, try again!")