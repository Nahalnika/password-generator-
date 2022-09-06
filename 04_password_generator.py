
import random
from string import digits, punctuation, ascii_lowercase, ascii_uppercase

all_combination_from_digits_letters_symbols = digits + punctuation\
                                              + ascii_uppercase + ascii_lowercase
# put the lenght of the password
password_length = int(input("Enter the password length: "))

password = "".join(random.sample(all_combination_from_digits_letters_symbols, password_length))

print(f"This is your current password: {password}")