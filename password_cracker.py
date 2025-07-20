import hashlib

hashed = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

with open("wordlist.txt","r") as file:
    for line in file:
        print(f"Trying: {line.strip()}")
        if hashlib.sha256(line.strip().encode()).hexdigest() == hashed:
            print(f"Password cracked: {line.strip()}")
            break