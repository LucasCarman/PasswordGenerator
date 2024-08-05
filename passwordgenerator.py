import secrets
import random
def createPassword(length, case):
    i = 0
    iterator = 0
    decision = ''
    password = ['']
    characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '*']
    concPass = ''
    while iterator < length:
        decision = secrets.choice(characters)
        decision = str(decision)
        if case == True:
            makeUpper = bool(random.getrandbits(1))
            if makeUpper == True:
                decision = decision.upper()
                password.append(decision)
                iterator+= 1
            else:
                password.append(decision)
                iterator += 1
        else:
            password.append(decision)
            iterator += 1
    while i < len(password):
        concPass += password[i]
        i += 1
    return concPass
