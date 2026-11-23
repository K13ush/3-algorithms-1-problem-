n = 4

# Plan: one formula - no loop needed
total = n * (n + 1) // 2  # steps = 1

# Plan: add each student's points one by one
total = 0
for student in range(1, n + 1):
    total += student  # steps = 4

# Plan: count every single point - loop inside a loop
total = 0
for student in range(1, n + 1):
    for point in range(1, student + 1):
        total += 1       # steps = 10
        