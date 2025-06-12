import random
import string

def generate_random_email(domain="example.com", prefix="testuser"):
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{random_str}@{domain}"