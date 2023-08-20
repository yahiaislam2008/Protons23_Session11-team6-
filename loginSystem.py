# simple login system with dictionary

database = {}
constantMessage1 = "Hello pls Enter your username: "#i wanted to use a constant but had no idea what to do
#checks if username is in dattabase
def checkingCaseOfUserNameInDataBase(username):
    return username in database.keys()
#for login
def login():
    username = input(constantMessage1)
    if not checkingCaseOfUserNameInDataBase(username):
        return 0
    password = input("Password: ")
    if password == database[username]["password"]:
        return username
    else:
        return -1
#for register
def regrest():
    username = input(constantMessage1)
    if checkingCaseOfUserNameInDataBase(username):
        return 1
    password = input("New Password: ")
    secret = input("Now enter your secrete phrase for safekeeping: ")
    database[username] = {"password": password, "secret": secret}
    return -1
def printingOutAllChoicesAndReturnUserChoice():
    print("\nWhat would you like to do?")
    print("1) login ")
    print("2) register ")
    print("3) Exit\n")
    chossing = int(input("> "))
    print("")
    return chossing
while True: #loop runs forever till break
    c = printingOutAllChoicesAndReturnUserChoice()
    match c:
        case 1:

            s = ()  #write the name of the function

            if s == 0:
                print("error: username not found")
            elif s == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {s}!")
                print("Your secret phrase is:")
                print(database[s]["secret"])
            continue
        case 2:
            s= ()  #write the name of the function
            if s == 1:
                print("\nSuccessfuly Registered!")
            elif s==-1:
                print("error: username already exists")
            continue
        case 3:
            print("Thank You")
            break
        case _:
            print("error: invalid input")

#if u have anything to add do it and i'm with u