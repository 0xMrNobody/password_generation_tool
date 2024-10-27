import random
import string
import argparse
import sys
import time

# Argument parser
parser = argparse.ArgumentParser(description='A simple CLI example.')

parser.add_argument('-l', '--length', type=int, help='Length of the passwords generated. Example: "-l 12"')
parser.add_argument('-n', '--number', type=int, help='Number of passwords you would like generated. Example: "-n 100"')
parser.add_argument('-m', '--mode', type=str, help='Which character sets will be used. "a = alphabet", "b = numbers", "c = punctuation" Examples: "-m a", "-m abc", "-m ac"')

args = parser.parse_args()

if args.length:
    passLength = args.length

if args.number:
    passNumber = args.number

if args.mode:
    passMode = args.mode

# Loading bar function
def loading_bar(iteration, total, length=40):
    percent = (iteration / total)
    arrow = '#' * int(length * percent)
    spaces = ' ' * (length - len(arrow))
    sys.stdout.write(f'\r|{arrow}{spaces}| {percent:.0%}')
    sys.stdout.flush()

# Function that generates the password
def generate_password(passLength, passMode):
    characterList = []
    for m in passMode: # Set the characters based on mode specified by user
        if m == 'a':
            characterList += string.ascii_letters
        if m == 'b':
            characterList += string.digits
        if m == 'c':
            characterList += string.punctuation
    # Generate and return password
    password = ''.join(random.choice(characterList) for i in range(passLength))
    return password


# Function that appends new passwords to the list and skips duplicate passwords that were generated
def append_unique(password):

    # Try to open the file
    try:
        with open('passwordlist.txt') as passFile:
            existing_lines = set(passFile.read().splitlines())
    except FileNotFoundError:
        existing_lines = set()  # File doesn't exist, start with an empty set


    # Check if password is unique
    if password not in existing_lines:
        with open('passwordlist.txt', 'a') as passFile:
            passFile.write(password + '\n')


# Generate passwords based on users input, check for duplicates to ignore, append the rest to the file
try:
    n = 0
    total_iterations = passNumber
    while n < passNumber:
        for i in range(total_iterations + 1):
            # Generate new password
            password = generate_password(passLength, passMode)

            # Append if password is unique
            append_unique(password)
            n += 1

            # Update and print loading bar
            loading_bar(i, total_iterations)
            time.sleep(0.000001)  # Simulate work being done

    print()
    print("password list has been created.")

except ValueError:
    print("Please input integers for your inputs and try again.")
