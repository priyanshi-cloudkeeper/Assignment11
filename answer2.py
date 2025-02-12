import random
import string

def generate_password():
    u = random.sample(string.ascii_uppercase, 2)
    l = random.sample(string.ascii_lowercase, 2)
    num = random.sample(string.digits, 2)
    special_char= random.sample("!@#$%&*", 1)
    
    all_chars = string.ascii_letters + string.digits + "!@#$%&*"
    remaining_char = random.sample([char for char in all_chars if char not in u + l + num + special_char], 9)
    
    password_list = u + l + num + special_char + remaining_char
    random.shuffle(password_list)
    
    return "".join(password_list)

print("Generated Password:", generate_password())
