# Mini Student Profile App - W6 Lesson 4 Hands-On Exercise
# OOP demonstration: Classes, Inheritance, and Object Methods

# Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        # Store the three values in instance attributes
        self.name = name
        self.course = course
        self.year_level = year_level

    def get_profile(self):
        # Return the student's information using HTML-like tags
        profile = f"<h2>{self.name}</h2>\n"
        profile += f"<p>Course: {self.course}</p>\n"
        profile += f"<p>Year Level: {self.year_level}</p>"
        return profile


# Child class for an IT student inheriting from Student.
class ITStudent(Student):
    # Class attribute for programming skill
    skill = "Python"

    def get_skill(self):
        # Return the programming skill using a <p> tag
        return f"<p>Programming Skill: {self.skill}</p>"


# Application class with Flask-inspired routes.
class StudentApp:
    def __init__(self, title, student):
        # Store the title and student object
        self.title = title
        self.student = student

    def route(self, path):
        # Return the correct content for /, /profile, or an invalid route
        if path == "/":
            return f"<h1>{self.title}</h1>"
        elif path == "/profile":
            # Combine student profile with programming skill
            return self.student.get_profile() + "\n" + self.student.get_skill()
        else:
            # Handle invalid routes
            return "<h1>404 - Page Not Found</h1>"

    def run(self):
        # Print the app title and test the required routes
        print(f"Running: {self.title}\n")
        
        # Test route: /
        print("GET /")
        print(self.route("/"))
        print()
        
        # Test route: /profile
        print("GET /profile")
        print(self.route("/profile"))
        print()
        
        # Test invalid route
        print("GET /unknown")
        print(self.route("/unknown"))


# Create the student and application objects
student = ITStudent("Jels", "BS Information Technology", 2)
app = StudentApp("PSU Student Profile App", student)

# Start the application
app.run()
