
# Multi-Plan Telecommunications Cost Optimization

# User requirements
data_required = 25       # GB
calls_required = 500     # minutes
validity_required = 28   # days
budget = 500             # Rs.

# Mobile plan details
plans = [
    {
        "name": "Basic Plan",
        "price": 199,
        "data": 15,
        "calls": 300,
        "validity": 28,
        "extra_data_rate": 20,
        "extra_call_rate": 0.50
    },
    {
        "name": "Standard Plan",
        "price": 349,
        "data": 30,
        "calls": 600,
        "validity": 28,
        "extra_data_rate": 15,
        "extra_call_rate": 0.40
    },
    {
        "name": "Premium Plan",
        "price": 499,
        "data": 50,
        "calls": 1000,
        "validity": 56,
        "extra_data_rate": 10,
        "extra_call_rate": 0.30
    },
    {
        "name": "Value Plan",
        "price": 299,
        "data": 25,
        "calls": 500,
        "validity": 30,
        "extra_data_rate": 12,
        "extra_call_rate": 0.35
    }
]

results = []

# Evaluate each mobile plan
for plan in plans:
    # Calculate excess usage
    extra_data = max(0, data_required - plan["data"])
    extra_calls = max(0, calls_required - plan["calls"])

    # Calculate excess charges
    data_charge = extra_data * plan["extra_data_rate"]
    call_charge = extra_calls * plan["extra_call_rate"]

    total_cost = plan["price"] + data_charge + call_charge

    # Check eligibility constraints
    eligible = (
        plan["data"] >= data_required
        and plan["calls"] >= calls_required
        and plan["validity"] >= validity_required
        and total_cost <= budget
    )

    results.append({
        "name": plan["name"],
        "base_price": plan["price"],
        "extra_data": extra_data,
        "extra_calls": extra_calls,
        "data_charge": data_charge,
        "call_charge": call_charge,
        "total_cost": total_cost,
        "validity": plan["validity"],
        "eligible": eligible
    })

# Display comparison
print("=" * 70)
print("       MOBILE PLAN COST OPTIMIZATION")
print("=" * 70)

for result in results:
    print(f"\nPlan: {result['name']}")
    print(f"Base Price       : Rs.{result['base_price']:.2f}")
    print(f"Extra Data       : {result['extra_data']} GB")
    print(f"Extra Calls      : {result['extra_calls']} minutes")
    print(f"Data Charges     : Rs.{result['data_charge']:.2f}")
    print(f"Call Charges     : Rs.{result['call_charge']:.2f}")
    print(f"Total Cost       : Rs.{result['total_cost']:.2f}")
    print(f"Validity         : {result['validity']} days")
    print("Eligibility      :", 
          "Eligible" if result["eligible"] else "Not Eligible")

# Find the most economical eligible plan
eligible_plans = [
    result for result in results if result["eligible"]
]

print("\n" + "=" * 70)
print("FINAL RECOMMENDATION")
print("=" * 70)

if eligible_plans:
    best_plan = min(
        eligible_plans,
        key=lambda result: (
            result["total_cost"],
            -result["validity"],
            result["name"]
        )
    )

    print("Best Plan        :", best_plan["name"])
    print(f"Total Cost       : Rs.{best_plan['total_cost']:.2f}")
    print(f"Validity         : {best_plan['validity']} days")
    print(f"Money Remaining  : Rs.{budget - best_plan['total_cost']:.2f}")
else:
    print("No plan satisfies all usage, validity, and budget constraints.")
    print("Consider increasing the budget or adjusting requirements.")

print("\nPlan comparison completed.")
