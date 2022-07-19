key = "test"

while True:
    try:
        password = input("enter the password: ")
        if password.lower() == key:
            print("LINK.com")
            break
        print("incorrect password")
        continue
    except:
        print("error, reload.")
