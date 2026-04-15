from fpdf import FPDF
def generate_report(students, topper, class_avg, failed_students):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 16)
    
    pdf.cell(0, 10, "Student Result Analysis Report", ln=True, align='C')

    pdf.ln(10)
    
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Summary", ln=True)
    
    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 10, f"Total Students: {len(students)}", ln=True)

    pdf.cell(0, 10, f"Class Average: {class_avg:.2f}", ln=True)
    
    pdf.cell(0, 10, f"Topper: {topper.name}", ln=True)
    
    pdf.cell(0, 10, f"Failed Students: {len(failed_students)}", ln=True)
    
    pdf.ln(10)
    
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Student Details", ln=True)
    
    pdf.set_font("Arial", "", 10)
    
    for s in students:
        pdf.cell(
            0, 8,
            f"{s.name} | Total: {s.get_total()} | Avg: {s.get_average():.2f} | Grade: {s.get_grade()}",
            ln=True
        )
    
    pdf.ln(10)
    
    
    
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Failed Students", ln=True)
    
    pdf.set_font("Arial", "", 10)
    
    for s in failed_students:
        pdf.cell(0, 8, f"{s.name}", ln=True)
    
    

    
    pdf.output("output/report.pdf")