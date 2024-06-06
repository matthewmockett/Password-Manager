from passwordManager import passwordManager

class userInterface:

    @staticmethod
    def welcomeMessage():
        print("Welcome to password manager\n")
    @staticmethod
    def getPasswordInput():
        return input("Please enter your password you would like to store: ")
    @staticmethod
    def displayConfirmation(passwordHash):
        print(f"Success, your password has been saved: {passwordHash}")
    
    
def main():
    userInterface.welcomeMessage()
    password = userInterface.getPasswordInput()
    passwordHash = passwordManager.generatePassword(password)
    userInterface.displayConfirmation(passwordHash)

if __name__ == "__main__":
    main()
