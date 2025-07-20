from ast import Return


def check_username_blacklist(username):
    blacklist = ["root", "admin"]
    if username in blacklist:
        return True
    return False

def check_ip_blacklist(ip):
    blacklist = ["192.168.1.1", "localhost"]
    if ip in blacklist:
        return True
    return False

def check_password_strength(passwd):
    if len(passwd) < 6:
        return "weak"
    elif any( char.isdigit() for char in passwd) and any(char.isalpha() for char in passwd):
        return "strong"
    else:
        return "medium"


credentail = input("enter your credentail (e.g. john@localhost):")
username = credentail.split("@")[0]
ip = credentail.split("@")[1]

if check_username_blacklist(username):
    print(f"authentication failed for user {username}")
    exit()

if check_ip_blacklist(ip):
    print(f"authentication failed for ip {ip}")
    exit()

passwd = input("password: ")
password_result = check_password_strength(passwd)
print(f"password strength: {password_result}")
if password_result == "weak":
    print("authentication falied: too weak password")
else:
    print("authentication success.")