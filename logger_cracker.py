import hashlib


def load_file(path):
    result = []
    with open(path,"r") as file:
        lines = file.readlines()
        for line in lines:
            result.append(line.strip())
    file.close()
    return result

hashes = load_file("hashes.txt")
wordlist = load_file("wordlist.txt")

cracked = {}
for hash in hashes:
    for word in wordlist:
        if hash == hashlib.sha256(word.encode()).hexdigest():
            cracked[word] = hash
            break
with open("cracked.txt","w") as file:
    for k,v in cracked.items():
        file.write(f"{k}:{v}\n")
    file.close()