from operator import countOf
import random

usable_characters = "aAbBcCdDeEfFgGhHjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890-=+_)(*&^%$£!{}[]\/'"
max_index = len(usable_characters) - 1
password = ""

x = 0
max_pw_characters = 20
while x < max_pw_characters:
    rand = random.randrange(0,max_index)
    password = password + usable_characters[rand]
    x = x + 1
print("Here is your new 20 character password: " + str(password))