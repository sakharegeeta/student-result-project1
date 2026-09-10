import csv
import os

FILE_NAME = "student_results.csv"


# 1. Create Excel/CSV file with header if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Name",
                    "Class",
                    "DBMS",
                    "TOC",
                    "AI",
                    "CN",
                    "Cloud",
                    "Robotics",
                    "Total",
                    "Percentage",
                    "Grade",
                ]
            )


# 2. Get student input and save to Excel
def get_result():
    name = input("Enter Student Name: ")
    student_class = input("Enter Class: ")

    dbms = int(input("Enter DBMS Marks: "))
    toc = int(input("Enter TOC Marks: "))
    ai = int(input("Enter AI Marks: "))
    cn = int(input("Enter Computer Network Marks: "))
    cloud = int(input("Enter Cloud Computing Marks: "))
    robotics = int(input("Enter Robotics and Automation Marks: "))

    total = dbms + toc + ai + cn + cloud + robotics
    percentage = total / 6

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    # Format percentage to 2 decimal places
    formatted_percentage = f"{percentage:.2f}%"

    # Save data into CSV/Excel file
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                name,
                student_class,
                dbms,
                toc,
                ai,
                cn,
                cloud,
                robotics,
                total,
                formatted_percentage,
                grade,
            ]
        )

    # Display result
    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Class:", student_class)
    print("DBMS:", dbms)
    print("TOC:", toc)
    print("AI:", ai)
    print("Computer Network:", cn)
    print("Cloud Computing:", cloud)
    print("Robotics and Automation:", robotics)
    print("Total:", total)
    print("Percentage:", formatted_percentage)
    print("Grade:", grade)
    print(
        "\n[Result successfully saved to Excel sheet ('student_results.csv')]"
    )


# 3. View saved records from Excel
def view_result():
    print("\n----- PREVIOUS STUDENT RESULTS -----")
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    else:
        print("No previous results found.")


# 4. Main Menu System
def menu():
    initialize_file()
    while True:
        print("\nSTUDENT RESULT MANAGEMENT SYSTEM")
        print("1. Get Result")
        print("2. View Previous Results")
        print("3. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            get_result()
        elif ch == "2":
            view_result()
        elif ch == "3":
            print("Thank you")
            break
        else:
            print("Enter valid choice")


# Start the program
menu()
