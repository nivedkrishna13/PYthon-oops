class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    def signup(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        print("Signup successful! Please login to continue.")
        self.menu()

    def menu(self):
        user_input = input("welcome to chatbook! How would you like to proceed? (1) Login (2) Sign Up (3) Exit: " +
        "\nPress 1 to signup\nPress 2 to login\nPress 3 to login\npress 3 to write a post\npress 4 to message a friend\npress 5 to exit: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            print("Goodbye!")
        else:
            print("Invalid input, please try again.")
            self.menu()

obj = chatbook()