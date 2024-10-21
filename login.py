import time
def login():
    user_credentials = {'yuvraj@29': 'yuvi'}
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_credentials and user_credentials[username] == password:
        time.sleep(0.5)
        print("Login successful! Welcome, " + username + "!")
    else:
        time.sleep(0.5)
        print("Invalid username or password. Please try again.")

login()
