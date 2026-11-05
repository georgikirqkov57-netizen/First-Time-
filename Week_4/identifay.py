
# Define a function to identify what is ahead
def identify():
    # Ask the user what they can see
    print("What lies before us?")
    object_seen = input()

    # Check if the object is a large boulder
    if object_seen == "a large boulder":
        print("\nIt's time to run!")
    else:
        print("\nWe will be fine.")

# Call the function
identify()
