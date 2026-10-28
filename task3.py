
# Hospital Billing and Patient Classification System

# Billing policy
CONSULTATION_FEE = 500
DIAGNOSTIC_FEE = 1000
TREATMENT_FEE = 3000

SENIOR_AGE = 60
SENIOR_DISCOUNT = 10       # 10% discount
MIN_DISCOUNT_BILL = 5000
HIGH_BILL_LIMIT = 10000

# Patient details
patients = [
    {
        "name": "Ganesh",
        "age": 20,
        "diagnostic": True,
        "treatment": True,
        "payment": 5000
    },
    {
        "name": "Rahul",
        "age": 65,
        "diagnostic": True,
        "treatment": True,
        "payment": 7000
    },
    {
        "name": "Priya",
        "age": 35,
        "diagnostic": False,
        "treatment": True,
        "payment": 1000
    },
    {
        "name": "Sita",
        "age": 70,
        "diagnostic": True,
        "treatment": False,
        "payment": 2000
    }
]


def calculate_bill(patient):
    # Validate patient information
    if patient["age"] < 0 or patient["payment"] < 0:
        return None, "Invalid patient data"

    consultation = CONSULTATION_FEE
    diagnostic = DIAGNOSTIC_FEE if patient["diagnostic"] else 0
    treatment = TREATMENT_FEE if patient["treatment"] else 0

    subtotal = consultation + diagnostic + treatment

    # Apply conditional concession
    discount = 0

    if patient["age"] >= SENIOR_AGE:
        discount = subtotal * SENIOR_DISCOUNT / 100
    elif subtotal >= MIN_DISCOUNT_BILL:
        discount = subtotal * 5 / 100

    total_bill = subtotal - discount

    # Validate billing constraints
    if total_bill < 0 or discount > subtotal:
        return None, "Billing constraint violated"

    balance = total_bill - patient["payment"]

    # Classify patient by payment status
    if balance <= 0:
        status = "Fully Paid"
        balance = 0
    elif patient["payment"] == 0:
        status = "Unpaid"
    elif patient["payment"] < total_bill:
        status = "Partially Paid"
    else:
        status = "Fully Paid"

    # High bill warning
    if total_bill >= HIGH_BILL_LIMIT:
        status += " - High Bill"

    return {
        "consultation": consultation,
        "diagnostic": diagnostic,
        "treatment": treatment,
        "subtotal": subtotal,
        "discount": discount,
        "total": total_bill,
        "paid": patient["payment"],
        "balance": balance,
        "status": status
    }, None


# Process all patients
print("HOSPITAL BILLING SYSTEM")
print("=" * 55)

for patient in patients:
    bill, error = calculate_bill(patient)

    print(f"\nPatient: {patient['name']}")

    if error:
        print("Error:", error)
        continue

    print(f"Consultation Charge: Rs.{bill['consultation']:.2f}")
    print(f"Diagnostic Charge:   Rs.{bill['diagnostic']:.2f}")
    print(f"Treatment Charge:    Rs.{bill['treatment']:.2f}")
    print(f"Subtotal:            Rs.{bill['subtotal']:.2f}")
    print(f"Concession:          Rs.{bill['discount']:.2f}")
    print(f"Final Bill:          Rs.{bill['total']:.2f}")
    print(f"Amount Paid:         Rs.{bill['paid']:.2f}")
    print(f"Balance Due:         Rs.{bill['balance']:.2f}")
    print(f"Patient Status:      {bill['status']}")

print("\nBilling process completed.")
