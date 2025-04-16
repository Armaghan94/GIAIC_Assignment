import streamlit as st

# Helper functions
def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"

def validate_marks(marks_dict):
    for subject, marks in marks_dict.items():
        if marks < 0 or marks > 100:
            return False, subject
    return True, None

# Initialize session state
if 'students' not in st.session_state:
    st.session_state.students = []

# Title
st.title("📊 Student Report Card Generator")

with st.form("student_form", clear_on_submit=True):
    st.subheader("🔹 Enter Student Information")

    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")

    st.subheader("🔢 Enter Marks (0 to 100)")
    math = st.number_input("Math", min_value=0.0, max_value=100.0, step=1.0)
    physics = st.number_input("Physics", min_value=0.0, max_value=100.0, step=1.0)
    urdu = st.number_input("Urdu", min_value=0.0, max_value=100.0, step=1.0)
    english = st.number_input("English", min_value=0.0, max_value=100.0, step=1.0)
    computer = st.number_input("Computer", min_value=0.0, max_value=100.0, step=1.0)

    submitted = st.form_submit_button("➕ Add Student")

    if submitted:
        marks = {
            "Math": math,
            "Physics": physics,
            "Urdu": urdu,
            "English": english,
            "Computer": computer
        }

        valid, subject = validate_marks(marks)
        if not valid:
            st.error(f"❌ Invalid marks for {subject}. Must be between 0 and 100.")
        elif not name or not roll_no:
            st.warning("❗ Please enter both Student Name and Roll Number.")
        else:
            total = sum(marks.values())
            percentage = (total / 500) * 100
            grade = calculate_grade(percentage)

            student_record = {
                "name": name,
                "roll_no": roll_no,
                "marks": marks,
                "total": total,
                "percentage": percentage,
                "grade": grade
            }

            st.session_state.students.append(student_record)
            st.success(f"✅ Record of {name} inserted successfully!")

# Display all report cards
if st.session_state.students:
    st.subheader("📑 All Student Report Cards")

    for i, student in enumerate(st.session_state.students):
        with st.expander(f"📄 {student['name']} (Roll No: {student['roll_no']})"):
            st.write("### Marks")
            st.table(student["marks"])
            st.write(f"**Total Marks:** {student['total']} / 500")
            st.write(f"**Percentage:** {student['percentage']:.2f}%")
            st.write(f"**Grade:** {student['grade']}")
