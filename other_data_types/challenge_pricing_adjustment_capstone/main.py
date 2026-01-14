grocery_inventory = {"Milk":("Dairy",3.50,8) , "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99,15), "Apples": ("Produce", 1.50, 50)}
eggs_tuple = grocery_inventory.get("Eggs")
eggs_price = eggs_tuple[1]
if eggs_price > 5:
    print("eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (eggs_tuple[0], eggs_price - 1, eggs_tuple[2])
else:
        print ("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes": ("Produce",1.20,30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
milk_tuple = grocery_inventory.get("Milk")
milk_stock = milk_tuple[2]
if milk_stock < 10:
    print("milk needs to be restocked. increasing stock by 20 units.")
    grocery_inventory["Milk"] = (milk_tuple[0] , milk_tuple[1] , milk_stock + 20)
else:
    print("Milk has sufficient stock.")

apples_tuple =  grocery_inventory.get("Apples")
apples_price = apples_tuple[1]
if apples_price > 2 :
    grocery_inventory.pop("Apples") 
    print("Apple removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)