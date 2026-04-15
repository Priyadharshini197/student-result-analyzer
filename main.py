from src.analyzer import (
    load_students,
    get_topper,
    get_failed_students,
    get_class_average
)

from src.visualizer import plot_subject_averages, plot_pass_fail
from src.report import generate_report

students = load_students()
topper = get_topper(students)
failed_students = get_failed_students(students)
class_avg = get_class_average(students)

plot_subject_averages(students)
plot_pass_fail(students)

generate_report(students, topper, class_avg, failed_students)

print("Executed successfully! Check output folder.")