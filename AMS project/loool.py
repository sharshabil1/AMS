import json

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    with open('student_info.txt', 'r') as file:
        user_data = json.load(file)
        
        if username in user_data:
            stored_password = user_data[username]['password']
            if password == stored_password:
                print(f"Welcome, {username}!")
                return True, user_data[username]['sections']
            else:
                print("Invalid password.")
        else:
            print("Invalid username.")
    
    return False, []

def studentMenu():
    logged_in, sections = login()

    if logged_in:
        while True:
            print("Student Menu")
            print("1. List Sections")
            print("2. Upload Excuse")
            print("3. Logout")
            
            studentChose = input("Enter your choice (1-3): ")
            if studentChose == '1':
                print("Your Sections:")
                for section in sections:
                    print(f"- {section}")
            elif studentChose == '2':
                print("Add Your File Here")
            elif studentChose == '3':
                logout()
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

def logout():
    print("Logged out successfully.")

def select():
    print("Welcome to The Attendance Monitoring System")
    while True:
        print("Are you:")
        print("1. Administrator")
        print("2. Faculty Member")
        print("3. Student")
        print("4. Exit")

        userType = input("Enter your choice (1-4): ")
        if userType == '1':
            adminMenu()
        elif userType == '2':
            facultyMenu()
        elif userType == '3':
            studentMenu()
        elif userType == '4':
            exit_program()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def adminMenu():
    print("Admin Menu")
    # Add admin functionalities here

def facultyMenu():
    print("Faculty Menu")
    # Add faculty functionalities here

def exit_program():
    print("Exiting program...")
    exit()

# Entry point of the program
if __name__ == "__main__":
    select()
