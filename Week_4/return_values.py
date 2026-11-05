
# Calculate the total weight
def sum_weights(person, inventory):
    total = person + inventory
    return total


# Calculate the average weight
def calc_avg_weight(person, inventory):
    total = sum_weights(person, inventory)
    average = total / 2
    return average


# Run the program
def run():
    # Ask for the two weights
    print("What is the weight of the person?")
    person = float(input())

    print("\nWhat is the weight of their inventory?")
    inventory = float(input())

    # Ask what to calculate
    print("\nWhat would you like to calculate (sum or average)?")
    choice = input()

    # Display the selected calculation
    if choice == "sum":
        result = sum_weights(person, inventory)
        print(f"\nThe sum of weights is {result:g}.")

    elif choice == "average":
        result = calc_avg_weight(person, inventory)
        print(f"\nThe average weight is {result:g}.")


# Start the program
run()
