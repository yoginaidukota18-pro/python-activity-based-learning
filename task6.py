
# Railway Fare and Reservation Calculator

# Fare rates per kilometer for each travel class
CLASS_RATES = {
    "Sleeper": 1.0,
    "AC 3 Tier": 2.0,
    "AC 2 Tier": 3.0,
    "AC First Class": 4.0
}

# Reservation fees for each class
RESERVATION_FEES = {
    "Sleeper": 20,
    "AC 3 Tier": 40,
    "AC 2 Tier": 50,
    "AC First Class": 60
}

CANCELLATION_PENALTY = 20  # Percentage


def calculate_distance_fare(distance, rate):
    # Distance slab calculation
    if distance <= 100:
        fare = distance * rate
    elif distance <= 500:
        fare = 100 * rate + (distance - 100) * rate * 0.90
    else:
        fare = (
            100 * rate
            + 400 * rate * 0.90
            + (distance - 500) * rate * 0.80
        )

    return fare


def calculate_passenger_fare(passenger):
    age = passenger["age"]
    distance = passenger["distance"]
    travel_class = passenger["class"]

    # Validate passenger details
    if age < 0 or distance <= 0:
        return None, "Invalid age or distance"

    if travel_class not in CLASS_RATES:
        return None, "Invalid travel class"

    # Calculate distance-based fare
    rate = CLASS_RATES[travel_class]
    base_fare = calculate_distance_fare(distance, rate)

    # Apply age-based concessions
    concession_rate = 0

    if age < 5:
        concession_rate = 100
    elif age <= 12:
        concession_rate = 50
    elif age >= 60:
        concession_rate = 20

    concession = base_fare * concession_rate / 100
    discounted_fare = base_fare - concession

    # Add reservation fee
    reservation_fee = RESERVATION_FEES[travel_class]
    total_fare = discounted_fare + reservation_fee

    # Apply cancellation penalty if ticket is cancelled
    cancellation_fee = 0
    refund = 0

    if passenger["cancelled"]:
        cancellation_fee = total_fare * CANCELLATION_PENALTY / 100
        refund = total_fare - cancellation_fee

    return {
        "base_fare": base_fare,
        "concession": concession,
        "reservation_fee": reservation_fee,
        "total_fare": total_fare,
        "cancellation_fee": cancellation_fee,
        "refund": refund
    }, None


# Passenger reservation details
passengers = [
    {
        "name": "Ganesh",
        "age": 19,
        "distance": 350,
        "class": "Sleeper",
        "cancelled": False
    },
    {
        "name": "Rahul",
        "age": 10,
        "distance": 350,
        "class": "AC 3 Tier",
        "cancelled": False
    },
    {
        "name": "Priya",
        "age": 65,
        "distance": 600,
        "class": "AC 2 Tier",
        "cancelled": True
    },
    {
        "name": "Sita",
        "age": 30,
        "distance": 150,
        "class": "AC First Class",
        "cancelled": False
    }
]


# Process all passenger reservations
print("=" * 60)
print("       RAILWAY FARE AND RESERVATION SYSTEM")
print("=" * 60)

total_collection = 0
total_refunds = 0

for passenger in passengers:
    result, error = calculate_passenger_fare(passenger)

    print(f"\nPassenger: {passenger['name']}")

    if error:
        print("Error:", error)
        continue

    print(f"Age              : {passenger['age']}")
    print(f"Distance         : {passenger['distance']} km")
    print(f"Travel Class     : {passenger['class']}")
    print(f"Base Fare        : Rs.{result['base_fare']:.2f}")
    print(f"Age Concession   : Rs.{result['concession']:.2f}")
    print(f"Reservation Fee  : Rs.{result['reservation_fee']:.2f}")
    print(f"Total Fare       : Rs.{result['total_fare']:.2f}")

    if passenger["cancelled"]:
        print("Status           : Cancelled")
        print(
            f"Cancellation Fee : Rs.{result['cancellation_fee']:.2f}"
        )
        print(f"Refund Amount    : Rs.{result['refund']:.2f}")
        total_refunds += result["refund"]
    else:
        print("Status           : Confirmed")
        total_collection += result["total_fare"]

print("\n" + "=" * 60)
print("RESERVATION SUMMARY")
print("=" * 60)
print(f"Confirmed Fare Collection: Rs.{total_collection:.2f}")
print(f"Total Refunds            : Rs.{total_refunds:.2f}")
print("Reservations processed successfully.")
