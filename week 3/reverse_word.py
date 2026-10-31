
# Ask the user to enter a phrase
print("What phrase do you want to see in reverse?")
phrase = input()

# Display the starting message
print("\nReversing...\n")

# Display the phrase in reverse using a for loop
print("The phrase is: ", end="")

for index in range(len(phrase) - 1, -1, -1):
    print(phrase[index], end="")

# Move to the next line
print()
