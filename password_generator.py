import random
chars = "1234567890asdfghjklmnbvcxzqwertyuiopASDFGHJKLMNBVCXZQWERTYUIOP@#$&*"

length = int(input("enter length: "))
password = ""

for i in range(length):
    password += random.choice(chars)
print(password)