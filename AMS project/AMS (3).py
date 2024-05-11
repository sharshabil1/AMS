import os
from json import loads

# Admin login info
admin_name = "admin"
admin_password = "admin"


class Student:

    def __init__(self, st_id, name, sections):
        self.st_id = st_id
        self.name = name
        self.sections = sections


class FacultyMember:
    def __init__(self, fac_id, name, sections):
        self. fac_id = fac_id
        self.name = name
        self.sections = sections


def login(user_type = 3):
    os.system('cls')

    print("Enter your username and password.")
    username = input("Username: ")
    password = input("Password: ")

    if user_type == 1:
        if username == admin_name and password == admin_password:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Welcome, {username.capitalize()}!")
        else:
            response = input("Invalid user name or password! try again?(Y/N)").capitalize()
            if response == "Y" or response == "Yes":
                login(1)
            else:
                exit_program()
    elif user_type == 2:
        faculty_info = open("Faculty_member_info.txt")

        for line in faculty_info:
            # Search the file for the input ID and password
            current_fac_id = line[4:line.find("|Password")]
            current_password = line[(line.find("|Password: ") + 11): line.find("|Name")]
            # Compare input with ID's and names in file

            if username == current_fac_id and password == current_password:

                # Gather user info from file and turn into a faculty member object
                name = line[line.find("Name: ") + 6:line.find("|Sections")]
                # Turn sections string into a python list
                sections = loads(line[line.find("Sections: ") + 10:])
                faculty_info.close()

                return FacultyMember(current_fac_id, name, sections)
        else:
            response = input("Invalid user name or password! try again?(Y/N)").capitalize()
            if response == "Y" or response == "Yes":
                return login(2)
            else:
                exit_program()

    # Student login process
    elif user_type == 3:
        student_info = open("student_info.txt")

        for line in student_info:
            # Search the file for the input ID and password
            current_st_id = line[4:line.find("|Password")]
            current_password = line[(line.find("|Password: ") + 11): line.find("|Name")]
            # Compare input with ID's and names in file

            if username == current_st_id and password == current_password:

                # Gather user info from file and turn into a Student object
                name = line[line.find("Name: ") + 6:line.find("|Sections")]
                # Turn sections string into a python list
                sections = loads(line[line.find("Sections: ") + 10:])
                student_info.close()

                return Student(current_st_id, name, sections)
        else:
            response = input("Invalid user name or password! try again?(Y/N)").capitalize()
            if response == "Y" or response == "Yes":
                return login(3)
            else:
                exit_program()

def logout():
    os.system('cls' if os.name == 'nt' else 'clear')
    current_user = None
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Logged out successfully.")
    cont = input("press any key to continue: ")
    select()


def exit_program():
  print("Exiting program...")
  os.system('cls' if os.name == 'nt' else 'clear')
  exit()
  

def select():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to The Attendance Monitoring System")
    print("Are you:")
    print("1. Administrator")
    print("2. Faculty member")
    print("3. Student")
    print("4. Exit")

    userType = input("Enter your choice (1-4): ")
    if userType == '1':
        login(1)
        adminMenu()
    elif userType == '2':
        user = login(2)
        facultyMenu(user)
    elif userType == '3':
        user = login(3)
        studentMenu(user)
    elif userType == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please enter a number between 1 and 4.")
        input("Press any key to continue: ")
        select()


def studentMenu(user):
    print(f"Hello {user.name.capitalize()}!\n")

    while True:

        print("1. List Sections")
        print("2. Upload excuse")
        print("3. Logout")

        studentChose = input("Enter your choice (1-3): ")

        if studentChose == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sections:")
            print("1- FOS/6")
            cont = input("press any key to continue: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif studentChose == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Add Your File Here")
            cont = input("press any key to continue: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif studentChose == '3':
            logout()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid choice. Please enter a number between 1 and 3.")


def adminMenu():

    while True:
        print("1. Review Excuses")
        print("2. Logout")

        adminChose = input("Enter your choice (1-2): ")

        if adminChose == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1- Mohammed, File//:")
            print("2- Ahmed, File//:")
            print("3- Ali, File//:")
            cont = input("press any key to continue: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif adminChose == '2':
            logout()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid choice. Please enter a number between 1 and 2.")


def facultyMenu(user):
    print(f"Hello {user.name.capitalize()}!")

    while True:
        print("Faculty Menu")
        print("1. List Sections")
        print("2. Record Attendance")
        print("3. Logout")

        facultyChose = input("Enter your choice (1-3): ")

        if facultyChose == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Sections:")
            print("1- FOS/6")
            print("1- Electric Circuits/1")
            cont = input("press any key to continue: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif facultyChose == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Students List:")
            print("1- Mohammed")
            print("2- Ahmed")
            print("3- Ali")
            cont = input("press any key to continue: ")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif facultyChose == '3':
            logout()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid choice. Please enter a number between 1 and 3.")

select()
