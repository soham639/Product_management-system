import json
import os
from tabulate import tabulate

def addProduct():

    products={}

    if os.path.exists("products.json"):
        with open("products.json","r") as f:
          products=json.load(f)
        p_id=input("Product ID:")
        products[p_id] = {"name": input("Product Name:"), "price": input("Product Price:"), "stock": input("Product Stock:")}
        with open("products.json","w") as f:
          json_data=json.dump(products,f,indent=4) 
        print(json_data)
        

def viewProduct():
        table=[]
        with open("products.json","r") as f:
            products=json.load(f)
        for p_id,detalis in products.items():
              table.append((p_id,detalis["name"],detalis["price"],detalis["stock"]))
        headers=["ID","Name","Price","Stock"]
        print(tabulate(table,headers=headers,tablefmt="grid"))
        lowStockProductAlert()

def deleteProduct():
    with open("products.json","r") as f:
            products=json.load(f)
    p_id=input("Enter p_id:")
    if p_id in products:
      del products[p_id]
      with open("products.json", "w") as f:
            json.dump(products, f, indent=4)
      viewProduct()
      print("✅ Successfully deleted!")
    else:
      print("❌ Product ID not found.")

def lowStockProductAlert():
   with open("products.json","r") as f:
            products=json.load(f)
            for p_id,details in products.items():
              if (int(details["stock"])<20):
                print(f" Alert!Less stock. (ID: {p_id}),{details["name"]} : {details['stock']} \n  ")
   
    
def sellProduct():
    print("--------------------------------------")
    viewProduct()
    
    with open("products.json", "r") as f:
        products = json.load(f)
    
    items_quantity = int(input("Enter how many types of items you want to buy: "))
    purchased_items = []  # list which stores purchased items
    
    for i in range(items_quantity):
        sp_id = input("Enter Product ID: ")
        
        if sp_id in products:
            quantity = int(input("Enter the quantity: "))
            available_stock = int(products[sp_id]['stock'])
            
            if quantity > available_stock:
                print(f"❌ Not enough stock for {products[sp_id]['name']}. Only {available_stock} items left.\n")
                continue  # Skip to next product
            else:
                products[sp_id]['stock'] = available_stock - quantity
                with open("products.json", "w") as f:
                    json.dump(products, f, indent=4)
                totalBill = quantity * int(products[sp_id]['price'])
                purchased_items.append({"sp_id": sp_id, "quantity": quantity})
        else:
            print("❌ Product not found!")

    continue_shopping = input("Do you want to buy more items (y/n): ")
    if continue_shopping.lower() == "y":
        return sellProduct()
    else:
        if purchased_items:
            generateRecipt(purchased_items)
        print("Thanks for shopping! Visit again!")

  
def generateRecipt(purchased_items):
    
    with open("products.json", "r") as f:
        products = json.load(f)
    
    receipt = []
    grand_total = 0

    for item in purchased_items:
        sp_id = item["sp_id"]
        quantity = item["quantity"]
        product = products[sp_id]
        name = product["name"]
        price = int(product["price"])
        total = quantity * price
        grand_total += total
        receipt.append([sp_id, name, price, quantity, total])

    headers = ["ID", "Name", "Price", "Quantity", "Total"]
    print(tabulate(receipt, headers=headers, tablefmt="grid"))
    print(f"\nGrand Total: ₹{grand_total}")
    print("--------------------------------------")



def mainMenu():
    while True:
        print("\n====== 🛒 Product Management System ======")
        print("1. Add Product")
        print("2. View Products")
        print("3. Delete Product")
        print("4. Sell Product")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            addProduct()
        elif choice == "2":
            viewProduct()
        elif choice == "3":
            deleteProduct()
        elif choice == "4":
            sellProduct()
        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Start the program
mainMenu()
