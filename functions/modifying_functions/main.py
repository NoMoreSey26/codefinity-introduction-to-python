def apply_discount(price, discount=0.05):
    apply_discount = price * (1 - discount)
    return apply_discount
def apply_tax(price,  tax=0.07):
    apply_tax = price * (1 + tax)
    return apply_tax
def calculate_total(price, discount=0.05, tax=0.07):
    calculate_total =  price *(1- discount) * (1 + tax)
    return calculate_total

total_price_default = calculate_total(120)
total_price_custom = calculate_total(100, discount=0.10 , tax=0.08)

print(f"Total cost with default discount and tax: ${total_price_default:.2f}")
print(f"Total cost with custom discount and tax: ${total_price_custom:.2f}")