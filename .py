import json
import os
from tabulate import tabulate

def addProduct():

    products={}

    if os.path.exists("products.json"):
        with open("products.json","r") as f:
          products=json.load(f)
        products["p_id":input("Product ID:")] = {"name": input("Product Name:"), "price": input("Product Price:"), "stock": input("Product Stock:")}
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
  viewProduct()
  with open("products.json","r") as f:
            products=json.load(f)
  items_quantity=int(input("Enter how many types items you want to buy:"))
  for i in range(items_quantity):
        sp_id=input("Enter Product id:")
        quantity=int(input("Enter the quantity:"))
        if sp_id in products:
          products[sp_id]['stock']=int(products[sp_id]['stock'])-quantity
          with open("products.json", "w") as f:
            json.dump(products, f, indent=4)
          totalBill=quantity*int( products[sp_id]['price'])
        else:
          print("Product not found!")
  continue_shopping=input("Do you want to buy more items(y/n):")
  if(continue_shopping=="y"):
    return sellProduct()
  else:
    generateRecipt(sp_id,quantity,totalBill)
    print("Thanks for shopping! Visit again!")
  
  
  
  
def generateRecipt(sp_id,quantity,totalBill):
    
    with open("products.json", "r") as f:
        products = json.load(f)
    
    product = products[sp_id]
    receipt = [(sp_id, product["name"], product["price"], quantity, totalBill)]
    headers = ["ID", "Name", "Price", "Quantity", "Total"]
    print(tabulate(receipt, headers=headers, tablefmt="grid"))

sellProduct()