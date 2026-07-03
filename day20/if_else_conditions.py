def login(a,b):
    if(a=="admin" and b=="password123"):
        print("succesfully logged in")
        loginpage()
    else:
        print("invalid")


def loginpage():
    print("welcome to TP world")


a=input("Enter the username:")
b=input("Enter the password:")
login(a,b)
