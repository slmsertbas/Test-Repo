import string
import random

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = "0123456789"
symbols = "!^+%&?*-"

def splitChar(word):
    return [char for char in word]

upper = splitChar(upper)
lower = splitChar(lower)
numbers = splitChar(numbers)
symbols = splitChar(symbols)


def generatePass():
    password = []
    random.shuffle(upper)
    random.shuffle(lower)
    random.shuffle(numbers)
    random.shuffle(symbols)

    for i in range(4):
        a = random.choice(upper)
        password.append(a)
    for i in range(2):
        a = random.choice(lower)
        password.append(a)
    for i in range(2):
        a = random.choice(numbers)
        password.append(a)

    

    s = [str(i) for i in password]
    random.shuffle(s)
    password = ''.join(s)

    return str(password)
    #print("Here is your randomly generated password: "+str(password))
    

#print("There will be 4 letters lower, 2 lettes upper and 2 numbers in your password.")
#generatePass()