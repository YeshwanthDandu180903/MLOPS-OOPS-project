class Chatbook:
    #intilaizing the constructor
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input("Welcome to Chatbook! Please choose an option:\n1. Sign Up\n2. Log In\n3. Post\n4.Message\n5.Press any Button to exit")
        if user_input=='1':
            self.sign_up()
        if user_input=='2':
            self.log_in()
        if user_input=='3':
            self.write_a_post()
        if user_input=='4':
            self.message_a_friend()
        if user_input not in ['1','2','3','4']:
            print("Thanks for using the Chatbook app,See you again!")
            exit()
    

    def sign_up(self):
        self.username=input("Enter your email:")
        self.password=input("Enter your password:")
        print("Sign up successful! Your email is the username Please log in to continue.")
        self.menu()


    def log_in(self):
        if self.username=="" and self.password=="":
            print("No user found,Please Sign up first")

        else:
            username=input("Enter your username:")
            password=input("Enter your password:")
            if username==self.username and password==self.password:
                print("Login successful..")
                self.logged_in=True
            else:
                print("User Creditionals not matched.")
        print('\n')
        self.menu()

    def write_a_post(self):
        if self.logged_in==True:
            self.message=input("Whats on your mind!... ")
            print(f"Following content has been posted {self.message}")
        else:
            print("Login is required to post something")

    def message_a_friend(self):
        if self.logged_in==True:
            frnd=input("Name your Friend:")
            message=input("Write your message: ")

            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to Login.To message your friend")
        print('\n')
        self.menu()






obj=Chatbook()
