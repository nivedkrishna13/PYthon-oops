class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.map = {}
        self.menu()
    def signup(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        self.map[self.username] = self.password
        print("Signup successful! Please login to continue.")
        self.menu()
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.map and self.map[username] == password:
            print("Login successful! Welcome, " + username + "!")
            self.loggedin = True
            self.menu()
        else:
            print("Invalid username or password. Please try again.")
            self.menu()
    def write_post(self):
        if self.loggedin:
            post = input("Write your post: ")
            print("Post successful! Your post: " + post)
            self.menu()
        else:
            print("You must be logged in to write a post.")
            self.menu()
    def message_friend(self):
        if self.loggedin:
            friend = input("Enter your friend's username: ")
            message = input("Enter your message: ")
            print("Message sent to " + friend + ": " + message)
            self.menu()
        else:
            print("You must be logged in to message a friend.")
            self.menu()
    def exit(self):
        if self.loggedin:
           print("Goodbye!")
           self.loggedin = False

        else:
            print("login first to exit")
        exit()


    def menu(self):
        user_input = input("welcome to chatbook! How would you like to proceed? (1) Login (2) Sign Up (3) Exit: " +
        "\nPress 1 to signup\nPress 2 to login\npress 3 to write a post\npress 4 to message a friend\npress 5 to exit: ")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.write_post()
        
        elif user_input == "4":
            self.message_friend()x
        elif user_input == "5":
            self.exit()
        else:
            print("Invalid input, please try again.")
            self.menu()

obj = chatbook()