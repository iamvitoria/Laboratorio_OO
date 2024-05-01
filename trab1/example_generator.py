# example_generator.py
import random
import string

#Gera valores dinamicamente conforme o tipo de dado
def generate_random_value(column_type):
    if column_type == "INTEGER":
        return random.randint(1, 100)
    elif column_type == "REAL":
        return round(random.uniform(1.0, 100.0), 2)
    elif column_type == "TEXT":
        return "'" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "'"
    elif column_type == "BLOB":
        return bytes(random.getrandbits(8) for _ in range(10))
    else:
        return None