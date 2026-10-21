"""Student Grade Analyzer - Completed

Complete student grade analysis program with file I/O, validation, and reporting.
"""


def classify_grade(grade):
    """Return the classification and status of a grade."""
    if grade >= 90:
        return ("Excellent", "Passed")
    elif grade >= 85:
        return ("Very Good", "Passed")
    elif grade >= 80:
        return ("Good", "Passed")
    elif grade >= 75:
        return ("Satisfactory", "Passed")
    else:
        return ("Needs Improvement", "Failed")


def load_students(filename):
    """Read valid student records from a text file and return them as a list."""
    students = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                
                # Skip blank lines
                if not line:
                    continue
                
                # Split the record
                parts = line.split(",")
                
                # Check for exactly three fields
                if len(parts) != 3:
                    continue
                
                student_id = parts[0].strip()
                name = parts[1].strip()
                
                try:
                    grade = float(parts[2].strip())
                    
                    # Validate grade range
                    if 0 <= grade <= 100:
                        students.append({
                            "student_id": student_id,
                            "name": name,
                            "grade": grade
                        })
                except ValueError:
                    # Invalid numeric grade, skip this record
                    continue
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return students


def calculate_statistics(students):
    """Calculate and return the class statistics."""
    if not students:
        return None
    
    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]
    
    for student in students:
        grade = student["grade"]
        total_grade += grade
        
        # Count passed/failed
        if grade >= 75:
            passed_count += 1
        else:
            failed_count += 1
        
        # Track highest
        if grade > highest_student["grade"]:
            highest_student = student
        
        # Track lowest
        if grade < lowest_student["grade"]:
            lowest_student = student
    
    average = total_grade / len(students)
    
    return {
        "num_students": len(students),
        "average": average,
        "passed": passed_count,
        "failed": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table."""
    print("\n" + "="*80)
    print(f"{'Student ID':<12} {'Name':<20} {'Grade':>8} {'Classification':<18} {'Status':<10}")
    print("="*80)
    
    for student in students:
        student_id = student["student_id"]
        name = student["name"][:20]  # Slice to max 20 chars
        grade = student["grade"]
        classification, status = classify_grade(grade)
        
        print(f"{student_id:<12} {name:<20} {grade:>8.2f} {classification:<18} {status:<10}")
    
    print("="*80)


def display_statistics(statistics):
    """Display the calculated class statistics."""
    if statistics is None:
        print("No statistics available.")
        return
    
    print("\n" + "="*50)
    print("CLASS STATISTICS")
    print("="*50)
    print(f"Number of students: {statistics['num_students']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed']}")
    print(f"Failed: {statistics['failed']}")
    print(f"Highest: {statistics['highest_student']['name']} - {statistics['highest_student']['grade']:.2f}")
    print(f"Lowest: {statistics['lowest_student']['name']} - {statistics['lowest_student']['grade']:.2f}")
    print("="*50)


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword."""
    matches = []
    keyword = keyword.strip().lower()
    
    for student in students:
        student_id = student["student_id"].lower()
        name = student["name"].lower()
        
        # Check for partial matches in both ID and name
        if keyword in student_id or keyword in name:
            matches.append(student)
    
    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file."""
    try:
        with open(filename, 'w') as file:
            file.write("="*80 + "\n")
            file.write("STUDENT GRADE ANALYZER REPORT\n")
            file.write("="*80 + "\n\n")
            
            # Student results
            file.write(f"{'Student ID':<12} {'Name':<20} {'Grade':>8} {'Classification':<18} {'Status':<10}\n")
            file.write("-"*80 + "\n")
            
            for student in students:
                student_id = student["student_id"]
                name = student["name"]
                grade = student["grade"]
                classification, status = classify_grade(grade)
                file.write(f"{student_id:<12} {name:<20} {grade:>8.2f} {classification:<18} {status:<10}\n")
            
            file.write("\n" + "="*80 + "\n")
            file.write("CLASS STATISTICS\n")
            file.write("="*80 + "\n")
            
            if statistics:
                file.write(f"Number of students: {statistics['num_students']}\n")
                file.write(f"Class average: {statistics['average']:.2f}\n")
                file.write(f"Passed: {statistics['passed']}\n")
                file.write(f"Failed: {statistics['failed']}\n")
                file.write(f"Highest: {statistics['highest_student']['name']} - {statistics['highest_student']['grade']:.2f}\n")
                file.write(f"Lowest: {statistics['lowest_student']['name']} - {statistics['lowest_student']['grade']:.2f}\n")
            
            print(f"Report saved to '{filename}'.")
    
    except OSError as e:
        print(f"Error saving report: {e}")


def main():
    """Run the menu-driven Student Grade Analyzer."""
    students = load_students("grades.txt")
    
    if not students:
        print("No valid student records were loaded.")
        return
    
    statistics = calculate_statistics(students)
    
    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student ID or name to search: ")
            matches = search_student(students, keyword)
            if matches:
                print(f"\nFound {len(matches)} match(es):\n")
                display_students(matches)
            else:
                print("No matching students found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Thank you for using the Student Grade Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()