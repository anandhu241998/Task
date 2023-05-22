# Product catalog
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.1),
    "tiered_50_discount": (30, 0.5)
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

# Initialize variables
subtotal = 0
discount_name = ""
discount_amount = 0
gift_wrap_total = 0
shipping_fee = 0
total = 0

# Get quantity and gift wrap information for each product
for product, price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product}: "))
    is_gift_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"

    # Calculate product total
    product_total = price * quantity
    subtotal += product_total

    # Calculate gift wrap fee
    if is_gift_wrapped:
        gift_wrap_total += gift_wrap_fee * quantity

    # Check discount rules and apply the most beneficial one
    for rule, (rule_quantity, rule_discount) in discount_rules.items():
        if quantity > rule_quantity:
            discount = min(quantity - rule_quantity, quantity) * price * rule_discount
            if discount > discount_amount:
                discount_name = rule
                discount_amount = discount

# Calculate shipping fee
shipping_fee = (subtotal - discount_amount) // items_per_package * shipping_fee_per_package

# Calculate total
total = subtotal + gift_wrap_total - discount_amount + shipping_fee

# Output the details
print("------ Order Details ------")
for product, price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product}: "))
    is_gift_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"
    product_total = price * quantity
    print(f"{product}: {quantity} x ${price} = ${product_total}")

print(f"\nSubtotal: ${subtotal}")
print(f"Discount applied: {discount_name} (${discount_amount})")
print(f"Shipping fee: ${shipping_fee}")
print(f"Gift wrap fee: ${gift_wrap_total}")
print(f"\nTotal: ${total}")
