
# Display the starting message
print("Program Started!")

# Ask the user to enter a character
print("Please enter a standard character:")
letter = input()

# Check if only one character was entered
if len(letter) == 1:

    # Find the ASCII code of the character
    value = ord(letter)

    # Display the result
    print(f"The ASCII code for {letter} is {value}.")

else:
    # Display an error message
    print("Error! Please enter only one character.")

# Display the ending message
print("Program Ended!")
