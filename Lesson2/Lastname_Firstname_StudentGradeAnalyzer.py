# Store the raw comma-separated records.
raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
]

# Store the passing average.
PASSING_GRADE = 75

# Create the dictionary that will map names to score lists.
student_scores = {}

# PART A: Parse and organize the records.
print("Processing records...\n")

for record in raw_records:
    # Split the record into fields.
    fields = record.split(",")

    # Add a guardian condition for an invalid field count.
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    # Store the student's name.
    name = fields[0]

    # Convert the score fields to numbers safely.
    scores = []
    try:
        # Use list slicing to get scores (fields[1:])
        for score_str in fields[1:]:
            score = int(score_str)
            scores.append(score)
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    # Add the name and scores to student_scores.
    student_scores[name] = scores


# PART B: Display records alphabetically.
print("ORGANIZED STUDENT RECORDS")

# Sort the names and display every student and score list.
sorted_names = sorted(student_scores.keys())
for name in sorted_names:
    print(f"{name}: {student_scores[name]}")


# Create a list for result tuples.
ranking = []

# Create counters for the class summary.
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C: Calculate the student results.
for name, scores in student_scores.items():
    # Guard against an empty score list.
    if len(scores) == 0:
        continue

    # Calculate total, average, highest, and lowest.
    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    # Determine the student's remark.
    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    # Add the average to sum_of_averages.
    sum_of_averages += average

    # Append the result tuple to ranking.
    ranking.append((average, name, highest_score, lowest_score, remark))


# PART D: Sort and display the ranking.
# Sort ranking from highest to lowest average (descending order).
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

# Use enumerate() and tuple unpacking to display the ranking.
for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank}     {name:<9} {average:6.2f}    {highest_score:<7} {lowest_score:<6} {remark}")


# PART E: Display the class summary.
# Calculate the class average safely.
if len(student_scores) > 0:
    class_average = sum_of_averages / len(student_scores)
else:
    class_average = 0

# Use ranking[0] and ranking[-1] safely.
highest_student = ranking[0]
lowest_student = ranking[-1]

print("\nCLASS SUMMARY")
print(f"Number of Students: {len(student_scores)}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")


# PART F: Guardian conditions are implemented above
# Test with invalid records (uncomment to test)
print("\n" + "="*50)
print("Testing with invalid records:")
print("="*50 + "\n")

test_records = [
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

test_student_scores = {}

for record in test_records:
    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0]
    scores = []
    
    try:
        for score_str in fields[1:]:
            score = int(score_str)
            scores.append(score)
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    test_student_scores[name] = scores

print("\nValid test records stored:", test_student_scores)
