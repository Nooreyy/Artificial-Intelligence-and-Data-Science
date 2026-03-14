'''Create a dictionary storing 2 students' data. Each student has name, age, marks 
(marks can be a list of 3 subjects). Write code to print each student’s name and average 
marks.'''

# create a dictionary storing 2 students' data
print("***Students Dictionary***")
students = {
    'student1': {
        'name': 'Noor',
        'age': 20,
        'marks': [85, 90, 78]
    },
    'student2': {
        'name': 'Aisha',
        'age': 22,
        'marks': [92, 88, 95]
    }
}

# print each student’s name and average marks
for student_id, student_info in students.items():
    name = student_info['name']
    average_marks = sum(student_info['marks']) / len(student_info['marks'])
    print(f"{name}: Average Marks = {average_marks:.2f}")