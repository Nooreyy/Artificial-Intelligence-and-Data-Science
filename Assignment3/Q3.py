'''An online learning platform wants to store course information.

Create a class called Course that contains:

Constructor parameters:

course_name
instructor_name
students_enrolled
Create a method:

show_course_info()
This method should display all course details.

Create three course objects and display their information.'''

class Course:
    def __init__(self, course_name, instructor_name, students_enrolled):
        self.course_name = course_name
        self.instructor_name = instructor_name
        self.students_enrolled = students_enrolled

    def show_course_info(self):
        print(f"Course Name: {self.course_name}")
        print(f"Instructor Name: {self.instructor_name}")
        print(f"Students Enrolled: {self.students_enrolled}")
# Create three course objects
course1 = Course("Python Programming", "Salman Raza", 150)
course2 = Course("Data Science", "Toqeer Mehmood", 200)
course3 = Course("Machine Learning", "Danial Zafar", 250)
# Display course information
course1.show_course_info()
print()  
course2.show_course_info()
print()  
course3.show_course_info()

