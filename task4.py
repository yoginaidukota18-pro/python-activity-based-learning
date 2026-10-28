
# Employee Payroll and Deduction Analysis

# Progressive deduction rates (illustrative)
def calculate_deduction(gross_salary):
    deduction = 0

    if gross_salary <= 20000:
        deduction = gross_salary * 0.05
    elif gross_salary <= 50000:
        deduction = (20000 * 0.05) + (
            (gross_salary - 20000) * 0.10
        )
    else:
        deduction = (
            (20000 * 0.05)
            + (30000 * 0.10)
            + ((gross_salary - 50000) * 0.15)
        )

    return deduction


def calculate_payroll(employee):
    basic = employee["basic"]
    allowances = employee["allowances"]
    overtime_hours = employee["overtime_hours"]
    overtime_rate = employee["overtime_rate"]
    incentives = employee["incentives"]

    # Validate inputs
    if min(
        basic, allowances, overtime_hours,
        overtime_rate, incentives
    ) < 0:
        return None

    # Calculate salary components
    overtime_pay = overtime_hours * overtime_rate
    gross_salary = (
        basic + allowances + overtime_pay + incentives
    )

    # Calculate progressive deductions
    deductions = calculate_deduction(gross_salary)

    # Calculate net salary
    net_salary = gross_salary - deductions

    return {
        "basic": basic,
        "allowances": allowances,
        "overtime_pay": overtime_pay,
        "incentives": incentives,
        "gross_salary": gross_salary,
        "deductions": deductions,
        "net_salary": net_salary
    }


# Employee records
employees = [
    {
        "id": 101,
        "name": "Ganesh",
        "basic": 25000,
        "allowances": 5000,
        "overtime_hours": 10,
        "overtime_rate": 200,
        "incentives": 3000
    },
    {
        "id": 102,
        "name": "Rahul",
        "basic": 18000,
        "allowances": 3000,
        "overtime_hours": 5,
        "overtime_rate": 150,
        "incentives": 1000
    },
    {
        "id": 103,
        "name": "Priya",
        "basic": 40000,
        "allowances": 8000,
        "overtime_hours": 8,
        "overtime_rate": 250,
        "incentives": 5000
    }
]


# Generate salary statements
print("=" * 55)
print("          EMPLOYEE SALARY STATEMENT")
print("=" * 55)

for employee in employees:
    result = calculate_payroll(employee)

    print(f"\nEmployee ID   : {employee['id']}")
    print(f"Employee Name : {employee['name']}")
    print("-" * 55)

    if result is None:
        print("Invalid salary data. Please check the inputs.")
        continue

    print(f"Basic Pay       : Rs.{result['basic']:,.2f}")
    print(f"Allowances      : Rs.{result['allowances']:,.2f}")
    print(f"Overtime Pay    : Rs.{result['overtime_pay']:,.2f}")
    print(f"Incentives      : Rs.{result['incentives']:,.2f}")
    print("-" * 55)
    print(f"Gross Salary    : Rs.{result['gross_salary']:,.2f}")
    print(f"Total Deductions: Rs.{result['deductions']:,.2f}")
    print(f"Net Salary      : Rs.{result['net_salary']:,.2f}")
    print("=" * 55)

print("\nPayroll processing completed successfully.")
