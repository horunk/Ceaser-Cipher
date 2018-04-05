import sys
print("""

Welcome to the Ceaser Cipher encryption/decryption module!
This is done as a practice assignment from school - if you have any feedback please feel free to contact at github.com/horunk .

""")

def show_menu():
    while True:
        input_menu = input("""
Please type 'e' if you wish to encrypt a text file
or type 'd' if you wish to decrypt a text file    
""")
        if input_menu == "e":
            encryption()
        elif input_menu == "d":
            decryption()
        elif input_menu == "quit":
            sys.exit(0)
        else:
            print("\nUnavailable option. Please try again or type 'quit' to exit.\n")

def encryption():
    #loop until correct file name is receiver or user quits the program
    while True:
        input_filepath = input("\nPlease insert file name if file is in the program folder or full path to the file you wish to encrypt: \n")

        if (input_filepath == "quit"):
            sys.exit(0)
            print("program should exit now...")

        try:
            inputFile = open(input_filepath, "r")
            break
        except:
            print("\nFailed to open the file specified. Try again or type 'quit' to exit.")





    #loop until user correctly inserts a integer or quits the program
    while True:
        input_shift = input("\nPlease insert the integer for encryption: \n")

        if (input_filepath == "quit"):
            sys.exit(0)
            print("program should exit now...")



        if(input_shift.isdigit()):
            if (int(input_shift) > 26 or int(input_shift) < 1):
                print("The inserted integer should be from 1 to 26 for Ceaser Cipher to work. Try again or type 'quit' to exit.")
                continue
            else:
                shift = int(input_shift)
                break
        else:
            print("\nThe input was not a integer. Please insert integer or type 'quit' to exit.")




    for line in inputFile:
        newline = ""
        for letter in line.rstrip():
            numericValue = ord(letter)

            if(numericValue>96 and numericValue<123):
                numericValue = numericValue + shift

                if(numericValue > 122):
                    numericValue = numericValue - 26
            elif(numericValue>47 and numericValue<58):
                numericValue = numericValue + shift

                if(numericValue > 57):
                    numericValue = numericValue - 10
            elif (numericValue > 64 and numericValue < 91):
                numericValue = numericValue + shift

                if (numericValue > 90):
                    numericValue = numericValue - 26

            newline = newline + str(chr(numericValue))
        print(newline)

    print("\n The End!")
#end of encryption function

def decryption():
    #loop until correct file name is receiver or user quits the program
    while True:
        input_filepath = input("\nPlease insert file name if file is in the program folder or full path to the file you wish to decrypt: \n")

        if (input_filepath == "quit"):
            sys.exit(0)
            print("program should exit now...")

        try:
            inputFile = open(input_filepath, "r")
            break
        except:
            print("\nFailed to open the file specified. Try again or type 'quit' to exit.")





    #loop until user correctly inserts a integer or quits the program
    while True:
        input_shift = input("\nPlease insert the integer for decrytion: \n")

        if (input_filepath == "quit"):
            sys.exit(0)
            print("program should exit now...")

        if(input_shift.isdigit()):
            if (int(input_shift) > 26 or int(input_shift) < 1):
                print("The inserted integer should be from 1 to 26 for Ceaser Cipher to work. Try again or type 'quit' to exit.")
                continue
            else:
                shift = int(input_shift)
                break
        else:
            print("\nThe input was not a integer. Please insert integer or type 'quit' to exit.")



    for line in inputFile:
        newline = ""
        for letter in line.rstrip():
            numericValue = ord(letter)

            if(numericValue>96 and numericValue<123):
                numericValue = numericValue - shift

                if(numericValue < 97):
                    numericValue = numericValue + 26
            elif(numericValue>47 and numericValue<58):
                numericValue = numericValue - shift

                if(numericValue < 48):
                    numericValue = numericValue + 10
            elif (numericValue > 64 and numericValue < 91):
                numericValue = numericValue - shift

                if (numericValue < 65):
                    numericValue = numericValue + 26

            newline = newline + str(chr(numericValue))
        print(newline)

    print("\n The End!")


show_menu()