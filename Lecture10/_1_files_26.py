import string
import random

for letter in string.ascii_uppercase:
    file_name = letter + '.txt'
    with open(file_name, 'w') as file:
        file.write(str(random.randint(1, 100)))

with open('summary.txt', 'w') as outputfile:
    for letter in string.ascii_uppercase:
        file_name = letter + '.txt'
        with open(file_name, 'r') as inputfile:
            info = inputfile.read()
        outputfile.write(f'{file_name}: {info} ')
 