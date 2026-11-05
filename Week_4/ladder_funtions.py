
# Function to display a ladder
def display_ladder(steps):
    # Draw the requested number of steps
    for step in range(steps):
        print("| |")
        print("***")

    # Display the bottom of the ladder
    print("| |")


# Function to create a ladder
def create_ladder():
    # Ask the user for the number of steps
    print("How many steps remain?")
    steps = int(input())

    # Call the function to display the ladder
    print()
    display_ladder(steps)


# Start the program
create_ladder()
