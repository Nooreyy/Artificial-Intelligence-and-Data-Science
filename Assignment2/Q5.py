'''Create a dictionary for a student with keys: name, age, grade. Update the age, 
add a new key city, and then print all keys and values separately.'''

# create a dictionary for a student
print("***Student Dictionary***")
student = {'name' : 'Noor', 
           'age' : 20,
           'grade' : 'A'}
print(student)

# update the age and add a new key city
print("\n***Update Age and Add City***")
student['age'] = 19
student['city'] = 'Faisalabad'
print(student)

# print all keys and values separately
print("\n***Keys***")
for key in student:
    print(key)

print("\n***Values***")
for value in student.values():
    print(value)