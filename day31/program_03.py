passwords = ["12345", "password", "Abc!9876", "qwerty", "Python2026!"]
for i in passwords:
    if len(i)>=8:
     print("strong password")
    else:
        print("weak password")