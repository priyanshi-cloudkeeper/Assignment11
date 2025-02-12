import random
import string

def generate_password():
    uppercase = random.sample(string.ascii_uppercase, 2)
    lowercase = random.sample(string.ascii_lowercase, 2)
    numbers = random.sample(string.digits, 2)
    special_chars = random.sample("!@#$%&*", 1)
    
    all_chars = string.ascii_letters + string.digits + "!@#$%&*"
    remaining_chars = random.sample([char for char in all_chars if char not in uppercase + lowercase + numbers + special_chars], 9)
    
    password_list = uppercase + lowercase + numbers + special_chars + remaining_chars
    random.shuffle(password_list)
    
    return "".join(password_list)

print("Generated Password:", generate_password())
