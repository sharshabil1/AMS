import json

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    with open('student_info.txt', 'r') as file:
        for line in file:
            # Remove spaces from the line and then parse as JSON
            cleaned_line = line.replace(" ", "")  # Remove all spaces from the line
            if cleaned_line.strip():  # Check if line is not empty after removing spaces
                try:
                    user_info = json.loads(cleaned_line.strip())
                except json.JSONDecodeError:
                    print("Error decoding JSON from line:", line)
                    continue
                stored_username = user_info.get('username')
                stored_password = user_info.get('password')
                
                # Check if entered username and password match stored credentials
                if username == stored_username and password == stored_password:
                    print(f"Welcome, {username}!")
                    return
        
        # If no matching credentials are found
        print("Invalid username or password.")
        choice = input("Do you want to try again? (yes/no): ").strip().lower()
        if choice == 'yes':
            login()
        else:
            select()


def logout():
    current_user = None
    print("Logged out successfully.")
    select()

def exit_program():
  print("Exiting program...")
  exit()

def select():
    print("Welcome to The Attendance Monitoring System")
    print("Are you:")
    print("1. Administrator")
    print("2. Faculty member")
    print("3. Student")
    print("4. Exit")

    userType = input("Enter your choice (1-4): ")
    if userType == '1':
        print("Admin")
        adminMenu()
    elif userType == '2':
        print("Member")
        facultyMenu()
    elif userType == '3':
        print("student")
        studentMenu()
    elif userType == '4':
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

def studentMenu():
    login()
    while True:


        with open('student_info.txt', 'r') as file:

            for line in file:
            # Remove spaces from the line and then parse as JSON
                cleaned_line = line.replace(" ", "")  # Remove all spaces from the line
                if cleaned_line.strip():  # Check if line is not empty after removing spaces
                    try:
                        user_info = json.loads(cleaned_line.strip())
                    except json.JSONDecodeError:
                        print("Error decoding JSON from line:", line)
                        continue
                    stored_username = user_info.get('username')
                
        
        
        print("Student Menu")
        print("1. List Sections")
        print("2. Upload excuse")
        print("3. Logout")


        studentChose = input("Enter your choice (1-3): ")

        if studentChose == '1':
            stored_username = user_info.get('username')
            print("Sections:")
            print("1- FOS/6")
        elif studentChose == '2':
            print("Add Your File Here")
        elif studentChose == '3':
            logout()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def adminMenu():
    login()
    while True:
        print("admin Menu")
        print("1. Review Excuses")
        print("2. Logout")


        adminChose = input("Enter your choice (1-2): ")

        if adminChose == '1':
            print("1- Mohammed, File//:")
            print("2- Ahmed, File//:")
            print("3- Ali, File//:")
        elif adminChose == '2':
            logout()
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

def facultyMenu():
    login()
    while True:
        print("faculty Menu")
        print("1. List Sections")
        print("2. Record Attendance")
        print("3. Logout")


        facultyChose = input("Enter your choice (1-3): ")

        if facultyChose == '1':
            print("Sections:")
            print("1- FOS/6")
            print("1- Electric Circuits/1")
        elif facultyChose == '2':
            print("Students List:")
            print("1- Mohammed")
            print("2- Ahmed")
            print("3- Ali")
        elif facultyChose == '3':
            logout()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

select()