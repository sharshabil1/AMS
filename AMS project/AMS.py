# Define user roles
USER_ROLES = {"faculty", "student", "admin"}

# User data (replace with database interaction later)
users = {
    "faculty1": {"password": "pass1", "role": "faculty", "section": "CS101"},
    "student1": {"password": "pass2", "role": "student", "section": "CS101"},
    "admin": {"password": "admin", "role": "admin"},
}

# Current user
current_user = None


def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]["password"] == password:
        global current_user
        current_user = username
        print(f"Welcome, {current_user}!")
    else:
        print("Invalid username or password.")


def logout():
    global current_user
    current_user = None
    print("Logged out successfully.")


def select_section(faculty):
    if faculty["role"] != "faculty":
        print("You are not authorized to perform this action.")
        return
    section = input("Enter section code (e.g., CS101): ")
    faculty["section"] = section


def record_attendance(faculty):
    if faculty["role"] != "faculty":
        print("You are not authorized to perform this action.")
        return
    section = faculty["section"]
    # Simulate attendance recording (replace with actual attendance recording logic)
    print(f"Attendance recording started for section {section}.")
    # (Later, update attendance data for students in this section)


def list_attendance(student):
    if student["role"] != "student":
        print("You are not authorized to perform this action.")
        return
    section = student["section"]
    # Simulate attendance retrieval (replace with actual data retrieval)
    print(f"Attendance for section {section} (placeholder data):")
    print("Date         | Status")
    print("------------|-------")
    print("2024-05-08   | Present")
    print("2024-05-07   | Absent")


def upload_excuse(student):
    if student["role"] != "student":
        print("You are not authorized to perform this action.")
        return
    excuse_file = input("Enter path to excuse file (e.g., excuse.txt): ")
    # Simulate excuse upload (replace with actual file handling)
    print(f"Excuse file uploaded from {excuse_file}.")
    # (Later, store excuse details and link it to the student)


def review_excuses(admin):
    if admin["role"] != "admin":
        print("You are not authorized to perform this action.")
        return
    # Simulate excuse retrieval (replace with actual data retrieval)
    print("List of excuses:")
    print("Student ID | Excuse File")
    print("-----------|------------")
    print("student1   | excuse.txt")
    print("---------- (more excuses may exist) ----------")
    excuse_choice = input("Enter student ID to review excuse (or 'q' to quit): ")
    if excuse_choice.lower() != "q":
        # Simulate excuse review and decision (replace with actual logic)
        print(f"Reviewing excuse for student {excuse_choice} (placeholder).")
        decision = input("Enter 'a' to accept or 'r' to reject: ")
        if decision.lower() == "a":
            print(f"Excuse for student {excuse_choice} accepted.")
        elif decision.lower() == "r":
            print(f"Excuse for student {excuse_choice} rejected.")
        else:
            print("Invalid decision.")


def main_menu():
    if not current_user:
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            login()
        elif choice == "2":
            exit()
        else:
            print("Invalid choice.")
    else:
        print(f"Logged in as: {current_user} ({users[current_user]['role']})")
        if users[current_user]["role"] == "faculty":
            print("1. Select Section")
            print("2. Record Attendance")
            print("")
main_menu()
