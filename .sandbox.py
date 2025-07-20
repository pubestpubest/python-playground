import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + "!@#$%^"
    return ''.join(random.choice(chars) for _ in range(length))

print("Generated password:", generate_password())
