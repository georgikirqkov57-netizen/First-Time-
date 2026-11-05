
# Define a function that takes an escape plan
def escape_by(plan):

    # Check the selected escape plan
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")

    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")

    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")

    else:
        print("We cannot escape that way! The boulder is in the way!")


# Call the function with different plans
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")
