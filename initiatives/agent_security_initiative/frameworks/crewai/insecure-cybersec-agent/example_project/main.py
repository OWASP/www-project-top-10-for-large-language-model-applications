import db
import utils
import config


def main():
    print("Welcome to the insecure app!")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if db.authenticate(username, password):
        print("Login successful!")
        command = input("Enter system command: ") 
        utils.run_system_command(command)
    else:
        print("Invalid credentials.")


if __name__ == "__main__":
    main()
