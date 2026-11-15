
import psycopg2
import os
from contextlib import closing
from dotenv import load_dotenv

# Load database configuration from .env file
load_dotenv()

# Database connection configuration
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "student_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
}


# ==========================================
# Database Connection
# ==========================================

def get_connection():
    """Create and return a PostgreSQL connection."""
    return psycopg2.connect(**DB_CONFIG)


# ==========================================
# READ: Get All Students
# ==========================================

def getAllStudents():
    """Retrieve and display all student records."""

    try:
        with closing(get_connection()) as conn:
            with conn:
                with conn.cursor() as cur:

                    cur.execute(
                        "SELECT * FROM students ORDER BY student_id;"
                    )

                    students = cur.fetchall()

                    print("\n========== All Students ==========")

                    if not students:
                        print("No student records found.")

                    for student in students:
                        print(student)

    except psycopg2.Error as e:
        print("Database error:", e)


# ==========================================
# CREATE: Add Student
# ==========================================

def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student record."""

    try:
        with closing(get_connection()) as conn:
            with conn:
                with conn.cursor() as cur:

                    cur.execute(
                        """
                        INSERT INTO students
                        (first_name, last_name, email, enrollment_date)
                        VALUES (%s, %s, %s, %s);
                        """,
                        (first_name, last_name, email, enrollment_date)
                    )

        print("Student added successfully!")

    except psycopg2.Error as e:
        print("Database error:", e)


# ==========================================
# UPDATE: Update Student Email
# ==========================================

def updateStudentEmail(student_id, new_email):
    """Update the email address of a student."""

    try:
        with closing(get_connection()) as conn:
            with conn:
                with conn.cursor() as cur:

                    cur.execute(
                        """
                        UPDATE students
                        SET email = %s
                        WHERE student_id = %s;
                        """,
                        (new_email, student_id)
                    )

                    if cur.rowcount > 0:
                        print("Student email updated successfully!")
                    else:
                        print("Student not found.")

    except psycopg2.Error as e:
        print("Database error:", e)


# ==========================================
# DELETE: Delete Student
# ==========================================

def deleteStudent(student_id):
    """Delete a student using their student ID."""

    try:
        with closing(get_connection()) as conn:
            with conn:
                with conn.cursor() as cur:

                    cur.execute(
                        """
                        DELETE FROM students
                        WHERE student_id = %s;
                        """,
                        (student_id,)
                    )

                    if cur.rowcount > 0:
                        print("Student deleted successfully!")
                    else:
                        print("Student not found.")

    except psycopg2.Error as e:
        print("Database error:", e)


# ==========================================
# Main Application Menu
# ==========================================

def main():

    while True:

        print("\n===== Student Database System =====")
        print("1. Display all students")
        print("2. Add a student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":

            getAllStudents()

        elif choice == "2":

            first_name = input("First name: ").strip()
            last_name = input("Last name: ").strip()
            email = input("Email: ").strip()
            enrollment_date = input(
                "Enrollment date (YYYY-MM-DD): "
            ).strip()

            if not first_name or not last_name or not email:
                print("Name and email cannot be empty.")
                continue

            addStudent(
                first_name,
                last_name,
                email,
                enrollment_date
            )

        elif choice == "3":

            try:
                student_id = int(input("Student ID: "))
                new_email = input("New email: ").strip()

                if not new_email:
                    print("Email cannot be empty.")
                    continue

                updateStudentEmail(student_id, new_email)

            except ValueError:
                print("Invalid student ID.")

        elif choice == "4":

            try:
                student_id = int(input("Student ID: "))
                deleteStudent(student_id)

            except ValueError:
                print("Invalid student ID.")

        elif choice == "5":

            print("Exiting application.")
            break

        else:

            print("Invalid choice. Please try again.")


# ==========================================
# Program Entry Point
# ==========================================

if __name__ == "__main__":
    main()
