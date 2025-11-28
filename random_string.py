import random
import string

length = int(input("Length: "))
chars = string.ascii_letters + string.digits
print("".join(random.choice(chars) for _ in range(length)))
