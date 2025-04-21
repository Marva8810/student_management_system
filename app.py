from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://mansumansoora42:9946824808@cluster0.hd8gt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
db = client["student_db"]  # Database name
students_collection = db["students"]  # Collection name

@app.route("/")
def dashboard():
    # Fetch all student documents
    students = list(students_collection.find())

    # Calculate total students
    total_students = len(students)

    # Example: Count students by grade
    grade_distribution = {}
    for student in students:
        grade = student.get("grade", "Unknown")
        grade_distribution[grade] = grade_distribution.get(grade, 0) + 1

    return render_template(
        "dashboard.html",
        total_students=total_students,
        grade_distribution=grade_distribution,
        students=students
    )

if __name__ == "__main__":
    app.run(debug=True)
