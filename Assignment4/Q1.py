import numpy as np

# Generate random marks for 50 students in 5 subjects (0-100)
np.random.seed(42)
marks = np.random.randint(30, 100, size=(50, 5))
subjects = ["Math", "Science", "English", "History", "CS"]

# 1. Average marks per student
avg_per_student = marks.mean(axis=1)
print("Average marks per student (first 5):")
print(avg_per_student[:5].round(2))

# 2. Topper — student with highest total marks
total_marks = marks.sum(axis=1)
topper_index = np.argmax(total_marks)
print(f"\nTopper: Student {topper_index + 1}")
print(f"Total marks: {total_marks[topper_index]}")
print(f"Marks by subject: {marks[topper_index]}")

# 3. Students who failed any subject (marks < 40)
failed_mask = np.any(marks < 40, axis=1)
failed_students = np.where(failed_mask)[0] + 1  # 1-indexed
print(f"\nStudents who failed at least one subject:")
print(f"Student IDs: {failed_students}")
print(f"Total failed: {len(failed_students)}")

# Bonus: Which subject has the most failures?
fail_per_subject = (marks < 40).sum(axis=0)
for s, f in zip(subjects, fail_per_subject):
    print(f"  {s}: {f} failures")
most_failed_subject = subjects[np.argmax(fail_per_subject)]
print(f"\nSubject with most failures: {most_failed_subject} ({fail_per_subject.max()} failures)")   
