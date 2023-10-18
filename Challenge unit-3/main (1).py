class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(students):
  return sorted(students, key=lambda student: student.cgpa, reverse=True)

# Test case 1:
students1 = [
  Student("Alice", "1", 3.5),
  Student("Bob", "2", 3.7),
  Student("Charlie", "3", 3.9),
  Student("David", "4", 3.8),
]
sorted_students1 = sort_students(students1)
for student in sorted_students1:
  print(f"{student.name}, {student.roll_number}, {student.cgpa}")

# Test case 2:
students2 = [
  Student("Eve", "5", 3.6),
  Student("Frank", "6", 3.5),
  Student("George", "7", 3.4),
  Student("Harry", "8", 3.3),
]
sorted_students2 = sort_students(students2)
for student in sorted_students2:
  print(f"{student.name}, {student.roll_number}, {student.cgpa}")