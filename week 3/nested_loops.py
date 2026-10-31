
# Ask the user for the number of rows
print("How many rows should I have?")
rows = int(input())

# Ask the user for the number of columns
print("\nHow many columns should I have?")
columns = int(input())

# Display the starting message
print("\nHere I go:\n")

# Create a grid using nested for loops
for row in range(rows):
    for column in range(columns):
        print(":-) ", end="")
    print()

# Display the completion message
print("\nDone!")
