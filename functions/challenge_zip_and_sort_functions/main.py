# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

product_name = "Banana", "Apple", "Mango", "Cherry"
price = 1.20, 0.50 ,2.50 , 1.75 
quantity_sold = 50, 100 , 25 , 40 

combined_list = list(zip( product_name, price, quantity_sold))

sorted_products = sorted(combined_list)
for item in sorted_products:
    print(f"Product:{item[0]} , Price:{item[1]} , Quantity Sold: {item[2]}")
