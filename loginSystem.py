# simple login system

database = {}


def username_exists(username):
    return username in database.keys()


def login():
    username = input("Username: ")
    if not username_exists(username):
        return 0
    password = input("Password: ")
    if password == database[username]["password"]:
        return username
    else:
        return -1
    

def register():
    username = input("Username : ")
    if username_exists(username) == True:
        return 1
    password = input("New Password: ")
    secret = input("Now enter your secrete phrase for safekeeping: ")
    database[username] = {"password": password, "secret": secret}
    return -1


def choices():
    print("\nWhat would you like to do?")
    print("1) login ")
    print("2) register ")
    print("3) Exit\n")
    inp = int(input("> "))
    print("")
    return inp


while True:
    choice = choices()
    match choice:


        case 1:

            func = (login()) 

            if func == 0:
                print("Error: username not found")
            elif func == -1:
                print("Error: incorrect password")
            else:
                print(f"\nWelcome back, {func}!")
                print("Your secret phrase is:")
                print(database[func]["secret"])
            continue


        case 2:
            func = (register()) 
            if func == -1:
                print("\nSuccessfuly Registered!")
            elif func == 1:
                print("Error: username already exists")
            continue


        case 3:
            print("Thank You")
            break

        
        case _:
            print("Error: invalid input")

