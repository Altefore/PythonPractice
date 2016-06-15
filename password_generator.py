# simple password generator

import random
import string

def main():
    #length = input("Input desired password length (6-20)")
    password = generate_password(10) #(length)
    print("Your randomly generated password is: %s" %password)

def generate_password(len):
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(len))
    return password


if __name__ == "__main__":
    main()
