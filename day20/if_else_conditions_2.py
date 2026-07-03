def login(a,b):
    if(a=="admin" and b=="password123"):
        print("succesfully logged in")
        return 1
    else:
        print("invalid")
        return 0


def homepage():
    print("welcome to TP world")
def errorpage():
    print("Error page")


a=input("Enter the username:")
b=input("Enter the password:")

c= login(a,b)
if(c==1):
    homepage()
else:
    errorpage()
