import json
from school import Student

# Read JSON data
with open("students.json", "r") as file:
  students_data = json.load(file)

# Convert data to Student objects
students = [Student(data) for data in students_data]

# Find youngest and oldest students
youngest_student = min(students, key=lambda s: s.age)
oldest_student = max(students, key=lambda s: s.age)

# Calculate average age
average_age = sum(s.age for s in students) // len(students)

# Find students with low attendance
bad_students = [s for s in students if s.attendance < 30]

# Print results
print(f"Youngest: {youngest_student.name}")
print(f"Oldest: {oldest_student.name}")
print(f"Average age: {average_age}")
print("Bad students:")
for student in bad_students:
  print(f"- {student.name}")
