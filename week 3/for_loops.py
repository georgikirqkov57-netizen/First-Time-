
# Ask the user how many mountains to display
print("How many mountains should I display?")
mountains = int(input())

# Display the starting message
print("\nDisplaying...\n")

# Draw the mountains using a for loop
for count in range(mountains):
    print("      __")
    print("     /  \\_")
    print("    / ^   \\")
    print("   /  ^    \\_")
    print("  /_ ^ ^    ^\\")
    print(" /   ^   ^   \\")
    print()

# Display the final message
print("Done!")
