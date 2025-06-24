import random
import string

def generate_random_emp_id(prefix="EMP", length=4):
    return f"{prefix}{''.join(random.choices(string.digits, k=length))}"
