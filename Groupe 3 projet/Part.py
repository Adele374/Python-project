
import datetime

# STUDENT CLASS
class Student:
    """Class to represent a student"""
    
    # Class attribute to keep track of total students in the school
    total_students = 0
    school_year = 2025
    
    def __init__(self, name, age, school, department, level, student_id, height, weight, email):
        """Constructor - initializes a new student"""
        self.name = name
        self.age = age
        self.school = school
        self.department = department
        self.level = level
        self.student_id = student_id
        self.height = height
        self.weight = weight
        self.email = email
        self.is_registered = False
        self.courses = []
        Student.total_students += 1
    
    def calculate_bmi(self):
        """Method to calculate BMI (Body Mass Index)"""
        if self.height > 0:
            bmi = self.weight / (self.height ** 2)
            return round(bmi, 2)
        return 0
    
    def get_bmi_category(self):
        """Method to determine BMI category"""
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def calculate_age_next_year(self):
        """Method to calculate age next year"""
        return self.age + 1
    
    def years_at_school(self):
        """Method to calculate years spent at school"""
        return self.level - 1
    
    def add_course(self, course_name, credits):
        """Method to add a course"""
        self.courses.append({"name": course_name, "credits": credits})
    
    def total_credits(self):
        """Method to calculate total credits"""
        total = 0
        for course in self.courses:
            total += course["credits"]
        return total
    
    def register(self):
        """Method to register the student"""
        self.is_registered = True
    
    def get_status(self):
        """Method to get academic status"""
        if self.level == 1:
            return "First year"
        elif self.level == 2:
            return "Second year"
        elif self.level == 3:
            return "Third year"
        elif self.level == 4:
            return "Fourth year"
        else:
            return f"Level {self.level}"
    
    def display_summary(self):
        """Method to display complete summary"""
        print("\n" + "="*50)
        print("           STUDENT SUMMARY")
        print("="*50)
        print(f"Full name: {self.name}")
        print(f"Current age: {self.age} years old")
        print(f"Age next year: {self.calculate_age_next_year()} years old")
        print(f"School: {self.school}")
        print(f"Department: {self.department}")
        print(f"Level: {self.level} ({self.get_status()})")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.email}")
        print(f"Status: {'Registered' if self.is_registered else 'Not registered'}")
        print("-"*50)
        print(f"Height: {self.height} m")
        print(f"Weight: {self.weight} kg")
        print(f"BMI: {self.calculate_bmi()}")
        print(f"BMI Category: {self.get_bmi_category()}")
        print("-"*50)
        print(f"Years already spent: {self.years_at_school()}")
        print(f"Creation year: {Student.school_year}")
        
        if len(self.courses) > 0:
            print("-"*50)
            print("ENROLLED COURSES:")
            for i, course in enumerate(self.courses, 1):
                print(f"  {i}. {course['name']} - {course['credits']} credits")
            print(f"Total credits: {self.total_credits()}")
        
        print("="*50)


# functions

def display_menu():
    """Function to display main menu"""
    print(".............................................................")
    print("        STUDENT CARD GENERATOR")
    print(".............................................................")
    print("1. Create a new student profile")
    print("2. Display all students")
    print("3. Exit")
    print("="*60)

def validate_age():
    """Function to validate age with loop"""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0 and age < 100:
                return age
            else:
                print("Invalid age! Must be between 1 and 99.")
        except ValueError:
            print("Error! Enter a valid number.")

def validate_level():
    """Function to validate academic level"""
    while True:
        try:
            level = int(input("Enter your academic level (1-7): "))
            if 1 <= level <= 7:
                return level
            else:
                print("Invalid level! Must be between 1 and 7.")
        except ValueError:
            print("Error! Enter a valid number.")

def validate_float(message, min_val=0.0, max_val=300.0):
    """Generic function to validate a decimal number"""
    while True:
        try:
            value = float(input(message))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Invalid value! Must be between {min_val} and {max_val}.")
        except ValueError:
            print("Error! Enter a valid decimal number.")

def validate_yes_no(message):
    """Function to validate a yes/no response"""
    while True:
        response = input(message).lower()
        if response in ["yes", "no", "y", "n"]:
            return response in ["yes", "y"]
        else:
            print("Please answer 'yes' or 'no'.")

def create_student():
    """Function to create a new student"""
    print("......................................................")
    print("    CREATING A NEW PROFILE")
    print("......................................................")
    
    # informations needed
    name = input("Full name: ")
    while len(name) < 3:
        print("Name must contain at least 3 characters!")
        name = input("Your full name: ")
    
    age = validate_age()
    school = input("School name: ")
    department = input("Department: ")
    level = validate_level()
    student_id = input("Student ID number: ")
    
    height = validate_float("Height in meters (e.g., 1.75): ", 0.5, 2.5)
    weight = validate_float("Weight in kg: ", 30.0, 200.0)
    
    email = input("University email: ")
    while "@" not in email:
        print("Invalid email! Must contain @")
        email = input("University email: ")
    
    # Create Student object
    student = Student(name, age, school, department, level, student_id, height, weight, email)
    
    
    if validate_yes_no("Are you registered? (yes/no): "):
        student.register()
    
    # Add new courses
    if validate_yes_no("Do you want to add courses? (yes/no): "):
        while True:
            course_name = input("Course name: ")
            credits = validate_float("Number of credits: ", 1, 10)
            student.add_course(course_name, int(credits))
            
            if not validate_yes_no("Add another course? (yes/no): "):
                break
    
    return student

def display_all_students(student_list):
    """Function to display all students"""
    if len(student_list) == 0:
        print("\nNo students registered at the moment.")
        return
    
    print("\n" + "="*50)
    print(f"    STUDENT LIST ({len(student_list)} total)")
    print("="*50)
    
    for i, student in enumerate(student_list, 1):
        print(f"\n--- Student #{i} ---")
        print(f"Name: {student.name}")
        print(f"ID: {student.student_id}")
        print(f"Level: {student.level}")
        print(f"Department: {student.department}")
        print(f"Registered: {'Yes' if student.is_registered else 'No'}")


# MAIN PROGRAM 

def main():
    """Main program function"""
    student_list = []
    
    print("=======================================================")
    print("  WELCOME TO OUR STUDENT MANAGEMENT SYSTEM")
    print("=======================================================")
    
    # Main program 's loop
    while True:
        display_menu()
        
        try:
            choice = int(input("\nChoose an option (1-3): "))
            
            if choice == 1:
                
                new_student = create_student()
                student_list.append(new_student)
                new_student.display_summary()
                print(f"\n✓ Student successfully created!")
                print(f"Total students in system: {Student.total_students}")
                
            elif choice == 2:
                # Display all students
                display_all_students(student_list)
                
                if len(student_list) > 0:
                    if validate_yes_no("\nDisplay details of a student? (yes/no): "):
                        index = int(input(f"Student number (1-{len(student_list)}): ")) - 1
                        if 0 <= index < len(student_list):
                            student_list[index].display_summary()
                        else:
                            print("The number is invalid!")
                
            elif choice == 3:
                # Exit the program
                print("\n" + "="*50)
                print("   Thank you for using our system!")
                print(f"   Total students created: {Student.total_students}")
                print("="*50)
                break
                
            else:
                print("Invalid option! Choose between 1 and 3 please.")
                
        except ValueError:
            print("Error! Enter a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()