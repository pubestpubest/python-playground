blacklist = ["root","admin","test"]
attempts = 3
password = "toor"
blacklist_flag = False

print("server 1: authentication")

username = input("username: ")

for user in blacklist:
    if user == username:
        print("authentication failed")
        blacklist_flag = True
        break
        

while attempts > 0 and not blacklist_flag:
    passwd = input("password: ")
    if passwd == password:
        print("authentication success\nsystem accessed")
        break
    else:
        attempts-=1

if attempts == 0 or blacklist_flag:
    print("ALERT: unauthorized login attempt")


