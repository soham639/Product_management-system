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
 
   
    
