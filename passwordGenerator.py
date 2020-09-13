import string
import random

if __name__ == "__main__":

    upperCase = string.ascii_uppercase
    lowerCase = string.ascii_lowercase
    digits = string.digits
    specialChar = string.punctuation

    password = []
    elements = []
    elements.extend(list(upperCase))
    elements.extend(list(lowerCase))
    elements.extend(list(digits))
    elements.extend(list(specialChar))

    for element in range(int(random.randrange(12, 32, 1))):
        password.append(random.choice(elements))

    print(' '.join(password))
