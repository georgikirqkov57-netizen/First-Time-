
# Ask the user for the brightness level
print("What level of brightness is required?")
brightness = int(input())

# Display the starting message
print("\nAdjusting brightness...\n")

# Increase brightness using a for loop
for level in range(2, brightness + 1, 2):
    print(f"Brightness level: {'*' * level}")

# Display the final message
print("\nComplete!")
