
# Manufacturing Cost and Profitability Analysis

# Profit target percentage
PROFIT_TARGET = 20

# Manufacturing product details
products = [
    {
        "name": "Product A",
        "material_cost": 10000,
        "labour_cost": 5000,
        "wastage_rate": 5,
        "machine_cost": 2000,
        "quantity": 100,
        "selling_price": 250
    },
    {
        "name": "Product B",
        "material_cost": 15000,
        "labour_cost": 7000,
        "wastage_rate": 8,
        "machine_cost": 3000,
        "quantity": 100,
        "selling_price": 350
    },
    {
        "name": "Product C",
        "material_cost": 8000,
        "labour_cost": 4000,
        "wastage_rate": 3,
        "machine_cost": 1500,
        "quantity": 100,
        "selling_price": 160
    }
]


def analyze_product(product):
    material = product["material_cost"]
    labour = product["labour_cost"]
    wastage_rate = product["wastage_rate"]
    machine = product["machine_cost"]
    quantity = product["quantity"]
    selling_price = product["selling_price"]

    # Validate input values
    if min(
        material, labour, wastage_rate,
        machine, quantity, selling_price
    ) < 0 or quantity == 0 or wastage_rate > 100:
        return None

    # Calculate wastage cost based on material cost
    wastage_cost = material * wastage_rate / 100

    # Calculate total production cost
    total_cost = material + labour + wastage_cost + machine

    # Calculate revenue and profit
    total_revenue = selling_price * quantity
    profit = total_revenue - total_cost

    # Calculate profit percentage on production cost
    profit_percentage = (
        profit / total_cost * 100
        if total_cost > 0 else 0
    )

    # Check profit target
    if profit_percentage >= PROFIT_TARGET:
        status = "Profit Target Achieved"
    elif profit > 0:
        status = "Profit Target Not Achieved"
    else:
        status = "Loss"

    # Calculate break-even selling price per unit
    break_even_price = total_cost / quantity

    return {
        "wastage_cost": wastage_cost,
        "total_cost": total_cost,
        "total_revenue": total_revenue,
        "profit": profit,
        "profit_percentage": profit_percentage,
        "break_even_price": break_even_price,
        "status": status
    }


# Analyze all products
print("=" * 65)
print("      MANUFACTURING COST AND PROFITABILITY ANALYSIS")
print("=" * 65)

for product in products:
    result = analyze_product(product)

    print(f"\nProduct Name: {product['name']}")
    print("-" * 65)

    if result is None:
        print("Invalid product data. Please check the inputs.")
        continue

    print(f"Material Cost       : Rs.{product['material_cost']:.2f}")
    print(f"Labour Charges      : Rs.{product['labour_cost']:.2f}")
    print(f"Wastage Cost        : Rs.{result['wastage_cost']:.2f}")
    print(f"Machine Cost        : Rs.{product['machine_cost']:.2f}")
    print(f"Total Production Cost: Rs.{result['total_cost']:.2f}")
    print(f"Production Quantity : {product['quantity']}")
    print(f"Selling Price/Unit  : Rs.{product['selling_price']:.2f}")
    print(f"Total Revenue       : Rs.{result['total_revenue']:.2f}")
    print(f"Total Profit/Loss   : Rs.{result['profit']:.2f}")
    print(f"Profit Percentage   : {result['profit_percentage']:.2f}%")
    print(f"Break-even Price    : Rs.{result['break_even_price']:.2f}")
    print(f"Profitability Status: {result['status']}")

print("\n" + "=" * 65)
print(f"Required Profit Target: {PROFIT_TARGET}%")
print("Analysis Completed Successfully.")
print("=" * 65)
