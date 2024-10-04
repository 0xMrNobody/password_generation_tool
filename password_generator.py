import random
import string
import numbers

# The function that generates a password for the user.
def generate_password(length, alph, digits, punct):

    # Start with an empty list of characters and append onto it the options the user selected.
    characterList = ""
    if alph == True:
        characterList = characterList + string.ascii_letters
    if digits == True:
        characterList = characterList + string.digits
    if punct == True:
        characterList = characterList + string.punctuation

    if characterList == "":
        print("Sorry, you did not select any character options so no password was generated")
    else:
        # Generate and return the password.
        password = ''.join(random.choice(characterList) for i in range(length))
        return password


# Define menu variable.
selection = "y"

while selection == "y":
    selection = input("Would you like to generate a new password? (y/n)")

    if selection == "y":
        # Try to take users input. If non-integer is giving, handle exception.
        try:
            length = int(input("How long is your new password? "))

            # Make sure integer is great than 0.
            if length > 0:

                # Ask user what they want and prepare variable to be passed to our generate_password() function.
                alph = input("Would you like to use all of the ascii letters? (y/n) ")
                digits = input("Would you like to use numbers? (y/n) ")
                punct = input("Would you like to use punctuation (y/n) ")

                if alph == 'y':
                    alph = True
                if digits == 'y':
                    digits = True
                if punct == 'y':
                    punct = True

                # Receive results from the function and output to user
                password = generate_password(length, alph, digits, punct)
                print (f"Here is the password: {password}")

            else:
                print ("Sorry, please input a valid positive integer.")

        except:
            selection = "y"
            print ("invalid input detected.")


        selection == True
    elif selection == "n":
        print("Successfully quit application.")
        selection = "n"

    else:
        print("Invalid option.")
        selection = "y"
