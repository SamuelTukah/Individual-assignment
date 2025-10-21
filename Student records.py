# student_records.py
"""Question 1b - Student class, list of students, average marks function."""

from typing import List

class Student:
    def __init__(self, name: str, marks: float):
        self.name = name
        self.marks = float(marks)

    def display(self):
        """Print the student's information."""
        print(f"{self.name} => {self.marks}")

def compute_average(students: List[Student]) -> float:
    if not students:
        return 0.0
    total = sum(s.marks for s in students)
    return total / len(students)

if __name__ == "__main__":
    # Create Student objects and store in list
    students = [
        Student("Alice", 80),
        Student("Bob", 90),
        Student("Chris", 75)
    ]

    # Display details
    print("Student Records:")
    for s in students:
        s.display()

    # Compute average
    avg = compute_average(students)
    print(f"\nAverage marks: {avg:.2f}")
