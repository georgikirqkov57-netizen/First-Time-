
# Ask the user how many rows to display
print("How many rows should I have?")
rows = int(input())

# Ask the user how many columns to display
print("\nHow many columns should I have?")
columns = int(input())

# Display the starting message
print("\nHere I go:\n")

# Display a grid using nested loops
for row in range(rows):
    for column in range(columns):
        print(":-) ", end="")
    print()

# Display the completion message
print("\nDone!")
