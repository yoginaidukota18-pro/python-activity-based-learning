
# Multi-Currency Travel Budget Analysis

# Base currency: Indian Rupees (INR)
BASE_CURRENCY = "INR"

# Sample exchange rates: 1 unit of foreign currency = INR
exchange_rates = {
    "INR": 1.0,
    "USD": 84.0,
    "EUR": 92.0,
    "GBP": 108.0,
    "JPY": 0.56
}

# Currency conversion fee percentage
CONVERSION_FEE_RATE = 2.0

# Total travel budget in INR
budget = 100000

# Travel expenses
expenses = [
    {"category": "Flights", "amount": 400, "currency": "USD"},
    {"category": "Hotels", "amount": 300, "currency": "EUR"},
    {"category": "Food", "amount": 150, "currency": "GBP"},
    {"category": "Transport", "amount": 10000, "currency": "JPY"},
    {"category": "Shopping", "amount": 200, "currency": "USD"},
    {"category": "Activities", "amount": 100, "currency": "EUR"}
]


def convert_to_inr(amount, currency):
    if amount < 0:
        raise ValueError("Expense amount cannot be negative.")

    if currency not in exchange_rates:
        raise ValueError("Unsupported currency: " + currency)

    # Convert foreign currency into INR
    converted_amount = amount * exchange_rates[currency]

    # Apply conversion fee only to foreign currencies
    if currency != BASE_CURRENCY:
        fee = converted_amount * CONVERSION_FEE_RATE / 100
    else:
        fee = 0

    total = converted_amount + fee

    return converted_amount, fee, total


# Calculate all expenses
category_totals = {}
total_spending = 0

print("=" * 75)
print("             MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
print("=" * 75)

print(f"{'Category':<15}{'Original':>15}{'Currency':>10}"
      f"{'Fee (INR)':>15}{'Total (INR)':>15}")
print("-" * 75)

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]
    currency = expense["currency"]

    try:
        converted, fee, total = convert_to_inr(amount, currency)
    except ValueError as error:
        print(f"Skipping {category}: {error}")
        continue

    category_totals[category] = total
    total_spending += total

    print(
        f"{category:<15}"
        f"{amount:>15.2f}"
        f"{currency:>10}"
        f"{fee:>15.2f}"
        f"{total:>15.2f}"
    )

# Budget analysis
print("-" * 75)
print(f"Travel Budget       : Rs.{budget:.2f}")
print(f"Total Spending      : Rs.{total_spending:.2f}")

remaining = budget - total_spending

if remaining >= 0:
    print(f"Remaining Budget    : Rs.{remaining:.2f}")
    print("Budget Status       : Within Budget")
else:
    print(f"Budget Exceeded By  : Rs.{abs(remaining):.2f}")
    print("Budget Status       : Over Budget")

# Identify largest expense category
if category_totals:
    largest_category = max(category_totals, key=category_totals.get)

    print("\nLargest Expense Category:", largest_category)
    print(f"Category Total: Rs.{category_totals[largest_category]:.2f}")

    print("\nExpense Category Summary")
    print("-" * 40)

    for category, amount in sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        print(f"{category:<15} Rs.{amount:>10.2f}")

print("\nAnalysis completed successfully.")
