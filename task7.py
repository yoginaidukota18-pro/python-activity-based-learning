
# Retail Billing with Multiple Discount Rules

# Product details: name, category, price, quantity
products = [
    {"name": "Laptop", "category": "Electronics",
     "price": 50000, "quantity": 1},
    {"name": "T-Shirt", "category": "Clothing",
     "price": 1000, "quantity": 2},
    {"name": "Notebook", "category": "Stationery",
     "price": 100, "quantity": 5},
    {"name": "Headphones", "category": "Electronics",
     "price": 2000, "quantity": 1}
]

# Category-specific tax rates (illustrative)
TAX_RATES = {
    "Electronics": 18,
    "Clothing": 5,
    "Stationery": 12
}

# Discount rules
THRESHOLD_1 = 5000
THRESHOLD_2 = 20000
DISCOUNT_1 = 5
DISCOUNT_2 = 10
MAX_CONCESSION = 5000


def calculate_bill(products):
    subtotal = 0
    item_details = []

    # Validate and calculate each item
    for product in products:
        price = product["price"]
        quantity = product["quantity"]
        category = product["category"]

        if price < 0 or quantity <= 0:
            print("Invalid product:", product["name"])
            continue

        if category not in TAX_RATES:
            print("Unknown category:", category)
            continue

        amount = price * quantity
        tax_rate = TAX_RATES[category]
        tax = amount * tax_rate / 100

        subtotal += amount

        item_details.append({
            "name": product["name"],
            "category": category,
            "price": price,
            "quantity": quantity,
            "amount": amount,
            "tax_rate": tax_rate,
            "tax": tax
        })

    # Calculate threshold discount
    if subtotal >= THRESHOLD_2:
        discount_rate = DISCOUNT_2
    elif subtotal >= THRESHOLD_1:
        discount_rate = DISCOUNT_1
    else:
        discount_rate = 0

    discount = subtotal * discount_rate / 100

    # Apply maximum concession limit
    discount = min(discount, MAX_CONCESSION)

    # Calculate total tax
    total_tax = sum(item["tax"] for item in item_details)

    # Calculate final amount
    final_amount = subtotal - discount + total_tax

    return subtotal, discount, total_tax, final_amount, item_details


# Generate invoice
subtotal, discount, total_tax, final_amount, items = calculate_bill(
    products
)

print("=" * 85)
print("                         RETAIL STORE INVOICE")
print("=" * 85)

print(f"{'Product':<15}{'Category':<15}{'Price':>10}"
      f"{'Qty':>6}{'Amount':>12}{'Tax':>10}")
print("-" * 85)

for item in items:
    print(
        f"{item['name']:<15}"
        f"{item['category']:<15}"
        f"{item['price']:>10.2f}"
        f"{item['quantity']:>6}"
        f"{item['amount']:>12.2f}"
        f"{item['tax']:>10.2f}"
    )

print("-" * 85)
print(f"{'Subtotal:':<60} Rs.{subtotal:>10.2f}")
print(f"{'Discount:':<60} Rs.{discount:>10.2f}")
print(f"{'Total Tax:':<60} Rs.{total_tax:>10.2f}")
print("=" * 85)
print(f"{'FINAL AMOUNT:':<60} Rs.{final_amount:>10.2f}")
print("=" * 85)
print("Thank you for shopping!")
