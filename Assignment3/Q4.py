'''A company management system wants to manage employees.

Create a parent class called Employee with:

Attributes:
name
salary
Method:
show_details()
Then create a child class called Developer that inherits from Employee and adds:
programming_language
Create a method:
show_language()
Create an object of the Developer class and display all details.'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_language(self):
        print(f"Programming Language: {self.programming_language}")
# Create an object of the Developer class
developer = Developer("Noor Fatima", 80000, "Python")
# Display all details
developer.show_details()
developer.show_language()
