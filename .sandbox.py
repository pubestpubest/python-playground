import hashlib


with open("wordlist.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    hashed = hashlib.sha256(line.strip().encode()).hexdigest()
    with open("hashes.txt", "a") as file:
        file.write(hashed+"\n")