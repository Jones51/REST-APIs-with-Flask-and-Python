friends_age = {'Rolf': 24, "Adam": 30 }

#Adding
friends_age["Bob"] = 30

print(friends_age)

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 23},
    {"name": "Jones", "age": 30},
]

print(friends[0]["name"])

student_attendance = {"Rolf": 96, "Bob": 50, "Carlos": 33}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")