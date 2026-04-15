import pandas as pd
from src.student import Student
def load_students():
    df = pd.read_csv("data/students.csv")
    students = []
    for _, row in df.iterrows():
        student_id = row["student_id"]   
        name = row["name"]               
        marks = {
            "math": row["math"],
            "science": row["science"],
            "english": row["english"],
            "history": row["history"],
            "computer": row["computer"]
        }
        
        student = Student(student_id, name, marks)
        students.append(student)
    
    return students


def get_topper(students):
    return max(students, key=lambda s: s.get_total())

def get_failed_students(students):
    return [s for s in students if not s.is_pass()]

def get_class_average(students):
    total = sum(s.get_average() for s in students)
    return total / len(students)

def get_rank_list(students):
    sorted_students = sorted(students, key=lambda s: s.get_total(), reverse=True)
    rank_list = []
    
    for i, student in enumerate(sorted_students, start=1):
        rank_list.append((i, student)) 
    
    return rank_list