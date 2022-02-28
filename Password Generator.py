'''
Lucio
Febuary 23, 2022
This code will make a password generator.
'''

from random import randint

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\"", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"]

choice = input("Do you want symbols or not? ").lower()

if choice == "yes": 
    length = int(input("How long do you want the password to be? "))

    total = []

    def random_total(numbers, lowercase_letters, uppercase_letters, symbols):
        random_numbers = numbers[randint(0, len(numbers)-1)]
        random_lowercase_letters = lowercase_letters[randint(0, len(lowercase_letters)-1)]
        random_uppercase_letters = uppercase_letters[randint(0, len(uppercase_letters)-1)]
        random_symbols = symbols[randint(0, len(symbols)-1)]
        random_character = (random_numbers, random_lowercase_letters, random_uppercase_letters, random_symbols)
        character = random_character[randint(0, len(random_character)-1)]
        return character

    for x in range(length):
        total.append(random_total(numbers, lowercase_letters, uppercase_letters, symbols))

    for x in total:
        print (x, end="")

else:
    length = int(input("How long do you want the password to be? "))
    
    total = []
    
    def random_total(numbers, lowercase_letters, uppercase_letters):
        random_numbers = numbers[randint(0, len(numbers)-1)]
        random_lowercase_letters = lowercase_letters[randint(0, len(lowercase_letters)-1)]
        random_uppercase_letters = uppercase_letters[randint(0, len(uppercase_letters)-1)]
        random_character = (random_numbers, random_lowercase_letters, random_uppercase_letters)
        character = random_character[randint(0, len(random_character)-1)]
        return character

    for x in range(length):
        total.append(random_total(numbers, lowercase_letters, uppercase_letters))

    for x in total:
        print (x, end="")