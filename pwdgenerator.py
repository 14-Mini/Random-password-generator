# import random module
import random

# import string module
import string


def pwd_gen():
    pwd = []
    length = random.randint(6, 20)
    while len(pwd) <= length:
        # if you want your desired characters
        # fill out over here using whatever algorithm

        uppr = random.choice(string.ascii_uppercase)
        lwr = random.choice(string.ascii_lowercase)
        num = random.choice(string.digits)
        sym = random.choice(string.punctuation)
        pwd.append(uppr)
        pwd.append(lwr)
        pwd.append(num)
        pwd.append(sym)
    random.shuffle(pwd)
    pwd = ''.join(pwd)
    return pwd


print(pwd_gen())

