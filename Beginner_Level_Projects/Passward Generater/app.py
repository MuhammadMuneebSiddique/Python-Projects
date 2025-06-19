import random
import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
digit = string.digits
symbol = "!@#$%^&*()_-+=}{|:;"

passward = ""

while len(passward) <= 8:
    passward += random.choice(upper_case)
    passward += random.choice(lower_case)
    passward += random.choice(symbol)
    passward += random.choice(digit)

print(f"Strong Passward is {passward}")