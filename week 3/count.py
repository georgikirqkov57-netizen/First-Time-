
# Ask how many obstacles to avoid
print("How many obstacles should I avoid?")
obstacles = int(input())

# Start counting from zero
avoided = 0

# Avoid obstacles using a while loop
while avoided < obstacles:
    print("Avoiding...", end="")
    avoided = avoided + 1
    print(f"Done! {avoided} obstacles avoided.")

# Display the final message
print("\nAll obstacles have been avoided.")
