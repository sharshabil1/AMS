import os

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Enter your username and password.")
    username = input("Username: ")
    password = input("Password: ")
    if username  == "admin"  and password == "admin":
        current_user = username
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome, {current_user}!")
        
    else:
        print("Invalid username or password.")
        userContinue = input("Press Y to continue or n to exit: ")
        print("")
        if userContinue == 'y' or userContinue == 'Y':
            login()
        elif userContinue == 'n' or userContinue == 'N':
            exit()
        else:
            login()

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
        print("Admin")
        adminMenu()
    elif userType == '2':
        print("Member")
        facultyMenu()
    elif userType == '3':
        print("student")
        studentMenu()
    elif userType == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid choice. Please enter a number between 1 and 4.")
        input("Press any key to continue: ")
        select()

def studentMenu():

    login()
    while True:
        print("Student Menu")
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
    login()
    while True:
        print("admin Menu")
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

def facultyMenu():
    login()
    while True:
        print("faculty Menu")
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
