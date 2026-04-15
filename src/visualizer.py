import matplotlib.pyplot as plt
def plot_subject_averages(students):
    subject_totals = {
        "math": 0,
        "science": 0,
        "english": 0,
        "history": 0,
        "computer": 0
    }
    
    count = len(students)

    for s in students:
        for subject, mark in s.marks.items():
            subject_totals[subject] += mark
    
    subject_averages = {sub: total / count for sub, total in subject_totals.items()}
    subjects = list(subject_averages.keys())
    averages = list(subject_averages.values())
    plt.figure()
    plt.bar(subjects, averages)
    
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.title("Subject-wise Average Marks")
    plt.savefig("output/subject_averages.png")
    plt.show()

def plot_pass_fail(students):
    pass_count = sum(1 for s in students if s.is_pass())
    fail_count = len(students) - pass_count
    labels = ["Pass", "Fail"]
    sizes = [pass_count, fail_count]
    
    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    
    plt.title("Pass vs Fail Distribution")
    
    plt.savefig("output/pass_fail.png")
    
    plt.show()