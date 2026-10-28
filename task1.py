
# University Scholarship Allocation System

students = [
    {
        "name": "Ganesh",
        "marks": 92,
        "subjects": [90, 95, 88],
        "attendance": 95,
        "income": 150000
    },
    {
        "name": "Rahul",
        "marks": 85,
        "subjects": [80, 75, 90],
        "attendance": 90,
        "income": 200000
    },
    {
        "name": "Priya",
        "marks": 92,
        "subjects": [92, 90, 95],
        "attendance": 98,
        "income": 120000
    },
    {
        "name": "Sita",
        "marks": 78,
        "subjects": [70, 75, 80],
        "attendance": 85,
        "income": 180000
    },
    {
        "name": "Arjun",
        "marks": 88,
        "subjects": [85, 90, 87],
        "attendance": 92,
        "income": 350000
    }
]

# Scholarship eligibility criteria
MIN_AGGREGATE = 80
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

eligible_students = []
rejected_students = []

# Check eligibility
for student in students:
    if (
        student["marks"] >= MIN_AGGREGATE
        and min(student["subjects"]) >= MIN_SUBJECT_MARKS
        and student["attendance"] >= MIN_ATTENDANCE
        and student["income"] <= MAX_INCOME
    ):
        eligible_students.append(student)
    else:
        rejected_students.append(student)

# Ranking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Name in alphabetical order
eligible_students.sort(
    key=lambda s: (
        -s["marks"],
        -s["attendance"],
        s["income"],
        s["name"]
    )
)

# Display eligible students
print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("-" * 65)

if eligible_students:
    print("\nEligible Students and Rankings:")
    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"{rank}. {student['name']} | "
            f"Marks: {student['marks']}% | "
            f"Attendance: {student['attendance']}% | "
            f"Income: Rs.{student['income']}"
        )
else:
    print("\nNo students are eligible for the scholarship.")

# Display rejected students
print("\nStudents Not Eligible:")
for student in rejected_students:
    print(student["name"])

print("\nTotal Applicants:", len(students))
print("Total Eligible:", len(eligible_students))
print("Total Not Eligible:", len(rejected_students))
