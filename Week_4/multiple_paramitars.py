
# Define a function with two parameters
def climb_ladder(remaining, crossed):

    # Compare remaining and crossed steps
    if remaining > crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# Call the function with different values
climb_ladder(5, 2)
climb_ladder(2, 5)
