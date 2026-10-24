
# Ask the user to choose an adventure
print("What type of adventure should I have?")
adventure = input()

# Check if the adventure is scary or short
if adventure == "scary" or adventure == "short":
    print("\nEntering the dark forest!")

# Check if the adventure is safe or long
elif adventure == "safe" or adventure == "long":
    print("\nTaking the safe route!")

# Handle any other answer
else:
    print("\nNot sure which route to take.")
