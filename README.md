# Student Database Application

Student: Huayang Du    

## 1. Project Description

This project is a Python application connected to a PostgreSQL database. It allows users to manage student records through a simple command-line interface.

The application supports the following operations:

Display all student records.

Add a new student.

Update a student's email address.

Delete a student record.

## 2. Technologies Used

Python 3

PostgreSQL

psycopg2

python-dotenv

## 3. Database Setup

1. Install PostgreSQL on your computer.
2. Open pgAdmin and create a database named `student_db`.
3. Open the Query Tool for the `student_db` database.
4. Open and execute the SQL script located at `database/setup.sql`.

The script creates the `students` table and inserts three initial student records.

## 4. Installation

Make sure Python and PostgreSQL are installed.

Clone or download this repository, then open a terminal in the project directory.

Install the required Python packages:

```
py -m pip install -r requirements.txt
```

## 5. Configuration

Create a `.env` file in the root directory of the project.

Add your PostgreSQL connection information:

```
DB_NAME=student_db
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
DB_PORT=5432
```

Replace `your_postgresql_password` with your own PostgreSQL password.

Do not upload your `.env` file to GitHub.

## 6. Running the Application

From the project root directory, run:

```
py app/main.py
```

The application will display a menu with five options:

1. Display all students
2. Add a student
3. Update student email
4. Delete a student
5. Exit

Follow the instructions displayed in the terminal to manage student records.

## 7. Project Structure

```
Student-Database-Assignment/
├── app/
│   └── main.py
├── database/
│   └── setup.sql
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 8. Demonstration Video

Video link: [Add your demonstration video link here]

